#!/usr/bin/env python3
"""Canada Home Gym Price Watch, standalone checker, stages A to C.

OBSERVE ONLY. Reads data/products.json, fetches each selected product's
own retailer page, extracts the current price, the compare at price, and
availability, applies the spec price rules, and writes a run report.
It never writes back to the data file and never changes a price.

Stage A: the seven Shopify stores, read through the Shopify product
JSON endpoints (.js first, then .json, then a page JSON-LD fallback).

Stage B adds:
- Second pass readers for Fitness Depot, Fitness Depot Plus, Decathlon
  Canada, Horizon Fitness Canada, and Great Life Fitness: the product
  page's structured data (JSON-LD offers) where present, falling back
  to the page's stated price (og:price meta).
- A Peloton Canada reader: Peloton states no structured offer. Its
  pages carry an embedded Canadian price table (the regular price) in
  the page's __NEXT_DATA__ JSON and the current selling price in the
  financing legal text ("Based on a price of $X"), keyed by product
  name. Both are read from the product's own page.
- Rogue Canada handling per spec section 7: a failed Rogue read is an
  EXPECTED FAILURE, reported in its own section, never a gate failure
  and never treated as a price.
- The spec section 7 validation gates, evaluated and reported on every
  run in observe only form: they block nothing yet.
- A failure alert composer in dry run form: when a gate fails or a
  store's read failure rate in a run exceeds half its products, the
  exact alert email text is written into the run report. Nothing is
  sent.

Stage C adds:
- Readers for the last four stores without one: Costco Canada and
  Fitness Depot Toronto through the structured reader (Costco pages
  carry a JSON-LD offer with price and availability), and Lion Fitness
  and Matsuru through the Shopify reader (both are Shopify stores).
  Fitness Depot Plus moves from the structured reader to the Shopify
  reader: its pages are Shopify and the .js endpoint answers with the
  full variant list, which the og:price fallback could not see.
- Headline variant matching: where a record marks a headline variant,
  the reader selects that variant. Where a record carries no headline
  marker and the page sells several variants, the reader never silently
  takes the first variant: it identifies the tracked configuration by
  the recorded price when a variant carries it, and otherwise reports
  the record as missing its headline variant marker, with no read
  attributed to the tracked configuration.
- A compare mode (--reference live): the reference record is the
  published catalogue at https://canadahomegym.ca/, parsed from its
  embedded product data, instead of the local data file. The reads
  still come from the retailer pages. This is how the daily proof run
  compares against the app's published records.
- Repo layout support: when this file sits at tools/checker/checker.py
  in the published repo, the data file is data/products.public.json at
  the repo root and reports land in reports/ at the repo root.

Spec rules applied (standalone-checker-spec.md section 5):
- Shelf prices only. No tax figure is read or written.
- A read 40 percent or more away from the recorded price is a HELD
  read: reported as held, never treated as a price.
- Stock is recorded as the page states it (available or not).

Usage:
  python3 checker.py                  stage A subset (src/subset.json)
  python3 checker.py --subset2        stage B subset (src/subset2.json)
  python3 checker.py --all            every product at the Shopify stores
  python3 checker.py --all-stores     every product whose retailer has a reader
  python3 checker.py --slugs a,b,c    named products only
  python3 checker.py --reference live [--all-stores|--slugs a,b,c]
                                      compare against the live published
                                      catalogue instead of the data file
"""

import json
import re
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
_LOCAL_DATA = SCRIPT_DIR.parent / "data" / "products.json"
_REPO_DATA = SCRIPT_DIR.parent.parent / "data" / "products.public.json"
if _LOCAL_DATA.exists():
    # Development layout: checker/{src,data,reports}
    BASE = SCRIPT_DIR.parent
    DATA_FILE = _LOCAL_DATA
elif _REPO_DATA.exists():
    # Published repo layout: tools/checker/checker.py, data/ and
    # reports/ at the repo root.
    BASE = SCRIPT_DIR.parent.parent
    DATA_FILE = _REPO_DATA
else:
    BASE = SCRIPT_DIR.parent
    DATA_FILE = _LOCAL_DATA
SUBSET_FILE = SCRIPT_DIR / "subset.json"
SUBSET2_FILE = SCRIPT_DIR / "subset2.json"
REPORTS_DIR = BASE / "reports"

LIVE_URL = "https://canadahomegym.ca/"

SHOPIFY_STORES = [
    "Bells of Steel",
    "Montreal Weights",
    "Gorila Fitness",
    "Northern Fitness",
    "Treadmill Factory",
    "Force USA Canada",
    "Altas Strength",
    "Lion Fitness",
    "Matsuru",
    "Fitness Depot Plus",
]

STRUCTURED_STORES = [
    "Fitness Depot",
    "Decathlon Canada",
    "Horizon Fitness Canada",
    "Great Life Fitness",
    "Costco Canada",
    "Fitness Depot Toronto",
]

PELOTON_STORE = "Peloton Canada"
ROGUE_STORE = "Rogue Canada"

READER_STORES = (SHOPIFY_STORES + STRUCTURED_STORES
                 + [PELOTON_STORE, ROGUE_STORE])

ALERT_TO = "hancventures@gmail.com"
HELD_THRESHOLD = 0.40
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"}

# Peloton: recorded slug -> (embedded price table key, legal text name)
PELOTON_MAP = {
    "peloton-cross-training-bike": ("bike", "Cross Training Bike"),
    "peloton-tread-flex": ("tread-flex", "Peloton Tread Flex"),
    "peloton-tread-vision": ("tread", "Peloton Tread Vision"),
    "peloton-tread-plus-vision": ("tread-plus", "Peloton Tread+ Vision"),
    "peloton-cross-training-row-plus": ("row", "Cross Training Row+"),
}


def money(cents):
    if cents is None:
        return "not stated"
    return f"${cents / 100:,.2f}"


def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.status, resp.read().decode("utf-8", "replace")


def norm(text):
    return re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).strip()


STOP_TOKENS = {"lb", "lbs", "kg", "in", "inch", "inches", "cm", "mm",
               "to", "of", "the"}


def tokens(text):
    """Canonical token set for variant labels: splits glued number and unit
    pairs ('3LB' -> 3), drops units and filler words, so the recorded label
    'Standard 84.5 in' and the Shopify title 'Standard - 84.5" | 215cm'
    describe the same variant."""
    parts = re.findall(r"\d+\.?\d*|[a-z]+", (text or "").lower())
    return {t for t in parts if t not in STOP_TOKENS}


def select_variant(page_variants, recorded_variants, recorded_price):
    """Return (variant, how, missing_marker).

    Where the record marks a headline variant, select that variant by
    label, then by canonical tokens; if no page variant matches it,
    return None with missing_marker False and let the caller run its
    fallbacks.

    Where the record carries no headline marker, never silently take
    the first variant of a multi variant page. A single variant page is
    read as it stands. On a multi variant page the tracked
    configuration is identified by the recorded price when a variant
    carries it; when none does, return None with missing_marker True
    and the caller reports the record as missing its headline variant
    marker, attributing no read to the tracked configuration."""
    headline = None
    for v in recorded_variants or []:
        if v.get("is_headline_price_variant"):
            headline = v
            break
    if headline is not None:
        label = norm(headline.get("label", ""))
        for sv in page_variants:
            if norm(sv.get("title", "")) == label:
                return sv, (f"variant matched by label "
                            f"'{headline.get('label')}'"), False
        label_tokens = tokens(headline.get("label", ""))
        for sv in page_variants:
            title_tokens = tokens(sv.get("title", ""))
            if label_tokens and (label_tokens <= title_tokens
                                 or title_tokens <= label_tokens):
                return sv, (f"variant matched by tokens to "
                            f"'{headline.get('label')}'"), False
        return None, (f"no variant on the page matches recorded "
                      f"headline '{headline.get('label')}'"), False
    if len(page_variants) == 1:
        return page_variants[0], ("the page sells a single variant; "
                                  "the record carries no headline "
                                  "variant marker"), True
    if recorded_price is not None:
        cands = [v for v in page_variants
                 if v["price_cents"] == recorded_price]
        if cands:
            extra = (f"; {len(cands)} variants carry that price"
                     if len(cands) > 1 else "")
            return cands[0], (
                f"record is missing its headline variant marker; the "
                f"tracked configuration was identified by its recorded "
                f"price {money(recorded_price)} among the page's "
                f"{len(page_variants)} variants{extra}"), True
    return None, "", True


def canonical_product_path(url):
    m = re.search(r"(/products/[^/?#]+)", url or "")
    base = re.match(r"(https?://[^/]+)", url or "")
    if m and base:
        return base.group(1) + m.group(1)
    return (url or "").rstrip("/")


def _variant(title, price_cents, compare_cents, available):
    if compare_cents is not None and compare_cents <= 0:
        compare_cents = None
    return {"title": title, "price_cents": price_cents,
            "compare_cents": compare_cents, "available": available}


# ---------------------------------------------------------------- Shopify

def _shopify_endpoint_urls(url, ext):
    """Candidate endpoint URLs for a Shopify product: the canonical
    /products/ path first, then the recorded URL as it stands. Locale
    prefixed stores (Fitness Depot Plus records /en/products/...) 404
    on the canonical path and answer on the recorded one."""
    canon = canonical_product_path(url) + ext
    raw = (url or "").rstrip("/") + ext
    return [canon] if raw == canon else [canon, raw]


def read_shopify_js(url):
    """The .js endpoint: prices already in cents, availability per variant."""
    errors = []
    for candidate in _shopify_endpoint_urls(url, ".js"):
        try:
            status, body = fetch(candidate)
            data = json.loads(body)
            variants = data.get("variants") or []
            if not variants:
                raise ValueError("Shopify .js carried no variants")
            return [_variant(v.get("title", ""), int(v["price"]),
                             v.get("compare_at_price"), v.get("available"))
                    for v in variants], "Shopify .js"
        except Exception as e:
            errors.append(str(e))
    raise ValueError("; ".join(errors))


def read_shopify_json(url):
    """The .json endpoint: prices as dollar strings, no availability."""
    errors = []
    for candidate in _shopify_endpoint_urls(url, ".json"):
        try:
            status, body = fetch(candidate)
            data = json.loads(body)
            product = data.get("product") or {}
            variants = product.get("variants") or []
            if not variants:
                raise ValueError("Shopify JSON carried no variants")
            out = []
            for v in variants:
                cap = v.get("compare_at_price")
                out.append(_variant(v.get("title", ""),
                                    round(float(v["price"]) * 100),
                                    round(float(cap) * 100) if cap else None,
                                    v.get("available")))
            return out, "Shopify .json"
        except Exception as e:
            errors.append(str(e))
    raise ValueError("; ".join(errors))


def extract_jsonld_offers(body):
    """Walk every JSON-LD block on a page and return a list of offers as
    (price_cents, available_or_None) from Product structured data,
    including AggregateOffer low prices."""
    found = []

    def walk(node):
        if isinstance(node, dict):
            offers = node.get("offers")
            if offers is not None and (
                    node.get("@type") in ("Product", "IndividualProduct")
                    or "offers" in node):
                offer_list = offers if isinstance(offers, list) else [offers]
                for off in offer_list:
                    if not isinstance(off, dict):
                        continue
                    price = off.get("price")
                    if price is None and off.get("@type") == "AggregateOffer":
                        price = off.get("lowPrice")
                    if price is None:
                        continue
                    try:
                        cents = round(float(str(price).replace(",", "")) * 100)
                    except ValueError:
                        continue
                    if cents <= 0:
                        continue
                    avail_raw = str(off.get("availability", "")).lower()
                    if "instock" in avail_raw or "instoreonly" in avail_raw:
                        avail = True
                    elif "outofstock" in avail_raw or "soldout" in avail_raw:
                        avail = False
                    elif "preorder" in avail_raw:
                        avail = True
                    else:
                        avail = None
                    found.append((cents, avail))
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    for m in re.finditer(
            r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>',
            body, re.S):
        try:
            walk(json.loads(m.group(1).strip()))
        except ValueError:
            continue
    return found


def read_page_fallback(url):
    """Fallback: read the page itself and pull the first JSON-LD offer."""
    status, body = fetch(url)
    offers = extract_jsonld_offers(body)
    if offers:
        cents, avail = offers[0]
        return [_variant("Default Title", cents, None, avail)], \
            "page JSON-LD offer"
    m = re.search(r'og:price:amount" content="([\d,]+(?:\.\d+)?)"', body)
    if m:
        return [_variant("Default Title",
                         round(float(m.group(1).replace(",", "")) * 100),
                         None, None)], "page og:price meta"
    raise ValueError("no price found in page fallback")


def read_shopify(url):
    errors = []
    for reader in (read_shopify_js, read_shopify_json):
        try:
            return reader(url)
        except Exception as e:
            errors.append(str(e))
    variants, how = read_page_fallback(url)
    return variants, f"page fallback ({how}); .js and .json failed: {errors}"


# ------------------------------------------------------------- Structured

def read_structured(url):
    """Second pass reader: the page's structured data (JSON-LD offers)
    where present, falling back to the page's stated price (og:price)."""
    status, body = fetch(url)
    if "Just a moment" in body[:2000] and "challenges.cloudflare.com" in body:
        raise ValueError(
            "Cloudflare bot challenge page served instead of the product "
            "page (plain automated read blocked)")
    offers = extract_jsonld_offers(body)
    if offers:
        variants = [_variant("Default Title", cents, None, avail)
                    for cents, avail in offers]
        return variants, "page JSON-LD offer"
    m = re.search(r'og:price:amount" content="([\d,]+(?:\.\d+)?)"', body)
    if m:
        return [_variant("Default Title",
                         round(float(m.group(1).replace(",", "")) * 100),
                         None, None)], \
            "page og:price meta (no structured offer on the page)"
    raise ValueError("no structured offer and no stated price found on "
                     "the page")


# ---------------------------------------------------------------- Peloton

def read_peloton(url, slug):
    """Peloton states no structured offer. Read the product's own page:
    the regular price from its embedded Canadian price table and the
    current selling price from its financing legal text."""
    if slug not in PELOTON_MAP:
        raise ValueError(f"no Peloton price mapping for slug '{slug}'")
    key, legal_name = PELOTON_MAP[slug]
    status, body = fetch(url)
    list_cents = None
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',
                  body, re.S)
    if m:
        try:
            nd = json.loads(m.group(1))
            prices = (nd.get("props", {}).get("pageProps", {})
                      .get("fallback", {}).get("prices", {})
                      .get("en-CA", {}))
            entry = prices.get(key) or {}
            if entry.get("price"):
                list_cents = int(entry["price"])
        except (ValueError, AttributeError):
            list_cents = None
    sale_cents = None
    pat = (r"Get the " + re.escape(legal_name) +
           r" for as low as \$[\d.]+/mo over 36 months at 0% APR\. "
           r"Based on a price of \$([\d,]+)")
    mm = re.search(pat, body)
    if mm:
        sale_cents = round(float(mm.group(1).replace(",", "")) * 100)
    if sale_cents is None and list_cents is None:
        raise ValueError("no Peloton price found: neither the embedded "
                         "price table nor the financing legal text "
                         "carried this product")
    selling = sale_cents if sale_cents is not None else list_cents
    compare = list_cents if (list_cents is not None
                             and list_cents != selling) else None
    source = ("Peloton page embedded Canadian price table"
              + (" and financing legal text" if sale_cents is not None
                 else ""))
    return [_variant("Default Title", selling, compare, None)], source


def read_product(p):
    retailer = p["retailer"]
    url = p["retailer_url"]
    if retailer in SHOPIFY_STORES:
        return read_shopify(url)
    if retailer == PELOTON_STORE:
        return read_peloton(url, p["slug"])
    return read_structured(url)


# ------------------------------------------------------- Live reference

def derive_stock_state(note):
    """The published catalogue embeds the stock note but not the app's
    derived stock state. Derive the state the way the app's own
    recorded pairs read: a blank note is not stated, an unclear note is
    unclear, the exact Out of stock note is out of stock, a note that
    opens with In stock is in stock, and anything else is as stated.
    Variant dependent notes (a headline size sold out inside a longer
    note) cannot be derived from the note alone; they read as their
    opening words, which is named here rather than hidden."""
    n = (note or "").strip()
    if not n:
        return "not_stated"
    if n.startswith("Stock unclear"):
        return "unclear"
    if n == "Out of stock":
        return "out_of_stock"
    if n.startswith("In stock"):
        return "in_stock"
    return "as_stated"


def load_live_reference():
    """Compare mode reference: fetch the published catalogue and parse
    the product data embedded in its page (var PRODUCTS = [...]) into
    the same record shape the local data file carries. The embedded
    data holds no headline variant markers, so variant selection in
    compare mode runs on the missing marker rules."""
    status, body = fetch(LIVE_URL, timeout=60)
    marker = "var PRODUCTS = "
    i = body.find(marker)
    if i < 0:
        raise ValueError("the live page does not embed a PRODUCTS "
                         "array; the published catalogue's shape has "
                         "changed")
    arr, _end = json.JSONDecoder().raw_decode(
        body[i + len(marker):].lstrip())
    out = []
    for lp in arr:
        variants = [{
            "label": v.get("label", ""),
            "price_cents": v.get("price"),
            "is_entry_variant": False,
            "is_headline_price_variant": False,
        } for v in lp.get("variants") or []]
        out.append({
            "slug": lp["slug"],
            "name": lp["name"],
            "retailer": lp["retailer"],
            "retailer_url": lp["url"],
            "visibility": "public",
            "variants": variants,
            "price_record": {
                "current_price_cents": lp.get("price"),
                "regular_price_cents": lp.get("regular"),
                "stock_note": lp.get("stock") or "",
                "stock_state": derive_stock_state(lp.get("stock")),
                "last_checked_date": lp.get("checked"),
                "last_successful_check_date": lp.get("checked"),
                "price_history": lp.get("checks") or [],
            },
        })
    return {"products": out}


def headline_label(p):
    for v in p.get("variants") or []:
        if v.get("is_headline_price_variant"):
            return v.get("label")
    return None


def find_anchor(page_variants, recorded_variants):
    """When the headline variant is not sold on the recorded page (the
    standing case: a per weight listing whose headline price was computed
    from a recorded rate), fall back to a recorded anchor variant whose
    price the page's single variant matches."""
    if len(page_variants) != 1:
        return None
    only = page_variants[0]
    for rv in recorded_variants or []:
        if rv.get("price_cents") == only["price_cents"]:
            return rv, only
    return None


CONCRETE_STOCK = {"in_stock", "out_of_stock"}


def check_product(p):
    rec = p["price_record"]
    recorded = rec.get("current_price_cents")
    recorded_reg = rec.get("regular_price_cents")
    recorded_stock = rec.get("stock_state")
    row = {
        "retailer": p["retailer"],
        "name": p["name"],
        "slug": p["slug"],
        "recorded": recorded,
        "recorded_reg": recorded_reg,
        "recorded_stock": recorded_stock,
        "read": None,
        "read_reg": None,
        "read_stock": None,
        "result": "",
        "reason": "",
        "stock_change": False,
        "marker_gap": False,
    }
    try:
        variants, source = read_product(p)
        variant, how, missing_marker = select_variant(
            variants, p.get("variants"), recorded)
        if missing_marker and len(variants) > 1:
            row["marker_gap"] = True
        if variant is None and not missing_marker and recorded is not None:
            for sv in variants:
                if sv["price_cents"] == recorded:
                    variant = sv
                    how = ("the recorded headline price is among the "
                           "prices the page's structured data offers; "
                           "the structured data names no variant labels")
                    break
        if variant is None and not missing_marker:
            if len(variants) == 1 and recorded is not None \
                    and variants[0]["price_cents"] == recorded:
                variant = variants[0]
                how = ("the page states a single price equal to the "
                       "recorded headline price; the structured data "
                       "names no variant label")
            else:
                anchor = find_anchor(variants, p.get("variants"))
                if anchor is None:
                    row["result"] = "READ FAILURE"
                    row["reason"] = how
                    if len(variants) > 1:
                        offered = ", ".join(
                            money(v["price_cents"]) for v in variants)
                        row["reason"] += (
                            f"; the page's structured data offers "
                            f"{len(variants)} unlabeled prices ({offered}), "
                            f"none equal to the recorded headline "
                            f"{money(recorded)} or a recorded variant price")
                    return finish_row(p, row)
                rec_anchor, variant = anchor
                read = variant["price_cents"]
                row.update(
                    read=read, read_reg=variant["compare_cents"],
                    read_stock=None if variant["available"] is None else
                    ("in_stock" if variant["available"] else "out_of_stock"))
                row["result"] = "DIFFERENCE"
                row["reason"] = (
                    f"the recorded headline variant "
                    f"'{headline_label(p)}' is not sold on the recorded "
                    f"page; the page sells a single variant read at "
                    f"{money(read)}, which matches the recorded anchor "
                    f"variant '{rec_anchor.get('label')}' at "
                    f"{money(rec_anchor.get('price_cents'))}; the headline "
                    f"price is a computed entry price, not a read price")
                return finish_row(p, row)
        if variant is None:
            # No headline marker on the record and no page variant
            # carries the recorded price: name the gap and attribute
            # no read to the configuration the record tracks.
            row["result"] = "HELD READ"
            offered = ", ".join(
                f"{v['title']} at {money(v['price_cents'])}"
                for v in variants)
            n_rec = len(p.get("variants") or [])
            if n_rec:
                rec_desc = (f"the record carries {n_rec} recorded "
                            f"variants, none of them marked as the "
                            f"headline variant")
            else:
                rec_desc = ("the record carries no recorded variants "
                            "and no headline variant marker")
            row["reason"] = (
                f"read via {source}; record is missing its headline "
                f"variant marker: {rec_desc}; the page sells "
                f"{len(variants)} variants ({offered}); none is priced "
                f"at the recorded {money(recorded)}, so no read can be "
                f"attributed to the configuration the record tracks; "
                f"reported, not treated as a price")
            return finish_row(p, row)
        read = variant["price_cents"]
        read_reg = variant["compare_cents"]
        avail = variant["available"]
        read_stock = None if avail is None else (
            "in_stock" if avail else "out_of_stock")
        row.update(read=read, read_reg=read_reg, read_stock=read_stock)
        if missing_marker and len(variants) == 1 \
                and recorded is not None and read != recorded:
            # A markerless record (the published catalogue's embedded
            # data carries no headline markers) whose recorded page
            # sells one variant priced like a recorded non headline
            # variant: the standing computed entry price case.
            anchor = find_anchor(variants, p.get("variants"))
            if anchor is not None:
                rec_anchor, _only = anchor
                row["read_stock"] = None
                row["result"] = "DIFFERENCE"
                row["reason"] = (
                    f"read via {source}; the record carries no "
                    f"headline variant marker; the recorded page sells "
                    f"a single variant read at {money(read)}, which "
                    f"matches the recorded variant "
                    f"'{rec_anchor.get('label')}' at "
                    f"{money(rec_anchor.get('price_cents'))}; the "
                    f"headline price is a computed entry price, not a "
                    f"read price")
                return finish_row(p, row)
        notes = [f"read via {source}; {how}"]
        if recorded is None:
            row["result"] = "DIFFERENCE"
            notes.append("no recorded price to compare")
        elif read == recorded:
            row["result"] = "MATCH"
        else:
            diff = (read - recorded) / recorded
            if abs(diff) >= HELD_THRESHOLD:
                row["result"] = "HELD READ"
                notes.append(
                    f"read is {abs(diff) * 100:.1f} percent away from the "
                    f"recorded price, at or over the 40 percent hold "
                    f"line; reported, not treated as a price")
            else:
                row["result"] = "DIFFERENCE"
                direction = "drop" if read < recorded else "rise"
                notes.append(
                    f"price {direction} of {money(abs(read - recorded))} "
                    f"({abs(diff) * 100:.1f} percent) since the last "
                    f"recorded check")
        if read_reg != recorded_reg:
            notes.append(
                f"compare at price differs: recorded "
                f"{money(recorded_reg)}, read {money(read_reg)}")
        if read_stock is not None and recorded_stock in CONCRETE_STOCK \
                and read_stock != recorded_stock:
            row["stock_change"] = True
            notes.append(
                f"stock change: recorded {recorded_stock}, page now "
                f"states {read_stock}")
        row["reason"] = "; ".join(notes)
    except urllib.error.HTTPError as e:
        row["result"] = "READ FAILURE"
        row["reason"] = f"HTTP {e.code} from the retailer's site"
    except Exception as e:
        row["result"] = "READ FAILURE"
        row["reason"] = f"{type(e).__name__}: {e}"
    return finish_row(p, row)


def finish_row(p, row):
    """Rogue failures are expected failures per spec section 7."""
    if p["retailer"] == ROGUE_STORE and row["result"] == "READ FAILURE":
        row["result"] = "EXPECTED FAILURE (Rogue)"
    return row


# ------------------------------------------------------------------ Gates

def evaluate_gates(data, processed_slugs, live=False):
    """Spec section 7 gates, observe only: evaluated and reported,
    blocking nothing. Returns a list of gate dicts. With live=True the
    reference under test is the published catalogue, not the file."""
    gates = []
    products = data["products"]
    public = [p for p in products if p.get("visibility") == "public"]

    gates.append({
        "name": "Gate 1: the data file parses" if not live
                else "Gate 1: the live reference record parses",
        "passed": True,
        "detail": f"data/products.json parsed cleanly; "
                  f"{len(products)} records loaded." if not live else
                  f"the published catalogue at {LIVE_URL} parsed "
                  f"cleanly; {len(products)} records loaded.",
        "offenders": [],
    })

    unprocessed = [p for p in public if p["slug"] not in processed_slugs]
    gates.append({
        "name": "Gate 2: the public product count in the data file "
                "matches the count the run processed" if not live else
                "Gate 2: the public product count in the live "
                "reference matches the count the run processed",
        "passed": not unprocessed,
        "detail": f"data file holds {len(public)} public products; "
                  f"this run processed {len(processed_slugs)} of them; "
                  f"{len(unprocessed)} not processed." if not live else
                  f"live reference holds {len(public)} public "
                  f"products; this run processed "
                  f"{len(processed_slugs)} of them; "
                  f"{len(unprocessed)} not processed.",
        "offenders": unprocessed,
    })

    offenders = []
    for p in public:
        rec = p.get("price_record") or {}
        has_price = rec.get("current_price_cents") is not None
        has_oos = rec.get("stock_state") == "out_of_stock"
        dated = bool(rec.get("last_checked_date")
                     or rec.get("last_successful_check_date"))
        if not ((has_price or has_oos) and dated):
            offenders.append(p)
    gates.append({
        "name": "Gate 3: every public product carries a recorded price "
                "or an explicit out of stock state from a dated check",
        "passed": not offenders,
        "detail": f"{len(public) - len(offenders)} of {len(public)} "
                  f"public products satisfy the gate.",
        "offenders": offenders,
    })
    return gates


def compose_alerts(gates, store_stats, stamp):
    """Dry run alert composer: returns the exact alert email text when
    any gate fails or a non Rogue store's failure rate exceeds half its
    products. Nothing is sent."""
    triggers = []
    for g in gates:
        if not g["passed"]:
            triggers.append(("gate", g))
    for retailer, st in sorted(store_stats.items()):
        if retailer == ROGUE_STORE:
            continue
        attempted = st["attempted"]
        failed = st["counts"].get("READ FAILURE", 0)
        if attempted and failed / attempted > 0.5:
            triggers.append(("store", (retailer, attempted, failed,
                                       st["failures"])))
    if not triggers:
        return None
    lines = [
        f"To: {ALERT_TO}",
        f"Subject: Canada Home Gym Price Watch checker alert, "
        f"{stamp.strftime('%Y-%m-%d')}: validation gate or store read "
        f"failure",
        "",
        "The standalone price checker run finished with problems that "
        "need attention. In live operation this run would publish "
        "nothing and the last good catalogue would stay live.",
        "",
    ]
    for kind, item in triggers:
        if kind == "gate":
            g = item
            lines.append(f"FAILED GATE: {g['name']}")
            lines.append(g["detail"])
            if g["offenders"]:
                lines.append("Products involved:")
                for p in g["offenders"]:
                    lines.append(f"- {p['name']} ({p['retailer']})")
            lines.append("")
        else:
            retailer, attempted, failed, failures = item
            lines.append(
                f"STORE READ FAILURES: {retailer}: {failed} of "
                f"{attempted} products failed to read, over half the "
                f"store's products in this run.")
            lines.append("Products involved:")
            for r in failures:
                lines.append(f"- {r['name']}: {r['reason']}")
            lines.append("")
    lines.append("This alert was composed by the checker in dry run "
                 "form. No email was sent.")
    return "\n".join(lines)


# ------------------------------------------------------------------- Main

def store_stats(rows):
    stats = {}
    for r in rows:
        st = stats.setdefault(r["retailer"], {
            "attempted": 0, "counts": {}, "failures": [],
            "stock_changes": [], "non_match": []})
        st["attempted"] += 1
        st["counts"][r["result"]] = st["counts"].get(r["result"], 0) + 1
        if r["result"] in ("READ FAILURE", "EXPECTED FAILURE (Rogue)"):
            st["failures"].append(r)
        if r["stock_change"]:
            st["stock_changes"].append(r)
        if r["result"] != "MATCH" or r["stock_change"]:
            st["non_match"].append(r)
    return stats


def load_subset_slugs(path):
    if not path.exists():
        print(f"note: subset file {path} not present; selecting nothing")
        return []
    return json.loads(path.read_text())["slugs"]


def main():
    args = sys.argv[1:]
    compare_live = False
    if "--reference" in args:
        idx = args.index("--reference")
        if idx + 1 < len(args) and args[idx + 1] == "live":
            compare_live = True
    if compare_live:
        try:
            data = load_live_reference()
        except Exception as e:
            print(f"compare mode stopped: the live reference could "
                  f"not be loaded: {type(e).__name__}: {e}")
            sys.exit(1)
    else:
        raw = DATA_FILE.read_text()
        data = json.loads(raw)
    products = data["products"]
    by_slug = {p["slug"]: p for p in products}
    if "--all-stores" in args:
        selected = [p for p in products
                    if p["retailer"] in READER_STORES
                    and p.get("visibility") == "public"]
        mode = (f"full run, all stores with a reader "
                f"({len(SHOPIFY_STORES)} Shopify, "
                f"{len(STRUCTURED_STORES)} structured, Peloton, Rogue)")
        tag = "full"
    elif "--all" in args:
        selected = [p for p in products if p["retailer"] in SHOPIFY_STORES
                    and p.get("visibility") == "public"]
        mode = "full run, Shopify stores"
        tag = "full"
    elif "--subset2" in args:
        wanted = load_subset_slugs(SUBSET2_FILE)
        selected = [by_slug[s] for s in wanted if s in by_slug]
        mode = "stage B subset run, 3 per second pass store plus Rogue"
        tag = "subset2"
    elif "--slugs" in args:
        wanted = args[args.index("--slugs") + 1].split(",")
        selected = [by_slug[s] for s in wanted if s in by_slug]
        mode = "named slugs"
        tag = "slugs"
    else:
        wanted = load_subset_slugs(SUBSET_FILE)
        selected = [by_slug[s] for s in wanted if s in by_slug]
        mode = "subset run, 3 per Shopify store"
        tag = "subset"
    if compare_live:
        mode += ("; COMPARE MODE: the reference record is the live "
                 "published catalogue at " + LIVE_URL + ", not the "
                 "local data file")
        tag = "compare-" + tag

    stamp = datetime.now(timezone.utc)
    rows = []
    for p in selected:
        rows.append(check_product(p))
        time.sleep(0.5)

    counts = {}
    for r in rows:
        counts[r["result"]] = counts.get(r["result"], 0) + 1
    stats = store_stats(rows)
    processed = {p["slug"] for p in selected
                 if p.get("visibility") == "public"}
    gates = evaluate_gates(data, processed, live=compare_live)
    alert_text = compose_alerts(gates, stats, stamp)

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    fname = f"run-{stamp.strftime('%Y-%m-%d-%H%M')}-{tag}.md"
    lines = [
        "# Checker run report",
        "",
        f"Run at (UTC): {stamp.isoformat()}",
        f"Mode: {mode}. OBSERVE ONLY: no prices changed, data file "
        f"untouched, nothing published, no email sent.",
        f"Products checked: {len(rows)}",
        "Summary: " + ", ".join(f"{k} {v}" for k, v in
                                sorted(counts.items())),
        "",
        "## Per store results",
        "",
    ]
    for retailer in READER_STORES:
        if retailer not in stats:
            continue
        st = stats[retailer]
        c = st["counts"]
        lines.append(f"### {retailer}")
        lines.append("")
        lines.append(
            f"Attempted {st['attempted']}; exact matches "
            f"{c.get('MATCH', 0)}; price differences "
            f"{c.get('DIFFERENCE', 0)}; held reads "
            f"{c.get('HELD READ', 0)}; stock changes "
            f"{len(st['stock_changes'])}; read failures "
            f"{c.get('READ FAILURE', 0)}"
            + (f"; expected failures "
               f"{c.get('EXPECTED FAILURE (Rogue)', 0)}"
               if retailer == ROGUE_STORE else "")
            + ".")
        if st["non_match"]:
            lines.append("")
            lines.append("| Product | Recorded | Read | Result | Reason |")
            lines.append("|---|---|---|---|---|")
            for r in st["non_match"]:
                lines.append(
                    f"| {r['name']} | {money(r['recorded'])} "
                    f"(reg {money(r['recorded_reg'])}, stock "
                    f"{r['recorded_stock']}) | {money(r['read'])} "
                    f"(reg {money(r['read_reg'])}, stock "
                    f"{r['read_stock']}) | {r['result']} | {r['reason']} |")
        lines.append("")
    marker_gaps = [r for r in rows if r.get("marker_gap")]
    if marker_gaps:
        lines += [
            "## Headline variant marker gaps",
            "",
            "These records carry no headline variant marker. The "
            "reader did not silently take the first variant of a multi "
            "variant page: it identified the tracked configuration by "
            "the recorded price where a variant carries it, and "
            "attributed no read where none does.",
            "",
            "| Product | Store | Result | How the read was handled |",
            "|---|---|---|---|",
        ]
        for r in marker_gaps:
            lines.append(
                f"| {r['name']} | {r['retailer']} | {r['result']} | "
                f"{r['reason']} |")
        lines.append("")
    lines += [
        "## Validation gates (observe only, blocking nothing)",
        "",
    ]
    for g in gates:
        lines.append(f"- {'PASS' if g['passed'] else 'FAIL'}: {g['name']}. "
                     f"{g['detail']}")
        if g["offenders"]:
            by_retailer = {}
            for p in g["offenders"]:
                by_retailer.setdefault(p["retailer"], []).append(p["name"])
            for retailer, names in sorted(by_retailer.items()):
                if len(g["offenders"]) <= 40:
                    lines.append(f"  - {retailer}: " + "; ".join(names))
                else:
                    lines.append(f"  - {retailer}: {len(names)} products")
    lines.append("")
    lines += ["## Dry run alert", ""]
    if alert_text:
        lines.append("An alert would be sent for this run. Its exact "
                     "text follows. It was NOT sent.")
        lines.append("")
        lines.append("```")
        lines.append(alert_text)
        lines.append("```")
    else:
        lines.append("No alert would be sent for this run: every gate "
                     "passed and no store's read failure rate exceeded "
                     "half its products.")
    lines.append("")
    report_path = REPORTS_DIR / fname
    report_path.write_text("\n".join(lines))
    print(f"checked {len(rows)}: " +
          ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    print(f"report: {report_path}")
    for g in gates:
        print(f"gate: {'PASS' if g['passed'] else 'FAIL'}: {g['name']}")
    print("alert: " + ("composed (dry run, not sent)" if alert_text
                       else "none"))
    for r in rows:
        if r["result"] != "MATCH":
            print(f"  {r['result']}: {r['retailer']} / {r['name']}: "
                  f"{r['reason']}")


if __name__ == "__main__":
    main()

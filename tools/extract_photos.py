#!/usr/bin/env python3
"""Extract product photo data-URIs from index.html as optimized WebP files.

Requires Pillow: python3 -m pip install Pillow
"""

import base64
import binascii
import io
import json
import re
import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError as exc:
    raise SystemExit(
        "Pillow is required; install it with: python3 -m pip install Pillow"
    ) from exc


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "index.html"
OUTPUT = ROOT / "index-new.html"
PHOTOS = ROOT / "assets" / "photos"
PRODUCTS_ASSIGNMENT = re.compile(r"\bvar\s+PRODUCTS\s*=\s*")
SLUG_PATTERN = re.compile(r"[a-z0-9][a-z0-9-]*\Z")
DATA_URI_PATTERN = re.compile(r"data:image/[a-z0-9.+-]+;base64\Z", re.IGNORECASE)


def load_products(source: str) -> tuple[list[dict], int, int]:
    match = PRODUCTS_ASSIGNMENT.search(source)
    if not match:
        raise ValueError("Could not find the PRODUCTS assignment in index.html")

    products, end = json.JSONDecoder().raw_decode(source, match.end())
    if not isinstance(products, list):
        raise ValueError("The PRODUCTS assignment is not a JSON array")
    return products, match.end(), end


def webp_bytes(data: bytes) -> bytes:
    with Image.open(io.BytesIO(data)) as opened:
        image = ImageOps.exif_transpose(opened)
        image.thumbnail((1000, 1000), Image.Resampling.LANCZOS)

        rgba = image.convert("RGBA")
        background = Image.new("RGBA", rgba.size, (255, 255, 255, 255))
        background.alpha_composite(rgba)

        output = io.BytesIO()
        background.convert("RGB").save(output, format="WEBP", quality=80)
        return output.getvalue()


def main() -> None:
    source_bytes = SOURCE.read_bytes()
    source = source_bytes.decode("utf-8")
    products, products_start, products_end = load_products(source)
    PHOTOS.mkdir(parents=True, exist_ok=True)

    converted = 0
    skipped_no_photo = 0
    skipped_non_data = 0
    source_image_bytes = 0
    webp_image_bytes = 0

    for product in products:
        photo = product.get("photo")
        if not photo:
            skipped_no_photo += 1
            continue
        if not isinstance(photo, str):
            raise ValueError(f"Invalid photo value for product {product.get('slug')!r}")
        if not photo.startswith("data:"):
            skipped_non_data += 1
            continue

        header, separator, payload = photo.partition(",")
        if not separator or not DATA_URI_PATTERN.fullmatch(header):
            raise ValueError(f"Invalid image data-URI for product {product.get('slug')!r}")

        slug = product.get("slug")
        if not isinstance(slug, str) or not SLUG_PATTERN.fullmatch(slug):
            raise ValueError(f"Invalid product slug for photo filename: {slug!r}")

        try:
            original = base64.b64decode(payload, validate=True)
        except (binascii.Error, ValueError) as exc:
            raise ValueError(f"Invalid base64 photo data for product {slug!r}") from exc

        try:
            converted_image = webp_bytes(original)
        except (OSError, ValueError, Image.DecompressionBombError) as exc:
            raise ValueError(f"Could not convert photo for product {slug!r}: {exc}") from exc

        destination = PHOTOS / f"{slug}.webp"
        destination.write_bytes(converted_image)
        product["photo"] = f"assets/photos/{slug}.webp"
        converted += 1
        source_image_bytes += len(original)
        webp_image_bytes += len(converted_image)

    replacement = json.dumps(products, ensure_ascii=False, separators=(",", ":"))
    output = source[:products_start] + replacement + source[products_end:]
    output_bytes = output.encode("utf-8")
    OUTPUT.write_bytes(output_bytes)

    print(f"Products: {len(products)}")
    print(f"Photos extracted: {converted}")
    print(f"Products without a photo: {skipped_no_photo}")
    print(f"Non-data photo values left unchanged: {skipped_non_data}")
    print(f"Original decoded image data: {source_image_bytes:,} bytes")
    print(f"WebP photo files: {webp_image_bytes:,} bytes")
    print(f"Photo size reduction: {source_image_bytes - webp_image_bytes:,} bytes")
    print(f"Source HTML: {len(source_bytes):,} bytes")
    print(f"Output HTML: {len(output_bytes):,} bytes ({OUTPUT.name})")
    print(f"Photo directory: {PHOTOS.relative_to(ROOT)}")


if __name__ == "__main__":
    try:
        main()
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"extract_photos: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

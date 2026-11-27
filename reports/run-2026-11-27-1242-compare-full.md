# Checker run report

Run at (UTC): 2026-11-27T12:42:49.460635+00:00
Mode: full run, all stores with a reader (10 Shopify, 6 structured, Peloton, Rogue); COMPARE MODE: the reference record is the live published catalogue at https://canadahomegym.ca/, not the local data file. OBSERVE ONLY: no prices changed, data file untouched, nothing published, no email sent.
Products checked: 2091
Summary: DIFFERENCE 15, HELD READ 31, MATCH 1488, READ FAILURE 557

## Per store results

### Bells of Steel

Attempted 119; exact matches 115; price differences 0; held reads 3; stock changes 3; read failures 1.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| Bells of Steel Dead Bounce All Black Bumper Plates, 260 lb Set | $447.99 (reg $559.99, stock out_of_stock) | not stated (reg not stated, stock None) | HELD READ | read via Shopify .js; record is missing its headline variant marker: the record carries no recorded variants and no headline variant marker; the page sells 5 variants (10 LB (Pair) at $45.99, 15 LB (Pair) at $63.99, 25 LB (Pair) at $87.99, 35 LB (Pair) at $119.99, 45 LB (Pair) at $149.99); none is priced at the recorded $447.99, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |
| Bells of Steel Manticore Four Post Converter Bench | $989.99 (reg $1,099.99, stock out_of_stock) | $989.99 (reg $1,099.99, stock in_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded out_of_stock, page now states in_stock |
| Bells of Steel Fitness Sandbags | $39.99 (reg $59.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 404 from the retailer's site |
| Ergo Rubber Hex Dumbbells | $944.99 (reg $1,080.99, stock in_stock) | not stated (reg not stated, stock None) | HELD READ | read via Shopify .js; record is missing its headline variant marker: the record carries 3 recorded variants, none of them marked as the headline variant; the page sells 23 variants (5 LB (Pair) at $22.99, 7.5 LB (Pair) at $35.99, 10 LB (Pair) at $41.99, 12.5 LB (Pair) at $50.99, 15 LB (Pair) at $61.99, 17.5 LB (Pair) at $63.99, 20 LB (Pair) at $81.99, 25 LB (Pair) at $107.99, 30 LB (Pair) at $127.99, 35 LB (Pair) at $149.99, 40 LB (Pair) at $163.99, 45 LB (Pair) at $154.99, 50 LB (Pair) at $205.99, 55 LB (Pair) at $225.99, 60 LB | 27 KG (Pair) at $247.99, 65 LB | 30 KG (Pair) at $267.99, 70 LB | 32 KG (Pair) at $287.99, 75 LB |  34 KG (Pair) at $309.99, 80 LB | 36 KG (Pair) at $209.99, 85 LB | 39 KG (Pair) at $349.99, 90 LB | 41 KG (Pair) at $369.99, 95 LB | 43 KG (Pair) at $391.99, 100 LB (Pair) at $411.99); none is priced at the recorded $944.99, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |
| Functional Trainer Cable Tower | $1,699.99 (reg $3,199.99, stock in_stock) | $1,699.99 (reg not stated, stock out_of_stock) | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,699.99 among the page's 5 variants; compare at price differs: recorded $3,199.99, read not stated; stock change: recorded in_stock, page now states out_of_stock |
| Arch Nemesis Tricep Bar | $89.99 (reg $99.99, stock in_stock) | $89.99 (reg $99.99, stock out_of_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded in_stock, page now states out_of_stock |
| Fitness Sandbag Sets | $188.99 (reg $269.99, stock in_stock) | not stated (reg not stated, stock None) | HELD READ | read via Shopify .js; record is missing its headline variant marker: the record carries 3 recorded variants, none of them marked as the headline variant; the page sells 8 variants (50 LB | 23 KG at $39.99, 100 LB | 45 KG at $44.99, 150 LB | 68 KG at $51.99, 200 LB | 91 KG at $58.99, 250 LB | 113 KG at $62.99, 300 LB | 136 KG at $69.99, 350 LB | 159 KG at $76.99, 400 LB | 181 KG at $83.99); none is priced at the recorded $188.99, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |

### Montreal Weights

Attempted 103; exact matches 88; price differences 0; held reads 0; stock changes 5; read failures 15.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| Pulley Attachment for Ascend Power Cage 3.0 | $199.00 (reg not stated, stock in_stock) | $199.00 (reg not stated, stock out_of_stock) | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $199.00 among the page's 2 variants; 2 variants carry that price; stock change: recorded in_stock, page now states out_of_stock |
| Pull-Up Bar | $29.99 (reg $49.99, stock out_of_stock) | $29.99 (reg $49.99, stock in_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded out_of_stock, page now states in_stock |
| Olympic Barbell | $179.00 (reg $249.00, stock in_stock) | $179.00 (reg $249.00, stock out_of_stock) | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $179.00 among the page's 2 variants; 2 variants carry that price; stock change: recorded in_stock, page now states out_of_stock |
| Bundle: Ascend 3-in-1 Adjustable Dumbbells (7 to 52.5 lb) & Bench | $549.00 (reg $850.00, stock in_stock) | $549.00 (reg $800.00, stock out_of_stock) | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $549.00 among the page's 3 variants; 2 variants carry that price; compare at price differs: recorded $850.00, read $800.00; stock change: recorded in_stock, page now states out_of_stock |
| Ascend R-200 Air Rower | $699.00 (reg $899.00, stock in_stock) | $699.00 (reg $899.00, stock out_of_stock) | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $699.00 among the page's 3 variants; 3 variants carry that price; stock change: recorded in_stock, page now states out_of_stock |
| Thinkrider X7 Smart Bike Trainer | $899.00 (reg $1,599.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Gym Floor Tiles | $49.00 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Ascend Shock Absorbing Tiles | $99.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Ascend Spin Bike Mat | $59.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Treadmill Mat | $79.99 (reg $59.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Ascend Elliptical Mat (L-100 & L-200) | $59.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Resistance Bands | $24.00 (reg $35.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Latex Resistance Band - 3pc/set | $19.99 (reg $39.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| High Speed Jump Rope | $19.99 (reg $29.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Foam Handle Jump Rope | $14.99 (reg $19.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Ab Roller Wheel | $24.95 (reg $29.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Handheld Percussion Massager | $124.99 (reg $199.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Hybrid Clip Pedals | $29.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| S2 Heart Rate Monitor Chest Strap | $49.99 (reg $59.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Treadmill Maintenance Kit | $29.99 (reg $39.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |

### Gorila Fitness

Attempted 62; exact matches 62; price differences 0; held reads 0; stock changes 1; read failures 0.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| Gorila Cast Iron Kettlebell | $57.00 (reg not stated, stock in_stock) | $57.00 (reg not stated, stock out_of_stock) | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $57.00 among the page's 11 variants; stock change: recorded in_stock, page now states out_of_stock |

### Northern Fitness

Attempted 109; exact matches 98; price differences 3; held reads 6; stock changes 0; read failures 2.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| REP Fitness Push Sled | $262.00 (reg not stated, stock in_stock) | $260.00 (reg not stated, stock in_stock) | DIFFERENCE | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; price drop of $2.00 (0.8 percent) since the last recorded check |
| 3-in-1 Soft Plyo Boxes | $144.00 (reg not stated, stock unclear) | not stated (reg not stated, stock None) | HELD READ | read via Shopify .js; record is missing its headline variant marker: the record carries 3 recorded variants, none of them marked as the headline variant; the page sells 3 variants (Small at $143.00, Medium at $169.00, Large at $293.00); none is priced at the recorded $144.00, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |
| REP Fitness Medicine Balls 2.0 | $59.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 404 from the retailer's site |
| COREFX Wall Balls | $82.47 (reg $92.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 404 from the retailer's site |
| Orion Nordic Bench Floor GHD | $269.00 (reg $599.00, stock in_stock) | $299.00 (reg $599.00, stock in_stock) | DIFFERENCE | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; price rise of $30.00 (11.2 percent) since the last recorded check |
| Orion Rubber Hex Dumbbell Set + 3 Tier Rack, 5-50lb | $679.00 (reg $1,299.00, stock in_stock) | $659.00 (reg $1,299.00, stock in_stock) | DIFFERENCE | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; price drop of $20.00 (2.9 percent) since the last recorded check |
| REP Fitness Urethane Dumbbell Sets | $2,090.00 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | HELD READ | read via Shopify .js; record is missing its headline variant marker: the record carries 4 recorded variants, none of them marked as the headline variant; the page sells 4 variants (5-50 LB Set at $2,081.00, 55-75 LB Set at $2,471.00, 80-100 LB Set at $3,251.00, 5-100 LB Set at $7,411.00); none is priced at the recorded $2,090.00, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |
| AD80 Adjustable Dumbbell Set (Snode) | $678.50 (reg $879.00, stock in_stock) | not stated (reg not stated, stock None) | HELD READ | read via Shopify .js; record is missing its headline variant marker: the record carries 2 recorded variants, none of them marked as the headline variant; the page sells 2 variants (AD80 Adjustable Dumbbells at $660.00, AD80 Adjustable Dumbbells + 8 Magnet Weight Plates at $759.00); none is priced at the recorded $678.50, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |
| AD80 Adjustable Dumbbell + Stand Bundle (Snode) | $889.00 (reg $1,199.00, stock in_stock) | not stated (reg not stated, stock None) | HELD READ | read via Shopify .js; record is missing its headline variant marker: the record carries 2 recorded variants, none of them marked as the headline variant; the page sells 2 variants (AD80 Adjustable Dumbbells at $809.00, AD80 Adjustable Dumbbells + 8 Magnet Weight Plates at $858.00); none is priced at the recorded $889.00, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |
| Hex Dumbbell Sets (REP Fitness) | $1,437.00 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | HELD READ | read via Shopify .js; record is missing its headline variant marker: the record carries 4 recorded variants, none of them marked as the headline variant; the page sells 4 variants (5-50 LB Set at $1,431.00, 55-75 LB Set at $1,691.00, 80-100 LB Set at $2,146.00, 5-100 LB Set at $4,811.00); none is priced at the recorded $1,437.00, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |
| QuickDraw Adjustable Dumbbells (REP Fitness) | $439.00 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | HELD READ | read via Shopify .js; record is missing its headline variant marker: the record carries 4 recorded variants, none of them marked as the headline variant; the page sells 4 variants (30 LB Pair at $437.00, 40 LB Pair at $541.00, 50 LB Pair at $645.00, 60 LB Pair at $749.00); none is priced at the recorded $439.00, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |

### Treadmill Factory

Attempted 241; exact matches 185; price differences 3; held reads 2; stock changes 0; read failures 51.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| Element Fitness Virgin Rubber Hex Dumbbells | $3.87 (reg not stated, stock in_stock) | $12.90 (reg $30.00, stock None) | DIFFERENCE | read via Shopify .js; the record carries no headline variant marker; the recorded page sells a single variant read at $12.90, which matches the recorded variant '10 lb' at $12.90; the headline price is a computed entry price, not a read price |
| Weider Cast Iron Hex Dumbbell | $17.50 (reg $35.00, stock as_stated) | $24.15 (reg not stated, stock in_stock) | DIFFERENCE | read via page fallback (page JSON-LD offer); .js and .json failed: ['HTTP Error 404: Not Found', 'Shopify JSON carried no variants']; the page sells a single variant; the record carries no headline variant marker; price rise of $6.65 (38.0 percent) since the last recorded check; compare at price differs: recorded $35.00, read not stated |
| Weider Urethane Dumbbell | $5.00 (reg $10.00, stock in_stock) | $24.15 (reg not stated, stock in_stock) | HELD READ | read via page fallback (page JSON-LD offer); .js and .json failed: ['HTTP Error 404: Not Found', 'Shopify JSON carried no variants']; the page sells a single variant; the record carries no headline variant marker; read is 383.0 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price; compare at price differs: recorded $10.00, read not stated |
| Treadmill Factory XM Cast Iron Kettlebell | $16.00 (reg not stated, stock in_stock) | $64.00 (reg not stated, stock in_stock) | HELD READ | read via page fallback (page JSON-LD offer); .js and .json failed: ['HTTP Error 404: Not Found', 'Shopify JSON carried no variants']; the page sells a single variant; the record carries no headline variant marker; read is 300.0 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price |
| IRONAX XC — VHT Vertical Hip Thrust | $799.00 (reg $1,099.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| IRONAX XC — HSLP Hack Squat / Leg Press | $1,699.00 (reg $2,099.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| IRONAX XLP Leg Press / Rubber Plate Combo | $1,599.00 (reg $2,499.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Body-Solid GSCR349 Commercial Seated Calf Raise | $649.88 (reg $1,161.25, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| IRONAX XC — LSC Leverage Squat / Calf | $1,299.00 (reg $1,799.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| XM FITNESS Commercial Hip Thrust Pro Glute Bench | $699.00 (reg $1,399.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| IRONAX XC — SHA Standing Hip Abductor | $999.00 (reg $1,499.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element Fitness Commercial Hip Thrust | $1,697.88 (reg $3,999.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element CARBON DUAL Leg Extension / Leg Curl Black (9019) | $2,299.00 (reg $3,999.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| IRONAX XC — SLE Seated Leg Extension | $799.00 (reg $1,299.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element Fitness Cobalt Dual Leg Ext & Curl | $2,999.00 (reg $4,299.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element CARBON DUAL Leg Press / Calf Raise Black (9010) | $2,199.00 (reg $3,299.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element IRON 7017 Seated Calf Raise | $899.00 (reg $1,199.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| IRONAX XC — PLC Prone Leg Curl | $899.00 (reg $1,399.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element CARBON DUAL Inner / Outer Thigh Black (9016) | $1,999.00 (reg $2,999.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Body-Solid GSCR349B Seated Calf Raise | $649.88 (reg $1,161.25, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| TuffStuff Evolution CLH-300 Horizontal Plate Loaded Leg Press / Hack Squat | $1,699.00 (reg $3,999.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element Fitness Chromium 604 Prone Leg Curl | $2,199.00 (reg $2,999.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Vision Fitness Glute Trainer PL78 | $2,699.00 (reg $3,999.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Vision Fitness Seated Calf Raise PL77 | $1,399.00 (reg $2,099.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element Fitness BLACK IRON Seated Calf Raise 7017 | $899.00 (reg $1,299.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element Fitness Cobalt Dual Inner / Outer Thigh Machine | $2,999.00 (reg $4,299.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element Fitness Cobalt Commercial Leg Press | $3,999.00 (reg $5,999.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element Fitness 9538 Hip Thrust MERCURY BLACK 235lbs | $2,999.00 (reg $4,999.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Vision Fitness Leg Extension / Leg Curl S711 | $3,999.00 (reg $5,999.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| IRONAX XC — VLP Vertical Leg Press | $999.00 (reg $1,799.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element 7034 Standing Squat IRON | $2,499.00 (reg $3,499.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Pro Club Line Leg Press SLP500G-2 | $3,799.00 (reg $4,748.75, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element Fitness 9506 Seated Leg Curl MERCURY BLACK | $3,799.00 (reg $4,999.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element Fitness BLACK IRON Hip Trainer 7038 | $2,699.00 (reg $3,599.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element MERCURY 9505 Leg Extension | $2,697.00 (reg $4,299.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Vision Fitness Keystone PL70 Leg Press | $3,999.00 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Vision Fitness Keystone PL71 Leg Extension | $2,499.00 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element Fitness Chromium 624 MULTI SQUAT | $4,499.00 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element Fitness BLACK IRON Standing Squat 7034 | $2,499.00 (reg $2,999.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element Fitness 9526 Glute IRON Silver Frame | $2,297.00 (reg $4,999.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element Fitness 7051 Assisted Nordic Ham IRON BLACK | $1,899.00 (reg $3,999.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element Fitness 9505 Leg Extension MERCURY BLACK 295lbs | $3,999.00 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element Fitness Chromium 625 Kneeling Glute Kickback | $3,999.00 (reg $4,999.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element CARBON DUAL Leg Press / Calf Raise (9010, second listing) | $2,199.00 (reg $3,299.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element Fitness BLACK IRON 45° Leg Press 7020 | $4,999.00 (reg $5,499.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element Fitness BLACK IRON Leg Extension 7025 | $1,799.00 (reg $2,799.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| ELEMENT IRON FLOOR GLUTE BLACK | $999.00 (reg $1,399.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element MERCURY 9509 Total Hip | $3,999.00 (reg $4,999.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element 9521 Prone Leg Curl MERCURY BLACK | $3,599.00 (reg $5,499.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| EL 7040 Lower Limb Standing Squat Iron | $1,699.00 (reg $2,699.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element MERCURY 9516 Calf Raise | $3,999.00 (reg $4,499.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Body Solid S2IOT-1 Series II Inner & Outer Thigh | $3,599.00 (reg $4,498.75, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element MERCURY 9506 Seated Leg Curl | $3,999.00 (reg $4,299.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element IRON 7026 Leg Curl | $2,199.00 (reg $2,999.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element IRON 7021 Hack Squat Plate Loaded | $3,699.00 (reg $5,199.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Mega Fitness Rubber Hex Dumbbell | $2.97 (reg not stated, stock in_stock) | $24.75 (reg not stated, stock None) | DIFFERENCE | read via Shopify .js; the record carries no headline variant marker; the recorded page sells a single variant read at $24.75, which matches the recorded variant '25 lb' at $24.75; the headline price is a computed entry price, not a read price |

### Force USA Canada

Attempted 25; exact matches 25; price differences 0; held reads 0; stock changes 0; read failures 0.

### Altas Strength

Attempted 43; exact matches 42; price differences 0; held reads 0; stock changes 0; read failures 1.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| AL-D01 Adjustable Dumbbell 70lb | $234.00 (reg $275.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 404 from the retailer's site |

### Lion Fitness

Attempted 213; exact matches 145; price differences 0; held reads 0; stock changes 3; read failures 68.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| 1 Inch Curl Bar | $29.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 404 from the retailer's site |
| 1" or 2" Weight Plate Rack (Olympic) | $119.99 (reg not stated, stock out_of_stock) | $119.99 (reg not stated, stock in_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded out_of_stock, page now states in_stock |
| Straight Bar 5 Feet (1 Inch) | $39.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 404 from the retailer's site |
| Straight Bar 6 Feet (1 Inch) | $49.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 404 from the retailer's site |
| Weight plate rack and Olympic bars | $139.99 (reg not stated, stock out_of_stock) | $139.99 (reg not stated, stock in_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded out_of_stock, page now states in_stock |
| 3D Smith 3-in-1 Phoenix Pro Training Cage | $6,999.99 (reg $9,999.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| J-Hook for Supreme Premium Cage | $99.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Phoenix Pro 3-in-1 Smith Training Cage | $5,499.99 (reg $7,499.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Squat Rack 3x3 with Safety Arms | $499.99 (reg $599.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Abducteur / Adducteur – Série Kobra | $1,749.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Aluminum drive handles for cable machines | $29.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Biceps Curl / Triceps Extension – Série Kobra | $999.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Cable Machine Pulley Lat Pull down | $299.99 (reg $399.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Chest Press / Shoulder Press – Série Kobra | $1,749.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Chest Press – Série Kobra | $1,499.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Circular Pulldown – Série Kobra | $1,499.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Curl biceps / Extension triceps – Série Kobra | $1,749.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Functional Trainer double poulie – Série Kobra | $2,499.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Incline Chest Press – Série Kobra | $1,249.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Lat Pulldown & Low Row – Série Kobra | $1,999.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Machine à Fentes Coulissantes – Série Kobra | $1,249.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Multistation 4 en 1 – Série Kobra | $5,499.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Multistation 4 en 1 – Série Kobra | $5,999.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Presse à Triceps – Série Kobra | $999.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Reverse Fly Assis – Série Kobra | $999.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Shoulder Press Assis – Série Kobra | $1,249.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Shoulder Press – Série Kobra | $1,499.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Smith Back Row – Série Kobra | $1,499.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Station Multifonction 5-en-1 Cable Crossover - Série Kobra | $6,999.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Station Multifonction 5-en-1 Cable Crossover - Série Kobra | $6,499.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Station multifonction 5-en-1 – Cable Crossover – Série Kobra | $6,999.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Station Multifonction 8-en-1 Cable Crossover - Série Kobra | $11,499.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| T-Bar Row avec Support Thoracique – Série Kobra | $999.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Élévation Latérale Assis/Debout – Série Kobra | $999.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Lion Fitness Air Bike | $849.99 (reg $999.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Lion Fitness Commercial Air Bike | $1,099.99 (reg $1,499.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Lion Fitness Spinning Bike | $749.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Matrix CXC Training Cycle | $2,499.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Stair Climber Lion Fitness | $3,499.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| 4x25' Rubber Mat Roll 8mm | $499.99 (reg $599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Carpet finishing moldings | $1.50 (reg $5.99, stock out_of_stock) | $1.50 (reg $5.99, stock in_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded out_of_stock, page now states in_stock |
| Pair of Phoenix Sandwich J-Cups | $199.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| 3-in-1 Foam Plyometric Box | $149.99 (reg $199.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Adjustable Dumbbell Rack (Black) | $149.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Adjustable training step – Non-slip platform | $79.99 (reg $99.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Ballon Bosu d'Équilibre Lion Fitness | $69.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Commercial Cable Handle | $24.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Commercial Triangle Handle | $29.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Lion Adjustable Dumbbell Rack | $224.99 (reg $199.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Lion Fitness Ankle Straps | $14.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Lion Fitness Wall Ball | $37.49 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Phoenix - 3-Tier Round Dumbbell Rack– 10 Pairs | $899.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Phoenix J-Cups Roller | $189.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Phoenix Thigh Support | $199.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Set of 6 Long Resistance Bands | $49.99 (reg $79.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Suspension Training Kit – Premium Version | $59.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Wall-mounted stand for 10 balloons / Slam balloons / Medicine balloons | $149.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| XL Heavy Duty 3 Tier Dumbbell Rack 5-75lb | $499.99 (reg $499.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Belt Squat – Série Kobra | $1,999.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Hip Thrust 3D – Série Kobra | $1,749.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Hip Thrust – Série Kobra | $1,249.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Leg Curl / Extension Phénix | $499.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Leg Extension / Leg Curl – Série Kobra | $1,749.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Phoenix Seating Module with Leg Support | $199.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Hexagonal Rubber Dumbbells (Sold individually and in pairs) | $12.50 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Set of 2 Adjustable Dumbbells (10 to 90lb) | $399.99 (reg $799.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| 5-75lb Hex Dumbbell Set with 3 Tier Rack | $1,567.99 (reg $1,999.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Set: 5-30lb Dumbbells with Rack | $301.89 (reg $377.49, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Sets: Rubber Hex Dumbbells 5 to 50lb and 5 to 75lb | $687.50 (reg $848.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Set: 5-25lb Dumbbells with Rack | $233.49 (reg $287.49, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Adjustable Kettlebell – 20lb & 40lb | $114.99 (reg $149.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |

### Matsuru

Attempted 16; exact matches 16; price differences 0; held reads 0; stock changes 1; read failures 0.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| Roll-Out Mat 6' x 18' | $1,199.00 (reg not stated, stock in_stock) | $1,199.00 (reg not stated, stock out_of_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded in_stock, page now states out_of_stock |

### Fitness Depot Plus

Attempted 750; exact matches 374; price differences 5; held reads 18; stock changes 28; read failures 353.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| PowerBlock Pro 100 EXP Stage 1 Base Kit, 5 to 40 lb | $650.00 (reg not stated, stock in_stock) | $325.00 (reg $650.00, stock in_stock) | HELD READ | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; read is 50.0 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price; compare at price differs: recorded not stated, read $650.00 |
| Inspire Fitness FT1 Functional Trainer Black | $2,500.00 (reg $2,745.60, stock in_stock) | $2,500.00 (reg $2,745.60, stock out_of_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded in_stock, page now states out_of_stock |
| Inspire Fitness FT2 Smith Functional, Black | $3,500.00 (reg $5,499.00, stock in_stock) | $3,500.00 (reg $5,499.00, stock out_of_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded in_stock, page now states out_of_stock |
| Inspire Fitness Smith Cage System | $4,545.60 (reg not stated, stock in_stock) | $4,545.60 (reg not stated, stock out_of_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded in_stock, page now states out_of_stock |
| Altas Strength AL-3073 | $2,150.00 (reg not stated, stock in_stock) | $2,150.00 (reg $2,150.00, stock out_of_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; compare at price differs: recorded not stated, read $2,150.00; stock change: recorded in_stock, page now states out_of_stock |
| ELEMENT FITNESS 5 - 50 URETHANE DUMBELL SET | $1,650.00 (reg $2,200.00, stock in_stock) | $1,650.00 (reg $2,200.00, stock out_of_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded in_stock, page now states out_of_stock |
| PowerBlock Pro 100 Exp, 5-100 lb Complete Set | $1,598.40 (reg not stated, stock in_stock) | $1,598.40 (reg not stated, stock out_of_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded in_stock, page now states out_of_stock |
| PowerBlock Sport EXP Stage I Kit, 5-50 lbs, PAIR | $537.70 (reg not stated, stock in_stock) | $537.70 (reg not stated, stock out_of_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded in_stock, page now states out_of_stock |
| PowerBlock Sport 3-24 lbs | $363.64 (reg not stated, stock in_stock) | $181.82 (reg $363.64, stock in_stock) | HELD READ | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; read is 50.0 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price; compare at price differs: recorded not stated, read $363.64 |
| Pull Down/Long Pull V1 selectorized machine | $2,199.00 (reg $4,500.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Seated Calf selectorized machine | $2,199.00 (reg $4,500.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Machine Pour Abdominaux ET Genoux Levés/Plongés | $2,500.00 (reg $3,599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Hip Thrust V1 | $899.00 (reg $3,399.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Hip Thrust V2 | $2,000.00 (reg $3,399.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Gripper | $2,500.00 (reg $1,750.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Calf Raise | $1,500.00 (reg $2,649.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness V – Squat à chargement de plaques | $2,500.00 (reg $3,599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Arm Press Back | $2,500.00 (reg $3,599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Vertical Leg Press | $2,500.00 (reg $3,999.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Incline Chest Fly Machine | $2,500.00 (reg $3,399.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Hip Belt Squat | $2,500.00 (reg $3,999.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Squat Lunge | $2,500.00 (reg $3,399.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Presse à déclinaison debout à charge de plaque | $2,500.00 (reg $3,599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Standing Incline Press | $2,500.00 (reg $3,599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Standing Press | $2,500.00 (reg $3,599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Free Weight Plate Loaded Squat Gym | $2,500.00 (reg $3,299.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Incline Lever Row | $2,500.00 (reg $2,799.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Hack Squat | $2,500.00 (reg $3,999.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Chargement de plaque X Pull Down | $2,500.00 (reg $3,599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Seated Leg Curl | $2,500.00 (reg $3,599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Decline Chest Press | $2,500.00 (reg $3,349.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Adductor | $2,500.00 (reg $3,599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Abductor Machine | $2,500.00 (reg $3,599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Standing Plate Loaded Shoulder Press | $2,500.00 (reg $3,599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Appareil d'entraînement musculaire pour mollets debout avec charge à plaques | $2,500.00 (reg $3,399.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Lateral Arm Lifting Trainer | $2,500.00 (reg $3,299.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Hip Builder | $2,500.00 (reg $3,999.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Tibia Dorsi | $2,500.00 (reg $2,549.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Iso-Lateral Leg Press | $2,500.00 (reg $3,999.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Abdominal Oblique Crunch Machine | $2,500.00 (reg $3,999.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded D.Y ROW | $2,500.00 (reg $3,599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Iso-Lateral Chest Press/Pulldown Plated Loaded | $2,500.00 (reg $3,999.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Presse à poitrine large avec charge libre | $2,500.00 (reg $3,599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Presse pectorale super inclinée à chargement par plaque | $2,500.00 (reg $3,599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Iso-Lateral Horizontal Bench Press | $2,500.00 (reg $3,299.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Leg Curl | $2,500.00 (reg $3,599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Row Plate Loaded | $2,500.00 (reg $3,599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Pulldown | $2,500.00 (reg $3,599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Bicep Curl | $2,500.00 (reg $3,599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Shoulder Press | $2,500.00 (reg $3,599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Plate Loaded Incline Chest Press | $2,500.00 (reg $3,599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Seated/Standing Shrug Plate loaded | $2,500.00 (reg $3,599.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Home Gym Equipment Rome Chair Al-3037 | $385.00 (reg $385.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| IRONAX Leg Extension / Leg Curl | $699.99 (reg $1,199.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Altas Strength Compact Leg Sled Machine AL-6007 | $999.00 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Addict fitness Addict fitness Sissy Squat | $1,500.00 (reg $2,299.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Accessoire d'aviron multi-style commercial Northern Lights | $79.88 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Accessoires de poignée YORK® Power Grip | $62.79 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | UnicodeEncodeError: 'ascii' codec can't encode character '\xae' in position 44: ordinal not in range(128) |
| Adjustable Dumbbell Rack | $104.99 (reg $119.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Al-3018 weight bench with leg curl, leg extension and preacher curl attachment | $520.00 (reg $799.00, stock out_of_stock) | $520.00 (reg $799.00, stock in_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded out_of_stock, page now states in_stock |
| Altas AL-4006 Adjustable Weight Bench | $279.00 (reg $279.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| ATOP Sports GPR02 Support d'alimentation | $719.86 (reg $1,000.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Attache cheville rembourrée en néoprène | $14.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Banc AB Evolve Econ Series, EC-288 | $300.00 (reg $1,000.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 404 from the retailer's site |
| Banc commercial Inspire Fitness FID5 | $563.64 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Banc FID IRONAX XFID1 avec (l'option extension  des jambes / flexion des jambes) | $499.99 (reg $599.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Banc militaire olympique Nautilus F3 - argent (Démonstrateur) | $400.00 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barbell Pad | $19.99 (reg $24.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barbell pad, Coussin d'haltères en mousse noire Northern Lights | $14.26 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barbell pad, Protecteur de cou pour haltères Manta Ray - Rouge doux | $14.88 (reg $24.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| BARRE DE CURL EZ RACKABLE XM GOLD | $229.00 (reg $329.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre de curling E-Z chromée Northern Lights Regular | $32.88 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre de curling Super EZ régulière | $41.88 (reg $49.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre de pompe cardio creuse Northern Lights de 59 po avec poignée en mousse | $34.99 (reg $49.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre de pression Northern Lights Commercial Tricep V | $38.99 (reg $49.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre de squat de sécurité olympique | $199.00 (reg $299.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre de traction à montage sur poutre à longueur réglable Northern Lights | $95.85 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre de triceps commerciale Northern Lights rotative | $55.88 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre de triceps de style olympique de 34 po | $99.00 (reg $145.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre de triceps rotative chromée Northern Lights | $41.88 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre Droite EL Plat 120lbs | $300.00 (reg $360.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre hexagonale olympique de 66 po | $269.00 (reg $349.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre latérale chromée de style professionnel de 34 po Northern Lights | $64.88 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre latérale Northern Lights, 48", creuse, peinte, simple, double | $39.99 (reg $49.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre olympique 24K XM Fitness Barre d'une capacité de 2000 lbs | $349.00 (reg $499.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre olympique E-Z curl Northern Lights | $62.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre olympique en aluminium – 72", 15LB | $127.27 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre olympique en chrome dur Northern Lights - 86", 28 mm, roulement - indice de 2 000 lb | $299.88 (reg $400.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre olympique Northern Lights - 79", 25 mm, 35LB - Bearing | $400.00 (reg $425.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre olympique Northern Lights - 86", 32 mm, 44LB - Roulement | $299.00 (reg $425.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre olympique Premium YORK® 5′ en oxyde noir |  500 lbs de capacité | $126.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | UnicodeEncodeError: 'ascii' codec can't encode character '\xae' in position 27: ordinal not in range(128) |
| Barre olympique Premium YORK® 7′ en oxyde noir – 30 mm | 1500 lbs de capacité | $261.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | UnicodeEncodeError: 'ascii' codec can't encode character '\xae' in position 27: ordinal not in range(128) |
| BARRE PULL DOWN PRISE NEUTRE – 34 » | $38.80 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre régulière 60" Northern Lights | $41.99 (reg $65.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre régulière 72" Northern Lights | $48.88 (reg $70.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre Suisse Droite en Acier Noir XM FITNESS | $129.00 (reg $249.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre Suisse Olympique Northern Lights - Noir | $199.88 (reg $265.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre Super Curl solide XM 2" | $79.99 (reg $99.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre YORK® 6′  en oxyde noir | 600 lbs de capacité | $143.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | UnicodeEncodeError: 'ascii' codec can't encode character '\xae' in position 27: ordinal not in range(128) |
| Boîte à craies XM Fitness | $269.00 (reg $299.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| bumper plate rack and Olympic weights XM FITNESS | $299.00 (reg $349.00, stock out_of_stock) | $299.00 (reg $349.00, stock in_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded out_of_stock, page now states in_stock |
| Bundle Musculaires Altas AL-6008 | $1,499.00 (reg $1,650.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Cage de musculation commerciale  AT-6013 | $756.88 (reg $1,200.00, stock out_of_stock) | $756.88 (reg $1,200.00, stock in_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded out_of_stock, page now states in_stock |
| Chariot de step aérobique Element Fitness | $249.00 (reg $299.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Collier fileté chromé régulier 1" | paire | $7.99 (reg $14.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Collier, Olympic, Smart Quick, paire | $18.18 (reg $29.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Colliers olympiques à verrouillage hexagonal - Paire | $18.99 (reg $29.99, stock out_of_stock) | $18.99 (reg $29.99, stock in_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded out_of_stock, page now states in_stock |
| Colliers à ressort standard Element Fitness 1" - Paire chromée | $9.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Competition Bar - Red Cerakote | $395.00 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Competition Bar V2 - Black Chrome | $395.00 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Competition Women Bar - Pink Cerakote | $350.00 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Compétition de plaques de pare-chocs olympiques Northern Lights | $41.32 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Corde à triceps Northern Lights | $24.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Coussin a genoux pour rack a squat et smith machine addict fitness | $140.00 (reg $262.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| CRAIE DE GYM LIQUIDE XM FITNESS | $19.99 (reg $34.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| CROCHETS POUR ACCESSOIRES MURAUX XM | $29.99 (reg $39.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Demi-rack commercial Inspire Fitness Ultimate, 83 po | $2,385.60 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Demi-rack commercial Inspire Fitness Ultimate, 97 po | $2,385.00 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Demi-rack IRONAX XHR | $659.00 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Dumbbell rack vertical pour 10 paires d’haltères | $199.99 (reg $225.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element Fitness Commercial Medicine Ball Rack 10 - MBA10 | $169.00 (reg $269.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element Fitness Medicine Ball Rack 15 - MBA15 | $299.00 (reg $349.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element Fitness Preacher Curl Bench | $494.01 (reg $799.00, stock out_of_stock) | $494.01 (reg $799.00, stock in_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded out_of_stock, page now states in_stock |
| Ensemble d'haltères curl en polyuréthane commercial Element Fitness | $2,199.00 (reg $2,999.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Ensemble de pompe cardio Element Fitness | $129.00 (reg $199.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Equipement de Gym à Domicile Rack à Squat Al-6008 | $970.91 (reg $1,499.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Evolve Olympic Triceps Bar | $79.99 (reg $160.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Glute noir Element | $999.00 (reg $1,399.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Haltère fileté chromé 60" Northern Lights (sans colliers) | $35.86 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Home Gym Equipment Fitness Bench AL-3021 | $200.00 (reg $200.00, stock out_of_stock) | $200.00 (reg $200.00, stock in_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded out_of_stock, page now states in_stock |
| Home Gym Equipment Fitness Bench AL-3026 | $199.00 (reg $199.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Inspire Fitness Extension de jambe/fixation de boucles pour banc FT2, noir | $212.99 (reg $299.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Inspire Fitness FT1 FID Bench | $427.99 (reg $799.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Inspire Fitness Power Rack FPC1, complete cage | $1,500.00 (reg $2,499.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Inspire Fitness SCS-WB2 Banc de musculation pour FT2 Noir | $623.99 (reg $800.00, stock out_of_stock) | $275.00 (reg $800.00, stock out_of_stock) | HELD READ | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; read is 55.9 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price |
| Inspire Fitness Squat Rack avec observateurs de sécurité | $999.99 (reg $1,499.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| IRONAX ADJUSTABLE NORDIC BENCH GHD | $499.00 (reg $899.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Ironax XFID bench | $350.99 (reg not stated, stock out_of_stock) | $350.99 (reg not stated, stock in_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded out_of_stock, page now states in_stock |
| IRONAX XPX POWER RACK | $699.99 (reg $1,299.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Landmine attachement XM FITNESS | $59.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Landmine Commercial with Bearing XM Fitness | $269.00 (reg $399.00, stock out_of_stock) | $269.00 (reg $399.00, stock in_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded out_of_stock, page now states in_stock |
| landmine commerciale légère XM Fitness | $139.00 (reg $169.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Landmine commerciale XM Fitness pour assiettes de 2" | $54.99 (reg $79.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Lat Pull Down Attachment | $300.00 (reg $350.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Light-Commercial Equipment Multi-Functional Bench AL-3039 | $469.00 (reg $499.99, stock out_of_stock) | $469.00 (reg $499.99, stock in_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded out_of_stock, page now states in_stock |
| Machine à mollets assise | Démonstrateur Longueuil | $381.82 (reg $449.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Northern Lights Barre latérale solide 48', Chrome | $50.99 (reg $59.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Northern Lights Commercial Lat Bar Style Pro | $62.99 (reg $79.99, stock out_of_stock) | $62.99 (reg $79.99, stock in_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded out_of_stock, page now states in_stock |
| Northern Lights CrossBox 18" Corner Kit B | $23.86 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Northern Lights CrossBox 43" X-Bar, MultiGrip, Noir | $95.86 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Northern Lights CrossBox Kit de rangement d'angle Petit modèle | $119.85 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Northern Lights CrossBox X-Bar 70" Triple Bar | $119.86 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Northern Lights Iron Factory Power Rack avec barre de traction multi-grip | $359.86 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Northern Lights Olympic Swiss Bar - Commercial | $299.99 (reg $399.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Pair of Olympic collars (as a pair) | $9.99 (reg $12.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Paire d'haltère en plastique fileté Regular 14" avec colliers | $9.99 (reg $14.99, stock in_stock) | $4.99 (reg $14.99, stock in_stock) | HELD READ | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; read is 50.1 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price |
| Pare-chocs olympique imparfait, 10 lb, coloré | $39.99 (reg $59.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Plaque de pare-chocs olympique Northern Lights 15 lb | $38.99 (reg $49.00, stock in_stock) | $15.00 (reg $49.00, stock in_stock) | HELD READ | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; read is 61.5 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price |
| Plaque de pare-chocs olympique Northern Lights 45 lb | $67.50 (reg $90.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Plaque de pare-chocs olympique Northern Lights de 35 lb | $49.99 (reg $79.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Plaque de pare-chocs olympique Northern Lights Fleck, 25 lb, vert | $58.99 (reg $98.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Plaque de pare-chocs olympique Northern Lights Fleck, 55 lb, rouge | $100.00 (reg $199.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Plaque de poids olympique avec revêtement en caoutchouc | choix de 5 a 45 LB | $3.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Plaque de poids olympique standard Northern Lights | choix de 2.5 a 45 LB | $3.12 (reg $4.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Plaque de pompe cardio Northern Lights, 10 lb | $23.96 (reg $29.00, stock in_stock) | $12.99 (reg $29.00, stock in_stock) | HELD READ | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; read is 45.8 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price |
| Plaque de pompe cardio Northern Lights, 2,5 lb | $5.99 (reg $8.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Plaque de pompe cardio Northern Lights, 5 lb | $11.98 (reg $14.99, stock in_stock) | $6.99 (reg $14.99, stock in_stock) | HELD READ | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; read is 41.7 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price |
| Poignée d'haltère chromée Northern Lights - Creuse | $38.18 (reg $49.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Poignée d'haltère olympique Northern Lights avec bagues en laiton | $76.99 (reg $99.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Poignée de barre olympique Northern Lights Landmine Double Grip | $23.86 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Poignée de câble chromée Northern Lights | $18.99 (reg $29.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Poignée de câble commerciale Northern Lights | $25.50 (reg $29.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| POIGNÉE VIKING SIMPLE 2" pour landmine XM FITNESS | $59.99 (reg $99.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Poignée étroite de landmine XM FITNESS | $24.99 (reg $79.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Poignées d'haltères filetées chromées Northern Lights 14" - Sans colliers | $13.99 (reg $19.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Porte-selle pour haltères à 3 niveaux Element Series | $999.00 (reg $1,199.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| POT À CRAIE - ABMAT | $29.99 (reg $49.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Prise d'haltères XM | $89.99 (reg $119.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Protège-nuque profilé pour haltères - Bleu doux | $24.99 (reg $31.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Rack pour poids olympique vertical XM Fitness | $218.99 (reg $299.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| RANGEMENT DE PLAQUE OLYMPIQUE MURALE VERTICALE XM | $169.00 (reg $249.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| RANGEMENT MURAL POUR DEUX BARRES OLYMPIQUE | $39.99 (reg $49.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| RANGEMENT À BARRE SIMPLE MURAL XM | $29.99 (reg $39.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Short Bar - Cerakote | $325.00 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Squat rack Altas AL-3028 | $1,599.00 (reg $1,599.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Strongman Log Bar | $389.00 (reg $499.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Support d'haltères commercial Element Fitness E-500-9830 | $699.00 (reg $1,299.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| SUPPORT D'HALTÈRES ELEMENT IRON 7016 | $999.00 (reg $1,399.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Support d'haltères en néoprène empilable vertical Element Fitness | $329.00 (reg $399.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| SUPPORT D'HALTÈRES PLAT XM À 3 NIVEAUX | $499.00 (reg $699.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Support d'haltères vertical pour haltère en vinyle/néoprène Element Fitness | $89.99 (reg $129.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| SUPPORT DE 10 BARRES BARBELL SÉRIE ELEMENT TITANIUM | $699.00 (reg $999.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Support de barbell Element Fitness, 10 paires | $569.00 (reg $899.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Support de barre olympique robuste 5 | $79.99 (reg $129.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Support de rangement Element 848ACR | $499.00 (reg $790.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| SUPPORT DE RANGEMENT MULTI-USAGES MURAL XM | $49.99 (reg $89.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Support de rangement multiple à 5 niveaux XM Fitness | $999.00 (reg $1,599.00, stock in_stock) | $788.99 (reg $1,599.00, stock in_stock) | DIFFERENCE | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; price drop of $210.01 (21.0 percent) since the last recorded check |
| Support de rangement mural pour bar olympique Northern Lights | $59.86 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Support de rangement pour balles/plaque olympique à 2 niveaux XM Fitness - 6 pieds | $449.00 (reg $849.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Support de sac lourd Northern Lights | $11.85 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Support de squat Northern Lights 92" Cross Box avec mentonnière | $585.00 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| SUPPORT MURAL POUR BALLES DE GYM ELEMENT FITNESS - GB2 | $49.00 (reg $99.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Support mural pour barre olympique Northern Lights, 1 barre | $23.85 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Support mural pour barre olympique Northern Lights, 2 barres | $35.86 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| SUPPORT MURAL POUR TAPIS | $24.99 (reg $29.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Support pour ballons de gymnastique Element Fitness - 122FBR | $129.00 (reg $149.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Support pour ballons médicinaux Northern Lights | $119.86 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Support pour rack domestique PowerBlock PowerBlock Pro100, 50 à 100 lb | $366.85 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Support à assiettes Northern Lights, assiette régulière | $83.86 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Support à rouleaux en mousse Element Fitness 4 emplacements - FRS | $199.00 (reg $249.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Supports de squat pour aurores boréales | $177.60 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| TP Pro Flat Bench | $291.99 (reg $349.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| TP Squat Rack with Pull-Up Bar and Safety Arm 2.0 | $750.00 (reg not stated, stock out_of_stock) | $750.00 (reg not stated, stock in_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded out_of_stock, page now states in_stock |
| TPWOD Support à Squat mural rétractable | $499.00 (reg $599.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Triangle de mentonnage commercial Northern Lights | $36.99 (reg $49.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Vertical storage support for bumper plate and Olympic weight | $129.00 (reg $199.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| WOD Bar - Chrome | $350.00 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| XM CAMBERED SWISS BAR | $249.00 (reg $349.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| XM FITNESS 3-Tier Dumbbell Storage Rack | $284.99 (reg $399.00, stock out_of_stock) | $284.99 (reg $399.00, stock in_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded out_of_stock, page now states in_stock |
| XM FITNESS FARMER'S WALK LOGS | $249.00 (reg $399.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| XM Fitness Rig Half Rack | $1,399.99 (reg $1,999.00, stock out_of_stock) | $1,399.99 (reg $1,999.00, stock in_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded out_of_stock, page now states in_stock |
| XM Fitness Step Through Olympic Hex / Trap Bar | $299.00 (reg $499.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| YORK® Olympic Hexagonal Dumbbell Bar – 20 kg | $209.09 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | UnicodeEncodeError: 'ascii' codec can't encode character '\xae' in position 58: ordinal not in range(128) |
| Northern Lights Ergonomic Molded Rubber Dumbbell, 3 lb | $2.99 (reg $4.99, stock in_stock) | $2.99 (reg $4.99, stock out_of_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded in_stock, page now states out_of_stock |
| PowerBlock Sport EXP Stage 2 Kit, 50-70 lbs | $237.60 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| PowerBlock Pro 100 Exp Stage 4 Kit, 80-100 lbs | $329.64 (reg $449.99, stock in_stock) | $164.82 (reg $329.64, stock in_stock) | HELD READ | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; read is 50.0 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price; compare at price differs: recorded $449.99, read $329.64 |
| PowerBlock Pro 100 Exp Stage 2 Kit, 40-60bs | $329.64 (reg $450.00, stock in_stock) | $164.82 (reg $329.64, stock in_stock) | HELD READ | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; read is 50.0 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price; compare at price differs: recorded $450.00, read $329.64 |
| Northern Lights Medium Dumbbell Rack | $199.99 (reg $350.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| York Chrome Dumbbell, 3 lb | $5.50 (reg $8.50, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Paire dumbbell ajustable Altas AL-D01 – 70 lb / 32 kg | $550.00 (reg not stated, stock in_stock) | $550.00 (reg not stated, stock out_of_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded in_stock, page now states out_of_stock |
| Hex Dumbbell PVC Coated | $9.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| PowerBlock Pro 100 Exp Stage 3 Kit, 60-80 lbs | $329.64 (reg $450.00, stock in_stock) | $329.64 (reg $450.00, stock out_of_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded in_stock, page now states out_of_stock |
| PowerBlock PowerBlock Pro100 Home Rack Support, 50-100 lb | $366.85 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| PowerMax Home PowerBlock Rack Bracket, 90# | $150.00 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| YORK® Kettlebells | $11.49 (reg $19.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | UnicodeEncodeError: 'ascii' codec can't encode character '\xae' in position 33: ordinal not in range(128) |
| PowerBlock Straight Bar, Pro 100 Urethane | $228.85 (reg not stated, stock in_stock) | $228.85 (reg not stated, stock out_of_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded in_stock, page now states out_of_stock |
| PowerBlock EZ Curl Bar, Pro 100 Urethane | $228.85 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| PowerBlock Urethane Straight Dumbbell | $238.80 (reg not stated, stock in_stock) | $119.40 (reg $238.80, stock in_stock) | HELD READ | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; read is 50.0 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price; compare at price differs: recorded not stated, read $238.80 |
| EZ-Curl Urethane PowerBlock Dumbbell | $238.80 (reg not stated, stock in_stock) | $238.80 (reg not stated, stock out_of_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded in_stock, page now states out_of_stock |
| A-Frame Dumbbell Rack | $200.00 (reg not stated, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Adjustable Kettlebell 12-32KG | $325.00 (reg not stated, stock in_stock) | $325.00 (reg not stated, stock out_of_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded in_stock, page now states out_of_stock |
| Cerakote Dumbbells - Builder - 5 - 75LB | $6,650.00 (reg not stated, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Cerakote Dumbbells - Builder - 5 - 50LB | $2,995.00 (reg not stated, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Cerakote Dumbbells - Builder - 5 - 150LB | $25,495.00 (reg not stated, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Cerakote Dumbbells - Builder - 105 - 150LB | $13,995.00 (reg not stated, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Commercial Dumbbells - 90LB Pair | $680.00 (reg not stated, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Commercial Dumbbells - 80-100LB Set | $3,250.00 (reg not stated, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Commercial Dumbbells - 75LB Pair | $575.00 (reg not stated, stock as_stated) | $150.00 (reg $575.00, stock out_of_stock) | HELD READ | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; read is 73.9 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price; compare at price differs: recorded not stated, read $575.00 |
| Commercial Dumbbells - 70LB Pair | $540.00 (reg not stated, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Commercial Dumbbells - 60LB Pair | $470.00 (reg not stated, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Commercial Dumbbells - 55LB Pair | $435.00 (reg not stated, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Commercial Dumbbells - 5-75LB Set | $4,595.00 (reg not stated, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Commercial Dumbbells - 5-100LB Set | $7,595.00 (reg not stated, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Commercial Dumbbells - 35LB Pair | $295.00 (reg not stated, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Commercial Dumbbells - 27.5LB Pair | $240.00 (reg not stated, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Commercial Dumbbells - 20LB Pair | $180.00 (reg not stated, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Commercial Dumbbells - 12.5LB Pair | $120.00 (reg not stated, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Commercial Dumbbells - 100LB Pair | $750.00 (reg not stated, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| XM FITNESS 2-Tier Kettlebell/Dumbbell Storage Rack - 6 Feet | $569.00 (reg $969.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| ABMAT - COUSSIN DE SQUAT SPLIT | $42.00 (reg $50.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Adaptateur de plaque olympique Northern Lights 13 pouces, 330 mm | $11.86 (reg not stated, stock in_stock) | $7.12 (reg $11.86, stock in_stock) | DIFFERENCE | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; price drop of $4.74 (40.0 percent) since the last recorded check; compare at price differs: recorded not stated, read $11.86 |
| Adaptateur de plaque olympique Northern Lights, 9", 230 mm | $9.46 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Ajusteur de boîte Plyo Northern Lights, Bois, 24" x 24" x 6" de haut | $74.88 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Anchor Gym – H1 Crochet Monté pour Mur/Plafond | $34.09 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Ancrage de porte, grand, entraîneur de suspension | $11.86 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Ancre de corde de combat Northern Lights CrossBox | $29.85 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Attache d'extrémité de boule de mine terrestre olympique Northern Lights | $63.64 (reg $79.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| BALLE DE RÉACTION | $4.99 (reg $9.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Ballon de Pilates lesté Northern Lights, 8 lb | $11.88 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| BARRE DE CHIN UP MURALE XM FITNESS *AJOUT D'EXTENSION UNIQUEMENT* | $109.00 (reg $149.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre de traction multi-grip montée au plafond XM Fitness | $124.99 (reg $99.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre de traction murale XM | $129.00 (reg $199.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre de traction Northern Lights - Barre courbée 1" x 48" avec poignées marteau | $59.86 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barre de traction pour cadre de porte de style Harbinger P90X | $29.99 (reg $39.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Barres push up Element Premium | $19.99 (reg $24.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Blaster à boucles pour bras Northern Lights | $48.99 (reg $75.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| BOSU Pro Entraîneur d'équilibre | $269.00 (reg $499.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Boîte Plyo en acier Rage 36" | $119.85 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Boîte Plyo Northern Lights, cadre en acier, dessus en caoutchouc, 18" | $179.85 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Bundle cardio tapis roulant Precor & Spinning HMC | $2,614.99 (reg $3,500.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Ceinture de trempage synthétique TKO/ceinture d'élévation des mollets | $35.86 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Chute de vitesse Northern Lights, 40'' X 40'' | $14.26 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| ClimbMill Matrix Lifestyle (Usagé) | $99,999.00 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Collier Spinlock olympique Northern Lights | $17.86 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Colliers olympiques Star Lock en aluminium, la paire | $35.00 (reg $38.99, stock in_stock) | $19.99 (reg $38.99, stock in_stock) | HELD READ | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; read is 42.9 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price |
| Corde d'escalade aurores boréales | $71.86 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Corde de combat couverte d'aurores boréales | $89.99 (reg $99.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Corde de combat ondulée en nylon noir/jaune de 50' | $99.00 (reg $189.97, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Corde de combat XM Fitness FLOW Rope | $79.99 (reg $129.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Coussin d'équilibre Northern Lights, 19'x15'x2-3/8', bleu | $38.99 (reg $49.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Dipping and Chinning Belt | $20.99 (reg $39.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Disques de glisse Element Fitness - 7" | $19.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Disques d’Equilibre Muscle Up | $14.99 (reg $19.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Drive Pad pour le Xtreme Monkey Red Sled | $129.00 (reg $249.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Element Fitness - Ballon médicinal | $29.99 (reg $47.99, stock in_stock) | $29.99 (reg $47.99, stock out_of_stock) | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $29.99 among the page's 11 variants; stock change: recorded in_stock, page now states out_of_stock |
| Elliptique HMC 633, argent | $860.20 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Ensemble Wall Ball 6 A 30LB | Commercial Ballon lesté (Copie) | $578.88 (reg $628.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| ENTRAÎNEUR D'AGILITÉ / HAIES HEXALES XM FITNESS | $39.99 (reg $79.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Fixation de câble Northern Lights 2BIG, barre droite de 20'' | $25.45 (reg $29.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Fixation de câble Northern Lights 2BIG, barre latérale de 48 po | $59.86 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Fixation de câble Northern Lights 2BIG, poignée double D | $47.86 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Fixation de dossier de roue Fran pour cycle à double action Northern Lights Air Force | $47.85 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Gilet lesté - Aérobic 12 livres | $29.88 (reg $35.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Gilet lesté XM FITNESS 25 lb, coupe en V | $99.00 (reg $129.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Haie réglable Northern Lights, 9" ou 12", vert | $11.86 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| HARNAIS DE LUMINOSITÉ/RÉSISTANCE POLYVALENT XM | $49.99 (reg $69.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Harnais de vitesse Northern Lights avec ceintures et ceintures d'épaule | $23.86 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Horizon 7.4 AT : Tapis de course durable et idéal pour le HIIT | $1,999.00 (reg $2,899.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| HyperWear Sandbell, Empty | $2.40 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Keiser M3+ (Reconstruit) | $1,500.00 (reg $3,600.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Keiser M3i | nouvelle version | Reconstruit | $1,795.00 (reg $1,900.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Landmine pour le sled XM red sled | $49.99 (reg $79.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Manchette de cheville Northern Lights | $12.99 (reg $14.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| MARTEAU (Masse) DE GYM | $39.99 (reg $59.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Masse en acier XM fitness | $24.99 (reg $39.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Matrix Connexus CXR50 Functional Training System | $1,999.00 (reg $2,999.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Mentonnière Northern Lights, échelle multiple, 43', noire | $71.86 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Mentonnière pour cadre de porte Northern Lights, multigrip, style P90X | $29.99 (reg $39.99, stock in_stock) | $14.99 (reg $39.99, stock in_stock) | HELD READ | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; read is 50.0 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price |
| Mini haie Northern Lights Performance, 12 po | $8.26 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| MUR D'ÉPURATION | $200.00 (reg $259.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Northern Lights ajouter du poids pour la pile de poids, 2,5 lb | $15.00 (reg $22.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Northern Lights IC-RD915W Vélo d'intérieur à traction arrière avec watts | $1,527.27 (reg $1,999.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Northern Lights Plyo Box Dessus en bois/caoutchouc, 24" x 24" x 6" de haut | $167.85 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Northern Lights The Step Junior Riser chacun noir | $9.99 (reg $19.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 404 from the retailer's site |
| Northern Lights The Step, 14" x 40", gris/noir | $89.09 (reg $99.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Octane LX8000 Commercial Latéral X, Con. standard | $4,011.20 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Octane Retro ZR8000 Zero Runner avec console standard | $1,500.00 (reg $4,500.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Planche oscillante en bois Element Fitness 16" - Commercial | $24.99 (reg $39.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Planche Wobble Ajustable Northern Lights - 41 cm | $14.99 (reg $19.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Planche à bascule en bois Element Fitness 20" | $39.99 (reg $49.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Pod d'équilibre Northern Lights 6,3" | $8.26 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Poids de cheville Northern Lights, 2 x 2,5 lb chacun, paire de 5 lb | $22.99 (reg $29.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Poids de cheville réglables - Paire de 20 lb - Element Fitness | $65.00 (reg $85.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Poids de poignet Element Fitness 2 lbs - Paire | $19.99 (reg $22.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Poignée de câble en nylon Northern Lights - Réglable | $9.99 (reg $14.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Poignée parlante numérique Better Body | $5.86 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Poignées York, paire, n° 6505 | $4.66 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Precor EFX® 447 - Série Precision™ | $7,346.20 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | UnicodeEncodeError: 'ascii' codec can't encode character '\xae' in position 27: ordinal not in range(128) |
| Quad d'agilité d'athlétisme 360 | $4.66 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Rameur commercial Octane RO | $1,941.20 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Rameur pneumatique DMaster R3000 | $800.00 (reg $999.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Rameur pneumatique Northern Lights ARC-102 | $975.20 (reg $1,500.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Roue abdominale double de luxe FIT505 | $29.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| RUBAN ADHÉSIF DOUBLE-FACE | $85.00 (reg $105.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Sac de haies d'athlétisme 360, 6 x 12 po | $5.86 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Sac de haies d'athlétisme 360, 6 x 6" | $4.66 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Sac de sable pour bûches Power, 20 lb | $60.00 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Sacs d'entraînement lesté avec sacs de sable haut de gamme | $79.99 (reg $149.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Sangle de berceau pour boule murale Northern Lights | $5.38 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Skierg Elite de Addict fitness | $850.00 (reg $1,399.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Slam ball choix entre 60lb et 150lb | $139.99 (reg not stated, stock in_stock) | $139.99 (reg not stated, stock out_of_stock) | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $139.99 among the page's 6 variants; stock change: recorded in_stock, page now states out_of_stock |
| Sled (traîneau à pousser) rouge | $329.00 (reg $499.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Stair Mill RS-800 Monte-Escalier Aérobic | Capicité de 330lbs RealLeaderUSA | $5,250.00 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Système de suspension Northern Lights vert avec poignées texturées | $48.99 (reg $55.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Série Precor EFX® 245 Energy™ | $4,185.60 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | UnicodeEncodeError: 'ascii' codec can't encode character '\xae' in position 33: ordinal not in range(128) |
| Série Precor EFX® 423 Precision™ | $5,385.60 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | UnicodeEncodeError: 'ascii' codec can't encode character '\xae' in position 33: ordinal not in range(128) |
| Tapis d'exercice XM Fitness Pro | $69.99 (reg $149.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Tapis de course Precor TRM 211 Energy™ Series | $1,985.00 (reg $2,500.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | UnicodeEncodeError: 'ascii' codec can't encode character '\u2122' in position 54: ordinal not in range(128) |
| Tapis de course Precor TRM 223 Energy™ Series | $3,200.00 (reg $5,000.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | UnicodeEncodeError: 'ascii' codec can't encode character '\u2122' in position 54: ordinal not in range(128) |
| Tapis de course Precor TRM 445 Precision™ Series | $5,385.60 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | UnicodeEncodeError: 'ascii' codec can't encode character '\u2122' in position 57: ordinal not in range(128) |
| Tapis de protection emboîtable en mousse Northern Lights - Ensemble de 6 Noir | $24.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Tapis en vinyle Northern Lights 2' x 4' x 2,5", noir | $47.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Tapis monstre Apachee Mills 3' x 4' x 1/4" | $35.86 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Tapis roulant Inspire Fitness T3 | $999.99 (reg $1,999.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Tendeur extensible pour mollets Step Fit | $19.99 (reg $49.99, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| TKO 20 lb. Gilet lesté réglable | $114.99 (reg $139.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| TKO Individuel 10 lb. Poids de cheville de rééducation | $71.86 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| TRAMPOLINE ELEMENT DELUXE PRO | $129.00 (reg $329.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| TRX Pro (P3) | $129.00 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Tuile casse tête Regupol 2'x2', bordure | $24.50 (reg $34.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Tuile casse tête Regupol 2'x2', coin | $24.50 (reg $39.99, stock in_stock) | $19.88 (reg $39.99, stock in_stock) | DIFFERENCE | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; price drop of $4.62 (18.9 percent) since the last recorded check |
| Tuile emboîtable Regupol 2'x2', centre | $24.50 (reg $35.00, stock in_stock) | $19.88 (reg $35.00, stock in_stock) | DIFFERENCE | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; price drop of $4.62 (18.9 percent) since the last recorded check |
| Vélo d'intérieur SF 300 | $225.00 (reg $350.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Vélo de groupe d'intérieur HMC 5008, argent | $729.99 (reg $1,000.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Vélo de groupe d'intérieur HMC 5008, rouge | $729.99 (reg $1,000.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Vélo de Spinning Résidentiel Jaune – Entraînement Intensif à Domicile ou en Studio | $375.00 (reg $450.00, stock in_stock) | $315.00 (reg $450.00, stock in_stock) | DIFFERENCE | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; price drop of $60.00 (16.0 percent) since the last recorded check |
| Vélo droit VISION Fitness U60 | $2,299.00 (reg $3,199.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Vélo elliptique domestique Precor EFX® 225 Energy™ Series, console R20-2 | $3,777.60 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | UnicodeEncodeError: 'ascii' codec can't encode character '\xae' in position 54: ordinal not in range(128) |
| Vélo elliptique domestique Precor EFX® 443 avec console R40 | $6,105.60 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | UnicodeEncodeError: 'ascii' codec can't encode character '\xae' in position 54: ordinal not in range(128) |
| Vélo elliptique Octane Q37, console standard | $625.60 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Vélo elliptique Octane Q47, console standard | $1,315.60 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Vélo pneumatique double action Pure Fitness 8534 | $250.00 (reg $350.00, stock in_stock) | $150.00 (reg $250.00, stock in_stock) | HELD READ | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; read is 40.0 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price; compare at price differs: recorded $350.00, read $250.00 |
| Vélo stationnaire commercial Vision U600E | $4,299.00 (reg $4,449.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Vélo vertical SportOp U60 | $900.00 (reg $1,200.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Vélo vertical Star Trac, série 4, avec écran tactile de 10 pouces | $2,985.60 (reg not stated, stock in_stock) | $1,499.99 (reg $3,500.00, stock in_stock) | HELD READ | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; read is 49.8 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price; compare at price differs: recorded not stated, read $3,500.00 |
| Vélo vertical Star Trac, série 4, avec écran tactile de 10 pouces | $2,985.60 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Wall Ball - 10LB | Commercial Ballon lesté | $80.00 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Wall Ball - 12LB | Commercial Ballon lesté | $54.00 (reg $85.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Wall Ball - 14LB | Commercial Ballon lesté | $57.00 (reg $90.00, stock out_of_stock) | $19.99 (reg $57.00, stock out_of_stock) | HELD READ | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; read is 64.9 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price; compare at price differs: recorded $90.00, read $57.00 |
| Wall Ball - 16LB | Commercial Ballon lesté | $60.00 (reg $95.00, stock out_of_stock) | $19.99 (reg $60.00, stock out_of_stock) | HELD READ | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; read is 66.7 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price; compare at price differs: recorded $95.00, read $60.00 |
| Wall Ball - 18LB | Commercial Ballon lesté | $64.00 (reg $100.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Wall Ball - 20LB | Commercial Ballon lesté | $68.00 (reg $110.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Wall Ball - 25LB | Commercial Ballon lesté | $73.00 (reg $120.00, stock out_of_stock) | $19.99 (reg $73.00, stock None) | HELD READ | read via Shopify .json; the page sells a single variant; the record carries no headline variant marker; read is 72.6 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price; compare at price differs: recorded $120.00, read $73.00 |
| Wall Ball - 30LB | Commercial Ballon lesté | $77.00 (reg $130.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Wall Ball - 6LB | Commercial Ballon lesté | $46.00 (reg $60.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Wall Ball - 8LB | Commercial Ballon lesté | $49.00 (reg $75.00, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| XM ANTI-SLIP PLYO BOX SOFT 20" 24" 30 | $269.00 (reg $439.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| XM FITNESS Air Skier | $1,299.00 (reg $2,299.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| XM FITNESS SLAM BALL | $110.99 (reg $160.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| XM PRO SLAM BALLS | $14.84 (reg $34.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| YORK® Boîte plyométrique 3-en-1 | $169.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Échelle d'agilité Northern Lights, 6 m x 13 échelons | $17.86 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Échelle d'agilité Northern Lights, tapis en caoutchouc, 10 marches | $35.86 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |
| Échelle d’Agilité 4m – Pro | $31.03 (reg $46.29, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 429 from the retailer's site |

### Fitness Depot

Attempted 55; exact matches 48; price differences 2; held reads 0; stock changes 0; read failures 5.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| Northern Lights Rubber Hex Dumbbell | $2.20 (reg not stated, stock in_stock) | $44.00 (reg not stated, stock None) | DIFFERENCE | read via page JSON-LD offer; the record carries no headline variant marker; the recorded page sells a single variant read at $44.00, which matches the recorded variant '50 lb' at $44.00; the headline price is a computed entry price, not a read price |
| Urethane Fixed Dumbbell | $60.00 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | ValueError: no structured offer and no stated price found on the page |
| Neoprene Dumbbell | $2.00 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | ValueError: no structured offer and no stated price found on the page |
| Threaded Chrome 60 in Barbell, No Collars | $29.88 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | ValueError: no structured offer and no stated price found on the page |
| Cardio Pump Plate | $3.75 (reg not stated, stock in_stock) | $15.00 (reg not stated, stock None) | DIFFERENCE | read via page JSON-LD offer; the record carries no headline variant marker; the recorded page sells a single variant read at $15.00, which matches the recorded variant '10 lb' at $15.00; the headline price is a computed entry price, not a read price |
| PowerBlock Straight Barbell, USA Elite | $148.00 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | ValueError: no structured offer and no stated price found on the page |
| PowerBlock Urethane EZ-Curl Barbell | $148.00 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | ValueError: no structured offer and no stated price found on the page |

### Decathlon Canada

Attempted 56; exact matches 0; price differences 0; held reads 0; stock changes 0; read failures 56.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| Domyos Modular Weight Training Mat | $24.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos Run 100 E Compact Fitness Treadmill | $524.99 (reg $749.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos T 900 Treadmill | $1,099.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos Compact Run100 Folding Treadmill | $749.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos Connected Exercise Bike 900 | $849.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos EB 900B Self-Powered Connected Exercise Bike | $471.99 (reg $589.99, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos EB 520 B Self-Powered and Connected Exercise Bike | $489.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos EB140 B Connected Exercise Bike | $309.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos Biking 100 Exercise Bike | $272.99 (reg $389.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos EL 300 Elliptical Trainer | $449.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos EL 540 Self-Powered Connected Elliptical Trainer | $749.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos Connected Rowing Machine 900 | $849.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos R 500B Self-Powered and Connected Rowing Machine | $454.99 (reg $649.99, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos MS 100 Fitness Mini Stepper | $84.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos MS 520 Mini Stepper | $129.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos MS 500 Fitness Mini Stepper | $69.99 (reg $99.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos Hex Dumbbells | $34.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Decathlon Domyos Kettlebell | $35.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Decathlon Domyos Kettlebell Pro | $24.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| DOMYOS Compact Guided Weight Machine, Home Gym 900 | $674.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Weight Training Dumbbell Set 20 kg (44 lb) | $84.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Dumbbell Set with Bar 50 kg (110 lb) | $209.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Weight Training Cage, Power Rack 900 | $619.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Fold-Down / Incline Weights Bench 500 | $149.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| 70 cm Lockable Pull-Up Bar | $34.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Adjustable Dip Bars - TS 100 | $94.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| 10 kg 28 mm Cast-Iron Weight Plate | $39.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Incline And Decline Weight Bench | $224.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Folding Weight Bench | $95.00 (reg $120.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Pull-Up and Dip Station, TS 900 | $299.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Weight Training Dumbbell Kit 10 kg (22 lb) | $31.99 (reg $44.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Adjustable Functional Training and Weight Training Kettlebell, 12–24 kg | $109.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Folding Floor Mat 8 mm | $19.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Durable Fitness Mat, 7 mm | $28.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Exercise Mat - 500 | $39.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Exercise Mat - 900 | $44.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Adjustable Ab Wheel | $21.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Weight Training Dual Mode Ab Wheel | $10.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Multi-Level Ab Wheel | $24.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Abdominal & Core Trainer Mat - Ab Mat | $29.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| All Surfaces Weight Training Gliding Discs x2 | $15.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Push-Up Bar Grips | $6.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Push-Up Bar Grips with Clip-On Wobble Base | $13.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Strength Training Foam Squat Pad - Black | $24.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Weight Training Hip Thrust Pad - Green | $29.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Weighted Vest, 6 to 10 kg | $74.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| 0-5 kg Washable Weighted Vest | $44.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| 0.5 to 2 kg Wrist and Ankle Weights | $34.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Wrist and Ankle Weights 2 x 2 kg (4.4 lb) | $29.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Wrist and Ankle Weights 2 x 1 kg | $21.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Weight Training Suspension Trainer - Black/Blue | $34.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Fitness Wooden Rings | $44.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Weight training rope | $29.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Compact Strength Training Kit | $39.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Weight Training Pulley Handle - Black | $6.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Weight Training Ankle Strap - Black | $15.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |

### Horizon Fitness Canada

Attempted 11; exact matches 10; price differences 1; held reads 0; stock changes 0; read failures 0.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| Horizon 7.0 AE Elliptical | $1,442.30 (reg not stated, stock out_of_stock) | $1,444.01 (reg not stated, stock out_of_stock) | DIFFERENCE | read via page JSON-LD offer; the page sells a single variant; the record carries no headline variant marker; price rise of $1.71 (0.1 percent) since the last recorded check |

### Great Life Fitness

Attempted 175; exact matches 174; price differences 0; held reads 0; stock changes 0; read failures 1.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| NORDICTRACK - S22I STUDIO BIKE (SPIN BIKE) | $2,499.00 (reg $2,599.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | ValueError: no structured offer and no stated price found on the page |

### Costco Canada

Attempted 23; exact matches 22; price differences 0; held reads 0; stock changes 0; read failures 1.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| Echelon Adjustable Dumbbells Set 7–52.5 lb. with Stand, Quick Weight Adjustment, Space-Saving Design | $499.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 404 from the retailer's site |

### Fitness Depot Toronto

Attempted 2; exact matches 1; price differences 0; held reads 0; stock changes 0; read failures 1.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| PowerBlock Pro 100 Exp Stage 1 Base Kit, 5-40lbs | $488.00 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | ValueError: no structured offer and no stated price found on the page |

### Peloton Canada

Attempted 7; exact matches 5; price differences 0; held reads 0; stock changes 0; read failures 2.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| Dumbbells | $60.00 (reg $70.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | ValueError: no Peloton price mapping for slug 'peloton-dumbbells' |
| Bike Weights | $18.00 (reg $30.00, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | ValueError: no Peloton price mapping for slug 'peloton-bike-weights' |

### Rogue Canada

Attempted 81; exact matches 78; price differences 1; held reads 2; stock changes 1; read failures 0; expected failures 0.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| Rogue Dumbbell Bumpers | $92.00 (reg not stated, stock as_stated) | not stated (reg not stated, stock None) | HELD READ | read via page JSON-LD offer; record is missing its headline variant marker: the record carries 7 recorded variants, none of them marked as the headline variant; the page sells 8 variants (Default Title at $571.00, Default Title at $860.00, Default Title at $1,120.00, Default Title at $1,796.00, Default Title at $1,705.00, Default Title at $2,000.00, Default Title at $3,261.00, Default Title at $3,909.00); none is priced at the recorded $92.00, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |
| Rogue 6-Shooter Urethane Olympic Grip Plates | $462.00 (reg not stated, stock out_of_stock) | $462.00 (reg not stated, stock in_stock) | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $462.00 among the page's 7 variants; stock change: recorded out_of_stock, page now states in_stock |
| Rogue Log Bag | $205.00 (reg not stated, stock as_stated) | $179.00 (reg not stated, stock in_stock) | DIFFERENCE | read via page JSON-LD offer; the page sells a single variant; the record carries no headline variant marker; price drop of $26.00 (12.7 percent) since the last recorded check |
| Regupol Aktiv Flooring | $232.00 (reg not stated, stock in_stock) | $640.00 (reg not stated, stock in_stock) | HELD READ | read via page JSON-LD offer; the page sells a single variant; the record carries no headline variant marker; read is 175.9 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price |

## Headline variant marker gaps

These records carry no headline variant marker. The reader did not silently take the first variant of a multi variant page: it identified the tracked configuration by the recorded price where a variant carries it, and attributed no read where none does.

| Product | Store | Result | How the read was handled |
|---|---|---|---|
| Gorilla 2x2 8mm Interlocking Rubber Tile, Black | Treadmill Factory | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $9.99 among the page's 2 variants |
| Premium Rubber Flooring 4 x 6 ft, 6 mm | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $63.97 among the page's 2 variants |
| Premium Rubber Flooring 4 x 6 ft, 8 mm | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $114.99 among the page's 2 variants |
| Home Rubber Flooring Roll 4 x 25 ft, 6 mm | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $259.99 among the page's 3 variants |
| Home Rubber Flooring Roll 4 x 25 ft, 8 mm | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $299.99 among the page's 3 variants |
| Home Rubber Flooring Roll 4 x 25 ft, 12 mm | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $469.99 among the page's 3 variants |
| Rubber Gym Tiles | Matsuru | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $10.99 among the page's 2 variants; 2 variants carry that price |
| Concept2 RowErg | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,499.00 among the page's 2 variants |
| Aviron Strong Series Rower | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $2,699.00 among the page's 3 variants; 2 variants carry that price |
| Ascend Power Cage 3.0 | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $399.00 among the page's 4 variants |
| Bells of Steel Light Commercial Power Rack | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $699.99 among the page's 2 variants |
| NUOBELL 550 Adjustable Dumbbell Set, 2 by 50 lb | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $589.00 among the page's 6 variants; 6 variants carry that price; compare at price differs: recorded not stated, read $699.00 |
| Montreal Weights Adjustable Kettlebell, 10 to 40 lb | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $149.00 among the page's 2 variants; 2 variants carry that price |
| Bells of Steel Adjustable Competition Kettlebell, 12 to 20.5 kg | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $189.99 among the page's 16 variants; 4 variants carry that price |
| Montreal Weights Ascend 2.0 Bench | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $199.00 among the page's 3 variants; 3 variants carry that price |
| Bells of Steel Barenaked Power Bar, Bare Steel | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $199.99 among the page's 2 variants |
| Bells of Steel Utility Bar, Black Zinc | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $224.99 among the page's 4 variants |
| Bells of Steel Dead Bounce All Black Bumper Plates, 260 lb Set | Bells of Steel | HELD READ | read via Shopify .js; record is missing its headline variant marker: the record carries no recorded variants and no headline variant marker; the page sells 5 variants (10 LB (Pair) at $45.99, 15 LB (Pair) at $63.99, 25 LB (Pair) at $87.99, 35 LB (Pair) at $119.99, 45 LB (Pair) at $149.99); none is priced at the recorded $447.99, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |
| Gorila Ox Bumper Plates, 160 lb Package | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $477.00 among the page's 11 variants |
| Northern Lights Standard Olympic Plate, Cast Iron, 45 lb | Fitness Depot Plus | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $56.25 among the page's 6 variants; compare at price differs: recorded not stated, read $69.99 |
| Bells of Steel Residential Power Rack | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $262.97 among the page's 2 variants |
| Rogue RML-390F Flat Foot Monster Lite Rack | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,247.00 among the page's 4 variants; 2 variants carry that price |
| Concept2 SkiErg | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,167.00 among the page's 3 variants; 2 variants carry that price |
| Bells of Steel Ergo Rubber Hex Dumbbells (Pairs) | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $22.99 among the page's 23 variants |
| Montreal Weights Hex Dumbbell Sets With Rack | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $249.99 among the page's 3 variants; compare at price differs: recorded not stated, read $399.00 |
| Orion Rubber Hex Dumbbells | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $5.25 among the page's 29 variants; compare at price differs: recorded not stated, read $10.00 |
| Orion Neoprene Hex Dumbbells | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1.00 among the page's 12 variants; compare at price differs: recorded not stated, read $2.00 |
| Gorila Black Rubber Hex Dumbbell | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $4.65 among the page's 27 variants |
| Gorila YORK Rubber Hex Dumbbells | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $5.50 among the page's 32 variants |
| Gorila Hex Dumbbell Sets | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $866.50 among the page's 2 variants |
| Bells of Steel Powder Coated Kettlebell | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $21.99 among the page's 13 variants |
| Bells of Steel Competition Kettlebell | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $44.99 among the page's 16 variants |
| Treadmill Factory Element Vinyl Kettlebell | Treadmill Factory | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $6.95 among the page's 17 variants; compare at price differs: recorded not stated, read $9.99 |
| Northern Fitness Orion Cast Iron Kettlebell | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $10.96 among the page's 21 variants; compare at price differs: recorded not stated, read $18.50 |
| Northern Fitness Orion Competition Cast Iron Kettlebell | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $39.25 among the page's 8 variants; compare at price differs: recorded not stated, read $54.99 |
| Northern Fitness Orion Competition Steel Kettlebell | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $39.40 among the page's 10 variants; compare at price differs: recorded not stated, read $52.00 |
| Gorila Cast Iron Kettlebell | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $57.00 among the page's 11 variants; stock change: recorded in_stock, page now states out_of_stock |
| Gorila Rubber Coated Kettlebell | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $112.00 among the page's 5 variants |
| Orion Functional Trainer | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,599.00 among the page's 4 variants; compare at price differs: recorded not stated, read $1,999.00 |
| Orion All-in-One Functional Trainer | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,899.00 among the page's 4 variants |
| REP Fitness Summit All-In-One Trainer with Ares 2.0 | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $7,544.00 among the page's 16 variants; 5 variants carry that price |
| Bells of Steel Cable Tower | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,049.99 among the page's 6 variants |
| Oblivyon Tower, 3 x 3 Cable Tower | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,439.99 among the page's 5 variants |
| Bells of Steel Cable Tower Squat Stands | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $2,149.99 among the page's 4 variants |
| Oblivyon Tower, 3 x 3 Cable Tower Squat Stands | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $2,929.99 among the page's 4 variants |
| Ascend CT300 Cable Workout Tower | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $349.99 among the page's 3 variants |
| REP Summit All-In-One with Wall-Mounted Ares 2.0 | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $7,057.00 among the page's 16 variants; 5 variants carry that price |
| Bells of Steel Buzz-Saw Heavy-Duty Adjustable Bench | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $389.99 among the page's 6 variants |
| Bells of Steel Converter Bench, Flat Bench | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $359.99 among the page's 2 variants |
| Bells of Steel Soft Glute Bench | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $199.99 among the page's 3 variants |
| Gorila Venom GHD Attachment | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,449.00 among the page's 3 variants; 3 variants carry that price |
| Rogue Chan Bar, Cerakote | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $603.00 among the page's 2 variants; 2 variants carry that price |
| REP Change Plates, Pair | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $46.00 among the page's 4 variants; compare at price differs: recorded not stated, read $46.00 |
| REP Calibrated Steel Plates, Pair | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $59.00 among the page's 9 variants; compare at price differs: recorded not stated, read $59.00 |
| Orion Calibrated Powerlifting Plate Sets | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $559.00 among the page's 3 variants; compare at price differs: recorded not stated, read $799.00 |
| Calibrated Powerlifting Plates (KG) | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $13.99 among the page's 9 variants |
| Out of Spec LB Competition Bumper Plates | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $149.99 among the page's 4 variants |
| Altas Strength Weight Plate | Altas Strength | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $15.00 among the page's 5 variants |
| Zenith Half Rack + Plate Storage | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $399.00 among the page's 2 variants; 2 variants carry that price; compare at price differs: recorded not stated, read $699.00 |
| Zenith Half Rack 2.0 | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $219.00 among the page's 2 variants; 2 variants carry that price; compare at price differs: recorded not stated, read $399.00 |
| NOHRD Folding SquatRack | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $3,779.00 among the page's 5 variants; 3 variants carry that price; compare at price differs: recorded not stated, read $3,779.00 |
| Rogue RM-3 Monster Rack 2.0 | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $2,171.00 among the page's 12 variants; 11 variants carry that price |
| Rogue RM-4 Monster Rack 2.0 | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $2,614.00 among the page's 12 variants; 11 variants carry that price |
| Rogue RM-6 Monster Rack 2.0 | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $4,079.00 among the page's 12 variants; 11 variants carry that price |
| Monster Lite Rig 2.0 | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $3,158.00 among the page's 121 variants; 2 variants carry that price |
| VersaClimber SM-Magnetic Climber | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $11,299.00 among the page's 2 variants; 2 variants carry that price |
| Pro Rubber Roll 4 x 25 ft, 6 mm | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $299.00 among the page's 8 variants |
| Pro Interlocking Tile 2 x 2, 6 mm, Black | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $12.99 among the page's 6 variants |
| Interlocking Rubber Tiles, 6 mm, Black | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $7.99 among the page's 9 variants; 2 variants carry that price |
| Heavy Duty Rubber Floor Tiles, 8 mm, 6 Pack, Grey | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $129.00 among the page's 2 variants |
| Bells of Steel Basilisk Stack Loaded Leg Extension / Leg Curl | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $2,379.99 among the page's 5 variants |
| Force USA XCalibur Locking Collars | Force USA Canada | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $149.00 among the page's 3 variants; 3 variants carry that price |
| Gorila Jammer Arms | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,099.00 among the page's 9 variants; 9 variants carry that price |
| Gorila Toro Dip Station | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $219.00 among the page's 3 variants |
| Gorila Sequoias Vertical Plate Storage | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $379.00 among the page's 2 variants |
| Force USA Storage Racks | Force USA Canada | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $449.00 among the page's 2 variants; compare at price differs: recorded $349.00, read $499.00 |
| Gorila Venom GHD Storage | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $99.00 among the page's 3 variants |
| Rogue Dog Sled 1.2 | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $459.00 among the page's 5 variants; 2 variants carry that price |
| Torque TANK M1 Push Sled | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $999.00 among the page's 3 variants |
| Bells of Steel 3 in 1 Anti-Slip Wood Plyo Boxes | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $59.99 among the page's 5 variants |
| 3-in-1 Soft Plyo Boxes | Northern Fitness | HELD READ | read via Shopify .js; record is missing its headline variant marker: the record carries 3 recorded variants, none of them marked as the headline variant; the page sells 3 variants (Small at $143.00, Medium at $169.00, Large at $293.00); none is priced at the recorded $144.00, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |
| COREFX Medicine Ball | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $55.00 among the page's 6 variants; compare at price differs: recorded not stated, read $55.00 |
| Bells of Steel Mighty Grip Medicine Balls | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $11.97 among the page's 10 variants |
| Bells of Steel Triple Stitched Medicine Balls | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $59.99 among the page's 10 variants |
| Rogue Medicine Balls | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $124.00 among the page's 11 variants |
| COREFX Slam Ball | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $28.79 among the page's 3 variants |
| REP Fitness Slam Balls | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $33.00 among the page's 12 variants |
| Bells of Steel Slam Balls | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $19.99 among the page's 10 variants |
| Rogue Echo Slam Balls | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $61.50 among the page's 9 variants |
| Rogue Sandbags | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $117.00 among the page's 5 variants; 2 variants carry that price |
| Rogue Strongman Sandbags | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $117.00 among the page's 8 variants |
| Rogue 3-in-1 Sandbag | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $281.00 among the page's 4 variants; 2 variants carry that price |
| Rogue Jerry Can Sandbags (JC-100S) | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $131.00 among the page's 3 variants; 2 variants carry that price |
| Centr x Hyrox Competition Sandbag | Treadmill Factory | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $166.00 among the page's 3 variants |
| Orion 50ft Battle Rope | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $49.99 among the page's 2 variants |
| Bells of Steel Chain Weight Vest | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $99.99 among the page's 2 variants |
| Calibrated Weight Plates | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $20.00 among the page's 6 variants |
| Phoenix Olympic Weight Plate Holder | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $299.99 among the page's 21 variants; 11 variants carry that price |
| Premium Olympic Bar Collars (Choice of Color) | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $14.99 among the page's 8 variants; 8 variants carry that price |
| Premium Rubber Bumper Plates (Sold as a Pair) | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $36.00 among the page's 6 variants |
| Rubber Coated Olympic Weight Plates (Sold in Pair) | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $7.50 among the page's 6 variants |
| Adjustable Commercial Bench – Phoenix Series | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $599.99 among the page's 21 variants; 11 variants carry that price |
| 2-in-1 Phoenix Pro Training Cage | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $4,999.99 among the page's 63 variants; 33 variants carry that price |
| Phoenix 2-in-1 Training Cage | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $3,499.99 among the page's 63 variants; 36 variants carry that price |
| Phoenix 3-in-1 Smith Training Cage | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $3,999.99 among the page's 63 variants; 33 variants carry that price |
| Ultimate 3x3 Cage with Pulley System | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,899.99 among the page's 2 variants; 2 variants carry that price |
| Extra weight stack | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $379.99 among the page's 2 variants |
| Lion Fitness Medicine Ball | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $15.99 among the page's 10 variants |
| Lion Fitness Slam Ball | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $17.49 among the page's 13 variants |
| Phoenix - 3-Tier Round Dumbbell Rack – 15 Pairs | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,499.99 among the page's 21 variants; 12 variants carry that price |
| Phoenix - 3-Tier Round Dumbbell Rack– 20 Pairs | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,999.99 among the page's 21 variants; 11 variants carry that price |
| Veste lesté ajustable | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $49.99 among the page's 3 variants |
| Set: 5-50lb Hexagonal Rubber Dumbbells + 3-Tier Rack | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $739.49 among the page's 3 variants |
| Lion Fitness Round Commercial Dumbbells (Sold Individually) 5 lbs to 200 lbs | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $10.00 among the page's 40 variants |
| Lion Fitness Neoprene Dumbbells | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $7.99 among the page's 11 variants |
| Set: 5-50 lb Round Dumbbells with 2-Tier Commercial Rack | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,549.99 among the page's 2 variants |
| Hexagonal Dumbbell Set 5-100lb with 2-Tier Commercial Rack | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,239.49 among the page's 3 variants |
| Set: Round Dumbbells 5 to 30 lbs with Rack of your Choice | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $499.99 among the page's 2 variants; 2 variants carry that price |
| The Duo: 5-30LB with Rack and Compact Folding Bench | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $451.88 among the page's 2 variants; 2 variants carry that price |
| Ensemble: Haltères Ronds en Uréthane Lion Fitness | Lion Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,650.00 among the page's 3 variants |
| Gorila Camo Rack | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $999.00 among the page's 72 variants; 2 variants carry that price |
| Gorila HR90 Half Rack | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,799.00 among the page's 54 variants; 6 variants carry that price |
| Gorila S15 Sheep Rack | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $549.00 among the page's 3 variants |
| Gorila SP3+ Power Rack | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,599.00 among the page's 72 variants; 8 variants carry that price |
| Gorila SP3B Power Rack | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,849.00 among the page's 72 variants; 8 variants carry that price |
| Gorila J72 Squat Stand | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $829.00 among the page's 9 variants; 8 variants carry that price |
| Gorila Silverback Wallmounts | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,249.00 among the page's 108 variants; 2 variants carry that price; compare at price differs: recorded $999.00, read not stated |
| Gorila SP3R Power Rack | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $2,799.00 among the page's 80 variants; 8 variants carry that price |
| Gorila Bamboo Squat Stand | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $719.00 among the page's 9 variants; 9 variants carry that price |
| Gorila Silverback Rig | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,599.00 among the page's 108 variants; 2 variants carry that price; compare at price differs: recorded $1,349.00, read not stated |
| Gorila SP3 Power Rack | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,549.00 among the page's 72 variants; 8 variants carry that price |
| Gorila J90 Squat Stand | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $929.00 among the page's 9 variants; 8 variants carry that price |
| Gorila AX35 PRO Rack | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,242.00 among the page's 32 variants; 15 variants carry that price |
| Gorila AX16 PRO Rack | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,112.00 among the page's 32 variants; 15 variants carry that price |
| Gorila AF35 PRO Fold Rack | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,749.00 among the page's 32 variants; 16 variants carry that price |
| Gorila AF35 Fold Rack | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,495.00 among the page's 10 variants; 5 variants carry that price |
| Gorila AF16 Fold Rack | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,387.00 among the page's 32 variants; 15 variants carry that price |
| Gorila Freedom Rig | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $2,599.00 among the page's 9 variants; 9 variants carry that price |
| Gorila AX16 Rack | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $950.00 among the page's 32 variants; 16 variants carry that price |
| Gorila AP3 Power Rack | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $2,046.00 among the page's 32 variants; 16 variants carry that price |
| Gorila AHR Half Rack | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,944.00 among the page's 32 variants; 16 variants carry that price |
| Gorila SP1E Power Rack | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $2,699.00 among the page's 9 variants |
| Gorila HR90D Double Half Rack | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $3,099.00 among the page's 9 variants; 8 variants carry that price |
| Gorila AX35 Rack | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,058.00 among the page's 32 variants; 15 variants carry that price |
| Gorila AF16 PRO Fold Rack | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,603.00 among the page's 32 variants; 16 variants carry that price |
| Gorila HR108 Half Rack | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $2,149.00 among the page's 9 variants; 9 variants carry that price |
| HomePro Dumbbells | Altas Strength | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $15.00 among the page's 11 variants |
| Force USA MyRack Modular Power Rack | Force USA Canada | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $406.00 among the page's 2 variants |
| Force USA Rubber Hex Dumbbell Sets | Force USA Canada | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $999.00 among the page's 3 variants |
| Force USA Rubber Hex Dumbbell Sets + Racks | Force USA Canada | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,099.00 among the page's 3 variants |
| IRONAX Athletic Series Commercial Bumper Plates | Treadmill Factory | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $14.90 among the page's 4 variants |
| Nike Grind Bumper Plates — Fusion | Treadmill Factory | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $55.00 among the page's 5 variants |
| Nike Grind Bumper Plates — Solar Haze | Treadmill Factory | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $55.00 among the page's 5 variants |
| Nike Rubber Bumper Plates — Black/White | Treadmill Factory | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $55.00 among the page's 5 variants |
| Nike Grind Change Plates — Wolf Grey Particle | Treadmill Factory | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $21.00 among the page's 4 variants |
| Nike Change Plates | Treadmill Factory | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $21.00 among the page's 4 variants |
| Nike Strength Pro Urethane Plates — Black/White | Treadmill Factory | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $35.00 among the page's 5 variants |
| Centr x Hyrox Competition Edge Bumper Plate | Treadmill Factory | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $70.00 among the page's 6 variants |
| Mega Fitness 1" Standard Steel Weight Plates | Treadmill Factory | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $2.48 among the page's 6 variants |
| NÜOBELL S 560 Adjustable Dumbbell Set | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $899.00 among the page's 2 variants; 2 variants carry that price |
| NÜOBELL S 5100 Adjustable Dumbbell Set | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,299.00 among the page's 4 variants; 4 variants carry that price |
| REP Fitness Urethane Dumbbell Sets | Northern Fitness | HELD READ | read via Shopify .js; record is missing its headline variant marker: the record carries 4 recorded variants, none of them marked as the headline variant; the page sells 4 variants (5-50 LB Set at $2,081.00, 55-75 LB Set at $2,471.00, 80-100 LB Set at $3,251.00, 5-100 LB Set at $7,411.00); none is priced at the recorded $2,090.00, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |
| NÜOBELL Adjustable Dumbbells | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $629.99 among the page's 14 variants; 7 variants carry that price |
| PowerBlock Elite USA EXP | Fitness Depot Plus | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $200.00 among the page's 3 variants |
| Rogue Dumbbell Sets | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,334.00 among the page's 3 variants |
| Rogue Urethane Dumbbells | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $3,362.00 among the page's 35 variants |
| NÜOBELL-S Adjustable Dumbbells | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $678.97 among the page's 8 variants; 2 variants carry that price |
| Urethane Dumbbells | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,899.99 among the page's 3 variants |
| Ergo Rubber Hex Dumbbells | Bells of Steel | HELD READ | read via Shopify .js; record is missing its headline variant marker: the record carries 3 recorded variants, none of them marked as the headline variant; the page sells 23 variants (5 LB (Pair) at $22.99, 7.5 LB (Pair) at $35.99, 10 LB (Pair) at $41.99, 12.5 LB (Pair) at $50.99, 15 LB (Pair) at $61.99, 17.5 LB (Pair) at $63.99, 20 LB (Pair) at $81.99, 25 LB (Pair) at $107.99, 30 LB (Pair) at $127.99, 35 LB (Pair) at $149.99, 40 LB (Pair) at $163.99, 45 LB (Pair) at $154.99, 50 LB (Pair) at $205.99, 55 LB (Pair) at $225.99, 60 LB | 27 KG (Pair) at $247.99, 65 LB | 30 KG (Pair) at $267.99, 70 LB | 32 KG (Pair) at $287.99, 75 LB |  34 KG (Pair) at $309.99, 80 LB | 36 KG (Pair) at $209.99, 85 LB | 39 KG (Pair) at $349.99, 90 LB | 41 KG (Pair) at $369.99, 95 LB | 43 KG (Pair) at $391.99, 100 LB (Pair) at $411.99); none is priced at the recorded $944.99, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |
| Straight Handle Rubber Hex Dumbbell Sets | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $949.99 among the page's 2 variants |
| AD80 Adjustable Dumbbell Set (Snode) | Northern Fitness | HELD READ | read via Shopify .js; record is missing its headline variant marker: the record carries 2 recorded variants, none of them marked as the headline variant; the page sells 2 variants (AD80 Adjustable Dumbbells at $660.00, AD80 Adjustable Dumbbells + 8 Magnet Weight Plates at $759.00); none is priced at the recorded $678.50, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |
| AD80 Adjustable Dumbbell + Stand Bundle (Snode) | Northern Fitness | HELD READ | read via Shopify .js; record is missing its headline variant marker: the record carries 2 recorded variants, none of them marked as the headline variant; the page sells 2 variants (AD80 Adjustable Dumbbells at $809.00, AD80 Adjustable Dumbbells + 8 Magnet Weight Plates at $858.00); none is priced at the recorded $889.00, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |
| Adjustable Dumbbell Set + Elite FID 2.0 Bench Bundle (NÜOBELL) | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $889.00 among the page's 12 variants; 6 variants carry that price |
| Elite EXP Adjustable Dumbbell Set (PowerBlock) | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $431.00 among the page's 3 variants; compare at price differs: recorded not stated, read $646.00 |
| EXP Adjustable Dumbbell Set (PowerBlock) | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $374.00 among the page's 3 variants |
| Hex Dumbbell Sets (REP Fitness) | Northern Fitness | HELD READ | read via Shopify .js; record is missing its headline variant marker: the record carries 4 recorded variants, none of them marked as the headline variant; the page sells 4 variants (5-50 LB Set at $1,431.00, 55-75 LB Set at $1,691.00, 80-100 LB Set at $2,146.00, 5-100 LB Set at $4,811.00); none is priced at the recorded $1,437.00, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |
| Knurled Grip Pro 100 EXP Dumbbell Set (PowerBlock) | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $548.00 among the page's 4 variants; compare at price differs: recorded not stated, read $739.00 |
| Pro 100 EXP Adjustable Dumbbells | 5-100lb Full Set (PowerBlock) | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,199.00 among the page's 2 variants; 2 variants carry that price |
| Pro 100 EXP Dumbbell Set (PowerBlock) | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $548.00 among the page's 4 variants |
| QuickDraw Adjustable Dumbbells (REP Fitness) | Northern Fitness | HELD READ | read via Shopify .js; record is missing its headline variant marker: the record carries 4 recorded variants, none of them marked as the headline variant; the page sells 4 variants (30 LB Pair at $437.00, 40 LB Pair at $541.00, 50 LB Pair at $645.00, 60 LB Pair at $749.00); none is priced at the recorded $439.00, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |
| REP x PÉPIN Adjustable Dumbbell Set | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,235.00 among the page's 4 variants |
| 580 Adjustable Dumbbell Set (NÜOBELL) | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $789.00 among the page's 6 variants; 3 variants carry that price |
| Multi-Function Smith Machine Bundles with Bumper Plates | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,999.00 among the page's 5 variants |
| Heavy Duty Adjustable Weight Bench 2.0 | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $349.00 among the page's 4 variants |
| Heavy Duty 8-in-1 Adjustable Bench | Ascend HB-800 | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $399.00 among the page's 2 variants |
| Foldable Wall Mounted Training Bundles With Bumper Plates (Various) | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $499.00 among the page's 4 variants |
| Olympic Training Bundles With Bumper Plates (Ascend Cage 3.0) | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $499.00 among the page's 8 variants; 2 variants carry that price |
| Olympic Training Bundles with Cast Iron Plates (Ascend Cage 3.0) | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $449.00 among the page's 8 variants; 2 variants carry that price |
| Olympic Training Bundles With Bumper Plates (Ascend Cage 1.0) | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $499.00 among the page's 4 variants |
| Olympic Training Bundles with Cast Iron Plates (Ascend Cage 1.0) | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $449.00 among the page's 4 variants |
| Compact Olympic Bundles - Cast Iron Plates | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $449.00 among the page's 8 variants |
| Compact Olympic Bundles - Bumper Plates | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $499.00 among the page's 8 variants; 2 variants carry that price |
| Pulley Attachment for Ascend Power Cage 3.0 | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $199.00 among the page's 2 variants; 2 variants carry that price; stock change: recorded in_stock, page now states out_of_stock |
| Plate Holders | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $39.99 among the page's 2 variants |
| Olympic Weight Plate Tree & Barbell Rack | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $149.00 among the page's 2 variants |
| Olympic Barbell | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $179.00 among the page's 2 variants; 2 variants carry that price; stock change: recorded in_stock, page now states out_of_stock |
| Premium Cast Iron Weight Plates | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $179.00 among the page's 5 variants |
| Regular Cast Iron Weight Plates | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $179.00 among the page's 5 variants; 2 variants carry that price |
| Montreal Weights Bumper Plates | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $49.00 among the page's 3 variants |
| Ascend Bumper Plates | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $49.00 among the page's 3 variants |
| Change Plates | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $29.99 among the page's 2 variants |
| Bundle: Set of Dumbbells (10 - 90 lb) & Bench | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $749.00 among the page's 6 variants |
| Bundle: Set of Dumbbells (5 - 52.5 lb) & Bench | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $449.00 among the page's 6 variants |
| Nuo Style Weights (5-70 lb or 7.5-90 lb) | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $599.00 among the page's 4 variants |
| Bundle: Nuo Style Dumbbells (5 - 70 lb or 7.5-90 lb) & Bench | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $799.00 among the page's 8 variants |
| Ascend 3-in-1 Adjustable Dumbbells (7 to 52.5 lb) | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $349.00 among the page's 2 variants |
| Bundle: Ascend 3-in-1 Adjustable Dumbbells (7 to 52.5 lb) & Bench | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $549.00 among the page's 3 variants; 2 variants carry that price; compare at price differs: recorded $850.00, read $800.00; stock change: recorded in_stock, page now states out_of_stock |
| Ascend Rubber Hex Dumbbells - Pairs (5 to 80 lb) | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $14.99 among the page's 16 variants |
| Ascend R-100 Magnetic Rower | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $499.00 among the page's 2 variants; 2 variants carry that price |
| Ascend R-200 Air Rower | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $699.00 among the page's 3 variants; 3 variants carry that price; stock change: recorded in_stock, page now states out_of_stock |
| Ascend L-200 Performance Elliptical | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $539.00 among the page's 2 variants; 2 variants carry that price |
| Hero Heavy-Duty Weight Bench | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $349.99 among the page's 4 variants |
| Monolift Rack Attachment | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $174.97 among the page's 2 variants |
| Landmine Rack Attachment | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $49.99 among the page's 3 variants |
| Kraken Rack Attachment for 4 Post Hydra & Manticore Racks (Single Side) | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $594.99 among the page's 8 variants; 2 variants carry that price |
| Functional Trainer | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,799.99 among the page's 3 variants |
| Functional Trainer Cable Tower | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,699.99 among the page's 5 variants; compare at price differs: recorded $3,199.99, read not stated; stock change: recorded in_stock, page now states out_of_stock |
| All-in-One Trainer | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,699.99 among the page's 4 variants |
| Drop-In Belt Squat / Stinger Belt Squat | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,709.99 among the page's 2 variants |
| Olympic Weightlifting Barbell | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $232.99 among the page's 2 variants |
| Safety Squat Bar - The SS4 | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $279.99 among the page's 5 variants |
| Axle Bars | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $94.99 among the page's 2 variants |
| Dead Bounce Conflict Bumper Plates | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $49.99 among the page's 6 variants |
| Crumb Bumper Plates | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $57.99 among the page's 5 variants |
| Coloured Bumper Plates | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $79.99 among the page's 6 variants |
| Urethane Bumper Plates | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $84.99 among the page's 5 variants |
| LB Competition Bumper Plates | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $189.99 among the page's 4 variants |
| KG Competition Bumper Plates | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $189.99 among the page's 4 variants |
| Calibrated Powerlifting Plates - LB | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $12.99 among the page's 10 variants; 2 variants carry that price |
| Gray Mighty Grip Olympic Weight Plates | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $9.99 among the page's 8 variants |
| Black Mighty Grip Olympic Weight Plates | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $9.99 among the page's 8 variants |
| Machined Iron Olympic Weight Plates | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $21.99 among the page's 6 variants |
| Rubber Coated Iron Weight Plates | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $14.99 among the page's 6 variants |
| Fractional Plates (Set of (8) 0.5lb Plates) | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $26.99 among the page's 2 variants |
| Urethane-Coated Change Plates | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $26.99 among the page's 10 variants |
| Urethane-Coated Change Plate Sets | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $259.99 among the page's 2 variants |
| Mark Wildman Adjustable Kettlebell | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $239.99 among the page's 5 variants; compare at price differs: recorded not stated, read $239.99 |
| Fitness Sandbag Sets | Bells of Steel | HELD READ | read via Shopify .js; record is missing its headline variant marker: the record carries 3 recorded variants, none of them marked as the headline variant; the page sells 8 variants (50 LB | 23 KG at $39.99, 100 LB | 45 KG at $44.99, 150 LB | 68 KG at $51.99, 200 LB | 91 KG at $58.99, 250 LB | 113 KG at $62.99, 300 LB | 136 KG at $69.99, 350 LB | 159 KG at $76.99, 400 LB | 181 KG at $83.99); none is priced at the recorded $188.99, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |
| Weighted Vest and Plates | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $49.49 among the page's 4 variants |
| Rogue Kettlebells | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $52.00 among the page's 18 variants |
| Rogue Kettlebell - E Coat | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $66.00 among the page's 15 variants |
| Rogue Kettlebell - Powder Coat | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $62.00 among the page's 12 variants |
| Rogue Rubber Coated Kettlebells | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $132.00 among the page's 5 variants |
| Rogue Competition Kettlebells | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $110.00 among the page's 13 variants |
| Rogue Thompson Fatbells | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $52.00 among the page's 15 variants |
| Rogue Loadable Kettlebell | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $109.00 among the page's 3 variants; 2 variants carry that price |
| Rogue Sand Kettlebells | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $78.00 among the page's 5 variants |
| GORUCK Sand Kettlebells | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $69.00 among the page's 5 variants |
| Rogue Dumbbells | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $35.00 among the page's 31 variants |
| Rogue Loadable Dumbbells | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $185.00 among the page's 9 variants; 2 variants carry that price |
| Rogue DB-15 Loadable Dumbbell | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $185.00 among the page's 9 variants; 2 variants carry that price |
| Rogue DB-15 Loadable Dumbbell - Stainless | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $206.00 among the page's 3 variants; 2 variants carry that price |
| Rogue DB25-10 Loadable Dumbbell | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $193.00 among the page's 3 variants; 2 variants carry that price |
| Rogue DB25-10 Loadable Dumbbell - Stainless | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $185.00 among the page's 3 variants; 2 variants carry that price |
| Monster Bells | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $774.00 among the page's 5 variants; 2 variants carry that price |
| Rogue Iron Dumbbells | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $66.00 among the page's 15 variants |
| Rogue HG 2.0 Bumper Plates | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $253.00 among the page's 12 variants |
| Rogue HG 2.0 KG Bumper Plates | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $253.00 among the page's 10 variants |
| Rogue Echo Bumper Plates V2 | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $239.00 among the page's 8 variants |
| Rogue Color Echo Bumper Plates | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $319.00 among the page's 12 variants |
| Rogue MIL Spec Echo Bumper | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $74.00 among the page's 8 variants |
| Rogue Bumper Plates by Hi-Temp | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $268.00 among the page's 14 variants |
| Rogue US-MIL Spec Bumper V2 | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $231.00 among the page's 13 variants |
| Rogue LB Competition Plates | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $495.00 among the page's 7 variants |
| Rogue Black Training LB Plates | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $460.00 among the page's 7 variants |
| Rogue Color LB Training 2.0 Plates | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $485.00 among the page's 7 variants |
| Rogue KG Training 2.0 Plates | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $317.00 among the page's 8 variants |
| Rogue Urethane Plates | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $502.00 among the page's 9 variants |
| Rogue Dumbbell Bumpers | Rogue Canada | HELD READ | read via page JSON-LD offer; record is missing its headline variant marker: the record carries 7 recorded variants, none of them marked as the headline variant; the page sells 8 variants (Default Title at $571.00, Default Title at $860.00, Default Title at $1,120.00, Default Title at $1,796.00, Default Title at $1,705.00, Default Title at $2,000.00, Default Title at $3,261.00, Default Title at $3,909.00); none is priced at the recorded $92.00, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |
| Rogue Technique Plates | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $247.00 among the page's 4 variants |
| Rogue Deep Dish Plates | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $281.00 among the page's 15 variants |
| Rogue 6-Shooter Olympic Grip Plates | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $292.00 among the page's 7 variants |
| Rogue 6-Shooter Urethane Olympic Grip Plates | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $462.00 among the page's 7 variants; stock change: recorded out_of_stock, page now states in_stock |
| Rogue Calibrated LB Steel Plates 2.0 - Black | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $425.00 among the page's 13 variants |
| Rogue Calibrated KG Steel Plates 2.0 - Black | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $360.00 among the page's 12 variants |
| Rogue LB Change Plates | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $50.00 among the page's 6 variants; compare at price differs: recorded $55.00, read not stated |
| Rogue KG Change Plates (IWF) | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $44.00 among the page's 7 variants; compare at price differs: recorded $50.00, read not stated |
| Rogue Olympic Change Plates | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $21.00 among the page's 4 variants |
| Rogue USA Olympic Change Plates | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $38.00 among the page's 6 variants |
| Rogue KG Medicine Balls | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $130.00 among the page's 4 variants |
| Rogue Rubber Medicine Ball | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $50.00 among the page's 9 variants |
| D-Ball Medicine Balls | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $99.00 among the page's 9 variants |
| Rogue MK D-balls | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $143.00 among the page's 2 variants |
| Rogue Hoover Medicine Balls | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $110.00 among the page's 2 variants |
| Dynamax Medicine Balls | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $151.00 among the page's 11 variants |
| Rogue Sandbag 2.0 | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $240.00 among the page's 4 variants; 2 variants carry that price |
| Rogue Echo Sandbag 2.0 | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $124.00 among the page's 4 variants; 2 variants carry that price; compare at price differs: recorded $144.00, read not stated |
| Rogue Echo Strongman Sandbags | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $76.00 among the page's 9 variants; 2 variants carry that price |
| Rogue Color Strongman Sandbags | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $137.00 among the page's 3 variants; 2 variants carry that price |
| Rogue Cyclone Strongman Sandbags | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $174.00 among the page's 4 variants |
| Rogue Feed Sack | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $137.00 among the page's 3 variants; 2 variants carry that price |
| Rogue Gym Mats - 25 Piece Bundle | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $2,106.00 among the page's 4 variants; 2 variants carry that price |
| Regupol AktivLok Interlocking Tiles | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $16.00 among the page's 6 variants; 2 variants carry that price |
| Regupol Econ Interlocking Tiles | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $15.00 among the page's 4 variants; 2 variants carry that price |
| Regupol AktivPro Tiles | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $336.00 among the page's 17 variants |
| 45 Degree Camber Curl selectorized machine | Fitness Depot Plus | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $2,199.00 among the page's 2 variants |
| Barre fixe en uréthane avec logo Northern Lights NL | Fitness Depot Plus | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $57.70 among the page's 10 variants |
| Northern Lights NL Logo Urethane Fixed EZ Curl | Fitness Depot Plus | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $86.50 among the page's 6 variants |
| Plaque de poids en fonte régulière Northern Lights | choix de 5 a 50 LB | Fitness Depot Plus | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $3.75 among the page's 5 variants |
| Hexagonal rubber dumbbell choice between 5lb and 120lb | Fitness Depot Plus | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $5.25 among the page's 33 variants |
| Neoprene dumbbell choice between 1lb and 15lb | Fitness Depot Plus | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $3.00 among the page's 11 variants |
| Northern Lights Fixed Urethane Dumbbell | Fitness Depot Plus | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $14.50 among the page's 21 variants |
| Haltères hexagonaux en néoprène | Fitness Depot Plus | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $3.00 among the page's 12 variants |
| Kettlebells Commercial en fonte recouverts de caoutchouc | Fitness Depot Plus | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $13.99 among the page's 10 variants |
| Balles murales TPWOD | Fitness Depot Plus | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $46.99 among the page's 3 variants |
| Element Fitness - Ballon médicinal | Fitness Depot Plus | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $29.99 among the page's 11 variants; stock change: recorded in_stock, page now states out_of_stock |
| Gilet lesté commercial XM Fitness | Fitness Depot Plus | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $129.00 among the page's 3 variants |
| Masse XM Fitness performance | Fitness Depot Plus | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $29.99 among the page's 5 variants |
| Parachute de résistance moyenne | Fitness Depot Plus | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $39.99 among the page's 2 variants |
| Pince à main Element Fitness | Fitness Depot Plus | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $14.99 among the page's 6 variants; 6 variants carry that price |
| Poids de cheville réglables TKO, 2,5 lb chacun, paire | Fitness Depot Plus | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $31.99 among the page's 2 variants |
| Slam ball choix entre 60lb et 150lb | Fitness Depot Plus | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $139.99 among the page's 6 variants; stock change: recorded in_stock, page now states out_of_stock |
| XM fitness Battle Rope | Fitness Depot Plus | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $127.99 among the page's 2 variants |
| Roll-Out Mats | Matsuru | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $8.49 among the page's 54 variants; 23 variants carry that price |
| Home Roll-Out Mats Pro - 12' x 12' | Matsuru | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,149.00 among the page's 8 variants; 4 variants carry that price; compare at price differs: recorded not stated, read $1,499.00 |
| Home Roll-Out Mats - 10' x 10' | Matsuru | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $699.00 among the page's 16 variants; 8 variants carry that price; compare at price differs: recorded not stated, read $999.00 |
| "Hybrid" Roll-Out Mat | Matsuru | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $109.00 among the page's 2 variants; compare at price differs: recorded not stated, read $159.00 |
| Wall Mats | Matsuru | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $109.99 among the page's 8 variants; 4 variants carry that price |
| Roll-Out Wall Mat | Matsuru | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $7.99 among the page's 15 variants; 5 variants carry that price |
| "Hybrid" Wall Panel | Matsuru | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $149.99 among the page's 2 variants |
| Tatami Mats | Matsuru | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $184.00 among the page's 6 variants; 6 variants carry that price; compare at price differs: recorded not stated, read $229.99 |
| Tatami Mats - 1 m x 1 m | Matsuru | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $99.99 among the page's 6 variants; 6 variants carry that price |
| Smooth Mats - 1 m x 1 m | Matsuru | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $99.99 among the page's 5 variants; 5 variants carry that price |

## Validation gates (observe only, blocking nothing)

- PASS: Gate 1: the live reference record parses. the published catalogue at https://canadahomegym.ca/ parsed cleanly; 2195 records loaded.
- FAIL: Gate 2: the public product count in the live reference matches the count the run processed. live reference holds 2195 public products; this run processed 2091 of them; 104 not processed.
  - Dotmar Fitness: 30 products
  - Irwin Fitness: 74 products
- PASS: Gate 3: every public product carries a recorded price or an explicit out of stock state from a dated check. 2195 of 2195 public products satisfy the gate.

## Dry run alert

An alert would be sent for this run. Its exact text follows. It was NOT sent.

```
To: hancventures@gmail.com
Subject: Canada Home Gym Price Watch checker alert, 2026-11-27: validation gate or store read failure

The standalone price checker run finished with problems that need attention. In live operation this run would publish nothing and the last good catalogue would stay live.

FAILED GATE: Gate 2: the public product count in the live reference matches the count the run processed
live reference holds 2195 public products; this run processed 2091 of them; 104 not processed.
Products involved:
- PR6-FT - 6-POST FUNCTIONAL TRAINER COMBO (Irwin Fitness)
- HR-24A: 24" DEPTH FLAT FOOT ANGLED HALF RACK (Irwin Fitness)
- SLM4-24: 24" DEPTH 4-POST POWER RACK (Irwin Fitness)
- SLM4-30: 30" DEPTH 4-POST POWER RACK (Irwin Fitness)
- PR6-41F: 6-POST FLAT FOOT POWER RACK (Irwin Fitness)
- PR6-41: 6-POST 41/20" DEPTH POWER RACK (Irwin Fitness)
- HR-24F: 24" DEPTH FLAT FOOT HALF RACK (Irwin Fitness)
- SLM6-30: 6-POST 30/18" DEPTH POWER RACK (Irwin Fitness)
- DOUBLE HALF RACK: DH-6 (Irwin Fitness)
- P-41: 41 DEPTH" 4-POST POWER RACK (Irwin Fitness)
- RAH-8P: 8-POST FULL RACK AND A HALF (Irwin Fitness)
- PCD: REVERSE HYPER / GHD (Irwin Fitness)
- COMPETITION BENCH (Irwin Fitness)
- IRWIN FITNESS AB-1.0 (Irwin Fitness)
- IRWIN FITNESS PRONE ROW 2.0 (Irwin Fitness)
- IRWIN FITNESS WELDED FLAT BENCH FB-7 (Irwin Fitness)
- SPARE ROLLERS - ROLLER J-CUP 2.0 (Irwin Fitness)
- RACK ATTACHED PEG BOARDS (Irwin Fitness)
- IRWIN FITNESS REMOVABLE UTILITY SEAT (Irwin Fitness)
- RACK BRIDGING SYSTEM (Irwin Fitness)
- IRWIN FITNESS UNIVERSAL 3X3" CROSSMEMBERS (Irwin Fitness)
- RACK MOUNTED LEG ROLLER (Irwin Fitness)
- SINGLE POST 1" STAINLESS STORAGE PIN (Irwin Fitness)
- ADJUSTABLE DIP BARS (Irwin Fitness)
- SINGLE BAR AND CHAIN STORAGE (Irwin Fitness)
- Double Bar Rack Mounted Storage (Irwin Fitness)
- ROTATIONAL LANDMINE ATTACHMENT (Irwin Fitness)
- IRWIN FITNESS SAFETY STRAP SYSTEM (Irwin Fitness)
- RACK ATTACHED STRAIGHT MULTI-GRIP PULLUP (Irwin Fitness)
- IRWIN FITNESS MONOLIFT ATTACHMENT (Irwin Fitness)
- IRWIN FITNESS RETURN ROLLER J-CUPS 2.0 (Irwin Fitness)
- 41" HORIZONTAL TOP CROSSMEMBER (Irwin Fitness)
- 5/8" HOLE - 3x3" SAFETY STRAP SHACKLES (Irwin Fitness)
- IRWIN FITNESS HALF SPOTTERS (Irwin Fitness)
- IRWIN FITNESS T-47 TROLLEY & LEVER ARM KIT (Irwin Fitness)
- ADJUSTABLE ATLAS BARS (Irwin Fitness)
- LOW ROFILE SANDWICH J-CUPS (Irwin Fitness)
- IRWIN FITNESS RACK STABILIZER FEET (Irwin Fitness)
- IRWIN FITNESS RACK HORNS (Irwin Fitness)
- ROLLER J-CUP DUFFALO/CB-4 BLOCKS (Irwin Fitness)
- IRWIN FITNESS FLIP-DOWN SAFTIES (PAIR) (Irwin Fitness)
- RACK MOUNTED CANTILEVER ARMS (Irwin Fitness)
- RACK MOUNTED A-HORNS (Irwin Fitness)
- SINGLE VERTICAL BARBELL HANGER (Irwin Fitness)
- RACK MOUNTED BAND HANGER (Irwin Fitness)
- BASE MOUNT SINGLE BAR STORAGE (Irwin Fitness)
- RACK ATTACHED MULTI-GRIP ANGLED PULLUP BAR (Irwin Fitness)
- DUAL FUNCTIONAL TRAINER STORAGE COMBO (Irwin Fitness)
- RACK ATTACHED FUNCTIONAL CABLE COLUMN (Irwin Fitness)
- FREE STANDING DUAL FUNCTIONAL CABLE COLUMN (Irwin Fitness)
- SINGLE FUNCTIONAL CABLE COLUMN (Irwin Fitness)
- Irwin Fitness Hi/Low Cable Tower (Irwin Fitness)
- 2-Tier Dumbbell Saddle Storage Rack (Irwin Fitness)
- 4-Tier Dumbbell Saddle Storage Rack (Irwin Fitness)
- 3-Tier Dumbbell Saddle Storage Rack (Irwin Fitness)
- Citadel Double Sided Saddle Rack (Irwin Fitness)
- IRWIN FITNESS ROUND URETHANE DUMBBELLS (Irwin Fitness)
- PowerBlock Pro 175 Commercial Set (Irwin Fitness)
- PowerBlock Pro 125 Commercial Set (Irwin Fitness)
- PowerBlock Pro 100 Commercial Set (Irwin Fitness)
- IFS BLACK 230lb TRAINING BUMPER SET (Irwin Fitness)
- 3" ACOUSTIC PRO OLYMPIC LIFTING PLATFORM (Irwin Fitness)
- 2" OLYMPIC LIFTING PLATFORM (Irwin Fitness)
- IRWIN FITNESS REVERSE HYPER (Irwin Fitness)
- 15 & 30 DEGREE WEDGE BOARDS (Irwin Fitness)
- ADJUSTABLE PULL BLOCKS (Irwin Fitness)
- ADJUSTABLE JERK BLOCKS (Irwin Fitness)
- VERTICAL KETTLEBELL RACK (Irwin Fitness)
- VERTICAL MED BALL RACK (Irwin Fitness)
- Free Standing 6-Bar Rack (Irwin Fitness)
- Citadel Corner Flat Shelves (Irwin Fitness)
- RACK MOUNTED SINGLE-POST BUMPER STORAGE SHELF (Irwin Fitness)
- RACK MOUNTED SINGLE-POST FLAT STORAGE SHELF (Irwin Fitness)
- 4-POST MULTI STORAGE RACK (Irwin Fitness)
- Atlantis NM-200 Functional Training System (Dotmar Fitness)
- Atlantis C-212 Pendulum Squat (Dotmar Fitness)
- Atlantis C-230 Leg Extension / Leg Curl Combo (Dotmar Fitness)
- Atlantis D-123 Lat Pulldown (Dotmar Fitness)
- Atlantis D-227 Glute & Ham Developer (Dotmar Fitness)
- Atlantis C-511-8 Half Rack (Dotmar Fitness)
- Atlantis Adjustable Leg Platform with Slide Adjustment (Dotmar Fitness)
- Atlantis RS-4 Rig System - Special Sale (Dotmar Fitness)
- Atlantis C-206 Leg Platform (Dotmar Fitness)
- Atlantis B-177 Adjustable Bench (Dotmar Fitness)
- Atlantis P-245 Dip Bar (Dotmar Fitness)
- Atlantis C-322 Poor Man's Glute & Ham Developer (Dotmar Fitness)
- Atlantis B-275 Flat Bench (Dotmar Fitness)
- Atlantis Jammer Arms (Pair)-older model (Dotmar Fitness)
- Atlantis Calf Platform (Dotmar Fitness)
- Atlantis Cambered/Neutral Pull-Up Bar (Dotmar Fitness)
- Atlantis Resistance Chains R-249 (Dotmar Fitness)
- Atlantis A-47 T-bar row with handles (Dotmar Fitness)
- Atlantis A-45 One Row Handle (Dotmar Fitness)
- Atlantis 23 in. Attachment Grip (Dotmar Fitness)
- Atlantis C-105 Leg Extension (Dotmar Fitness)
- Atlantis B-157 Biceps Curl (Dotmar Fitness)
- Atlantis Olympic Platform with Insert (Dotmar Fitness)
- Atlantis M-126 Tibia Dorsi Flexion (Dotmar Fitness)
- Atlantis R-734 Landmine (Dotmar Fitness)
- Atlantis 35 in. Attachment Grip (Dotmar Fitness)
- Atlantis 29 in. Attachment Grip (Dotmar Fitness)
- Atlantis 11 in. Attachment Grip (Dotmar Fitness)
- Atlantis 16 in. Attachment Grip (Dotmar Fitness)
- Atlantis 15 in. Attachment Grip (Dotmar Fitness)

STORE READ FAILURES: Decathlon Canada: 56 of 56 products failed to read, over half the store's products in this run.
Products involved:
- Domyos Modular Weight Training Mat: HTTP 403 from the retailer's site
- Domyos Run 100 E Compact Fitness Treadmill: HTTP 403 from the retailer's site
- Domyos T 900 Treadmill: HTTP 403 from the retailer's site
- Domyos Compact Run100 Folding Treadmill: HTTP 403 from the retailer's site
- Domyos Connected Exercise Bike 900: HTTP 403 from the retailer's site
- Domyos EB 900B Self-Powered Connected Exercise Bike: HTTP 403 from the retailer's site
- Domyos EB 520 B Self-Powered and Connected Exercise Bike: HTTP 403 from the retailer's site
- Domyos EB140 B Connected Exercise Bike: HTTP 403 from the retailer's site
- Domyos Biking 100 Exercise Bike: HTTP 403 from the retailer's site
- Domyos EL 300 Elliptical Trainer: HTTP 403 from the retailer's site
- Domyos EL 540 Self-Powered Connected Elliptical Trainer: HTTP 403 from the retailer's site
- Domyos Connected Rowing Machine 900: HTTP 403 from the retailer's site
- Domyos R 500B Self-Powered and Connected Rowing Machine: HTTP 403 from the retailer's site
- Domyos MS 100 Fitness Mini Stepper: HTTP 403 from the retailer's site
- Domyos MS 520 Mini Stepper: HTTP 403 from the retailer's site
- Domyos MS 500 Fitness Mini Stepper: HTTP 403 from the retailer's site
- Domyos Hex Dumbbells: HTTP 403 from the retailer's site
- Decathlon Domyos Kettlebell: HTTP 403 from the retailer's site
- Decathlon Domyos Kettlebell Pro: HTTP 403 from the retailer's site
- DOMYOS Compact Guided Weight Machine, Home Gym 900: HTTP 403 from the retailer's site
- Weight Training Dumbbell Set 20 kg (44 lb): HTTP 403 from the retailer's site
- Dumbbell Set with Bar 50 kg (110 lb): HTTP 403 from the retailer's site
- Weight Training Cage, Power Rack 900: HTTP 403 from the retailer's site
- Fold-Down / Incline Weights Bench 500: HTTP 403 from the retailer's site
- 70 cm Lockable Pull-Up Bar: HTTP 403 from the retailer's site
- Adjustable Dip Bars - TS 100: HTTP 403 from the retailer's site
- 10 kg 28 mm Cast-Iron Weight Plate: HTTP 403 from the retailer's site
- Incline And Decline Weight Bench: HTTP 403 from the retailer's site
- Folding Weight Bench: HTTP 403 from the retailer's site
- Pull-Up and Dip Station, TS 900: HTTP 403 from the retailer's site
- Weight Training Dumbbell Kit 10 kg (22 lb): HTTP 403 from the retailer's site
- Adjustable Functional Training and Weight Training Kettlebell, 12–24 kg: HTTP 403 from the retailer's site
- Folding Floor Mat 8 mm: HTTP 403 from the retailer's site
- Durable Fitness Mat, 7 mm: HTTP 403 from the retailer's site
- Exercise Mat - 500: HTTP 403 from the retailer's site
- Exercise Mat - 900: HTTP 403 from the retailer's site
- Adjustable Ab Wheel: HTTP 403 from the retailer's site
- Weight Training Dual Mode Ab Wheel: HTTP 403 from the retailer's site
- Multi-Level Ab Wheel: HTTP 403 from the retailer's site
- Abdominal & Core Trainer Mat - Ab Mat: HTTP 403 from the retailer's site
- All Surfaces Weight Training Gliding Discs x2: HTTP 403 from the retailer's site
- Push-Up Bar Grips: HTTP 403 from the retailer's site
- Push-Up Bar Grips with Clip-On Wobble Base: HTTP 403 from the retailer's site
- Strength Training Foam Squat Pad - Black: HTTP 403 from the retailer's site
- Weight Training Hip Thrust Pad - Green: HTTP 403 from the retailer's site
- Weighted Vest, 6 to 10 kg: HTTP 403 from the retailer's site
- 0-5 kg Washable Weighted Vest: HTTP 403 from the retailer's site
- 0.5 to 2 kg Wrist and Ankle Weights: HTTP 403 from the retailer's site
- Wrist and Ankle Weights 2 x 2 kg (4.4 lb): HTTP 403 from the retailer's site
- Wrist and Ankle Weights 2 x 1 kg: HTTP 403 from the retailer's site
- Weight Training Suspension Trainer - Black/Blue: HTTP 403 from the retailer's site
- Fitness Wooden Rings: HTTP 403 from the retailer's site
- Weight training rope: HTTP 403 from the retailer's site
- Compact Strength Training Kit: HTTP 403 from the retailer's site
- Weight Training Pulley Handle - Black: HTTP 403 from the retailer's site
- Weight Training Ankle Strap - Black: HTTP 403 from the retailer's site

This alert was composed by the checker in dry run form. No email was sent.
```

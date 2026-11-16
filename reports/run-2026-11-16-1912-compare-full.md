# Checker run report

Run at (UTC): 2026-11-16T19:12:01.325960+00:00
Mode: full run, all stores with a reader (10 Shopify, 6 structured, Peloton, Rogue); COMPARE MODE: the reference record is the live published catalogue at https://canadahomegym.ca/, not the local data file. OBSERVE ONLY: no prices changed, data file untouched, nothing published, no email sent.
Products checked: 423
Summary: DIFFERENCE 6, HELD READ 4, MATCH 387, READ FAILURE 26

## Per store results

### Bells of Steel

Attempted 70; exact matches 68; price differences 0; held reads 1; stock changes 0; read failures 1.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| Bells of Steel Dead Bounce All Black Bumper Plates, 260 lb Set | $447.99 (reg $559.99, stock in_stock) | not stated (reg not stated, stock None) | HELD READ | read via Shopify .js; record is missing its headline variant marker: the record carries no recorded variants and no headline variant marker; the page sells 5 variants (10 LB (Pair) at $45.99, 15 LB (Pair) at $63.99, 25 LB (Pair) at $87.99, 35 LB (Pair) at $119.99, 45 LB (Pair) at $149.99); none is priced at the recorded $447.99, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |
| Bells of Steel Fitness Sandbags | $39.99 (reg $59.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 404 from the retailer's site |

### Montreal Weights

Attempted 12; exact matches 12; price differences 0; held reads 0; stock changes 0; read failures 0.

### Gorila Fitness

Attempted 30; exact matches 30; price differences 0; held reads 0; stock changes 0; read failures 0.

### Northern Fitness

Attempted 61; exact matches 59; price differences 0; held reads 0; stock changes 0; read failures 2.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| REP Fitness Medicine Balls 2.0 | $59.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 404 from the retailer's site |
| COREFX Wall Balls | $82.47 (reg $92.99, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 404 from the retailer's site |

### Treadmill Factory

Attempted 48; exact matches 43; price differences 3; held reads 2; stock changes 1; read failures 0.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| AssaultRunner Pro | $3,999.00 (reg $4,599.00, stock in_stock) | $3,999.00 (reg $4,599.00, stock out_of_stock) | MATCH | read via Shopify .js; the page sells a single variant; the record carries no headline variant marker; stock change: recorded in_stock, page now states out_of_stock |
| Element Fitness Virgin Rubber Hex Dumbbells | $3.87 (reg not stated, stock in_stock) | $12.90 (reg $30.00, stock None) | DIFFERENCE | read via Shopify .js; the record carries no headline variant marker; the recorded page sells a single variant read at $12.90, which matches the recorded variant '10 lb' at $12.90; the headline price is a computed entry price, not a read price |
| Weider Rubber Hex Dumbbell | $3.45 (reg not stated, stock in_stock) | $24.15 (reg $52.50, stock None) | DIFFERENCE | read via Shopify .js; the record carries no headline variant marker; the recorded page sells a single variant read at $24.15, which matches the recorded variant '35 lb' at $24.15; the headline price is a computed entry price, not a read price |
| Weider Cast Iron Hex Dumbbell | $17.50 (reg $35.00, stock as_stated) | $24.15 (reg not stated, stock in_stock) | DIFFERENCE | read via page fallback (page JSON-LD offer); .js and .json failed: ['HTTP Error 404: Not Found', 'Shopify JSON carried no variants']; the page sells a single variant; the record carries no headline variant marker; price rise of $6.65 (38.0 percent) since the last recorded check; compare at price differs: recorded $35.00, read not stated |
| Weider Urethane Dumbbell | $5.00 (reg $10.00, stock in_stock) | $24.15 (reg not stated, stock in_stock) | HELD READ | read via page fallback (page JSON-LD offer); .js and .json failed: ['HTTP Error 404: Not Found', 'Shopify JSON carried no variants']; the page sells a single variant; the record carries no headline variant marker; read is 383.0 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price; compare at price differs: recorded $10.00, read not stated |
| Treadmill Factory XM Cast Iron Kettlebell | $16.00 (reg not stated, stock in_stock) | $64.00 (reg not stated, stock in_stock) | HELD READ | read via page fallback (page JSON-LD offer); .js and .json failed: ['HTTP Error 404: Not Found', 'Shopify JSON carried no variants']; the page sells a single variant; the record carries no headline variant marker; read is 300.0 percent away from the recorded price, at or over the 40 percent hold line; reported, not treated as a price |

### Force USA Canada

Attempted 19; exact matches 19; price differences 0; held reads 0; stock changes 0; read failures 0.

### Altas Strength

Attempted 33; exact matches 33; price differences 0; held reads 0; stock changes 0; read failures 0.

### Lion Fitness

Attempted 4; exact matches 4; price differences 0; held reads 0; stock changes 0; read failures 0.

### Matsuru

Attempted 4; exact matches 4; price differences 0; held reads 0; stock changes 0; read failures 0.

### Fitness Depot Plus

Attempted 13; exact matches 13; price differences 0; held reads 0; stock changes 0; read failures 0.

### Fitness Depot

Attempted 45; exact matches 41; price differences 2; held reads 0; stock changes 0; read failures 2.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| Northern Lights Rubber Hex Dumbbell | $2.20 (reg not stated, stock as_stated) | $44.00 (reg not stated, stock None) | DIFFERENCE | read via page JSON-LD offer; the record carries no headline variant marker; the recorded page sells a single variant read at $44.00, which matches the recorded variant '50 lb' at $44.00; the headline price is a computed entry price, not a read price |
| Urethane Fixed Dumbbell | $48.00 (reg not stated, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | ValueError: no structured offer and no stated price found on the page |
| Neoprene Dumbbell | $2.00 (reg not stated, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | ValueError: no structured offer and no stated price found on the page |
| Cardio Pump Plate | $3.75 (reg not stated, stock in_stock) | $15.00 (reg not stated, stock None) | DIFFERENCE | read via page JSON-LD offer; the record carries no headline variant marker; the recorded page sells a single variant read at $15.00, which matches the recorded variant '10 lb' at $15.00; the headline price is a computed entry price, not a read price |

### Decathlon Canada

Attempted 21; exact matches 0; price differences 0; held reads 0; stock changes 0; read failures 21.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| Domyos Modular Weight Training Mat | $24.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos Run 100 E Compact Fitness Treadmill | $749.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos T 900 Treadmill | $1,099.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos Compact Run100 Folding Treadmill | $749.99 (reg not stated, stock out_of_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos Connected Exercise Bike 900 | $849.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos EB 900B Self-Powered Connected Exercise Bike | $589.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos EB 520 B Self-Powered and Connected Exercise Bike | $489.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos EB140 B Connected Exercise Bike | $309.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos Biking 100 Exercise Bike | $389.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos EL 300 Elliptical Trainer | $449.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos EL 540 Self-Powered Connected Elliptical Trainer | $749.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos Connected Rowing Machine 900 | $849.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos R 500B Self-Powered and Connected Rowing Machine | $649.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos MS 100 Fitness Mini Stepper | $84.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos MS 520 Mini Stepper | $129.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos MS 500 Fitness Mini Stepper | $99.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Domyos Hex Dumbbells | $19.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Corength Hex Dumbbells | $69.99 (reg not stated, stock as_stated) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Decathlon Domyos Kettlebell | $29.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| Decathlon Domyos Kettlebell Pro | $24.99 (reg not stated, stock not_stated) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |
| DOMYOS Compact Guided Weight Machine, Home Gym 900 | $674.99 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | READ FAILURE | HTTP 403 from the retailer's site |

### Horizon Fitness Canada

Attempted 11; exact matches 10; price differences 1; held reads 0; stock changes 0; read failures 0.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| Horizon 7.0 AE Elliptical | $1,450.21 (reg not stated, stock as_stated) | $1,449.90 (reg not stated, stock out_of_stock) | DIFFERENCE | read via page JSON-LD offer; the page sells a single variant; the record carries no headline variant marker; price drop of $0.31 (0.0 percent) since the last recorded check |

### Great Life Fitness

Attempted 7; exact matches 7; price differences 0; held reads 0; stock changes 0; read failures 0.

### Costco Canada

Attempted 19; exact matches 19; price differences 0; held reads 0; stock changes 0; read failures 0.

### Fitness Depot Toronto

Attempted 1; exact matches 1; price differences 0; held reads 0; stock changes 0; read failures 0.

### Peloton Canada

Attempted 5; exact matches 5; price differences 0; held reads 0; stock changes 0; read failures 0.

### Rogue Canada

Attempted 20; exact matches 19; price differences 0; held reads 1; stock changes 0; read failures 0; expected failures 0.

| Product | Recorded | Read | Result | Reason |
|---|---|---|---|---|
| Rogue Medicine Balls | $64.00 (reg not stated, stock in_stock) | not stated (reg not stated, stock None) | HELD READ | read via page JSON-LD offer; record is missing its headline variant marker: the record carries 11 recorded variants, none of them marked as the headline variant; the page sells 11 variants (Default Title at $124.00, Default Title at $131.00, Default Title at $137.00, Default Title at $144.00, Default Title at $151.00, Default Title at $158.00, Default Title at $165.00, Default Title at $179.00, Default Title at $185.00, Default Title at $192.00, Default Title at $206.00); none is priced at the recorded $64.00, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |

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
| Rubber Gym Tiles | Matsuru | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $10.99 among the page's 2 variants; 2 variants carry that price; compare at price differs: recorded not stated, read $19.99 |
| Pro Rubber Roll 4 x 25 ft, 6 mm | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $299.00 among the page's 8 variants |
| Pro Interlocking Tile 2 x 2, 6 mm, Black | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $12.99 among the page's 6 variants |
| Interlocking Rubber Tiles, 6 mm, Black | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $7.99 among the page's 9 variants; 2 variants carry that price |
| Heavy Duty Rubber Floor Tiles, 8 mm, 6 Pack, Grey | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $129.00 among the page's 2 variants |
| Concept2 RowErg | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,499.00 among the page's 2 variants |
| Aviron Strong Series Rower | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $2,699.00 among the page's 3 variants; 2 variants carry that price |
| Ascend Power Cage 3.0 | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $399.00 among the page's 4 variants |
| Bells of Steel Light Commercial Power Rack | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $699.99 among the page's 2 variants |
| NUOBELL 550 Adjustable Dumbbell Set, 2 by 50 lb | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $589.00 among the page's 6 variants; 6 variants carry that price; compare at price differs: recorded not stated, read $699.00 |
| Montreal Weights Adjustable Kettlebell, 10 to 40 lb | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $149.00 among the page's 2 variants; 2 variants carry that price |
| Bells of Steel Adjustable Competition Kettlebell, 12 to 20.5 kg | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $189.99 among the page's 16 variants; 4 variants carry that price |
| Montreal Weights Ascend 2.0 Bench | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $199.00 among the page's 3 variants; 3 variants carry that price |
| Bells of Steel Barenaked Power Bar, Bare Steel | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $199.99 among the page's 2 variants |
| Bells of Steel Utility Bar, Black Zinc | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $224.99 among the page's 4 variants; compare at price differs: recorded not stated, read $249.99 |
| Bells of Steel Dead Bounce All Black Bumper Plates, 260 lb Set | Bells of Steel | HELD READ | read via Shopify .js; record is missing its headline variant marker: the record carries no recorded variants and no headline variant marker; the page sells 5 variants (10 LB (Pair) at $45.99, 15 LB (Pair) at $63.99, 25 LB (Pair) at $87.99, 35 LB (Pair) at $119.99, 45 LB (Pair) at $149.99); none is priced at the recorded $447.99, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |
| Gorila Ox Bumper Plates, 160 lb Package | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $477.00 among the page's 11 variants |
| Northern Lights Standard Olympic Plate, Cast Iron, 45 lb | Fitness Depot Plus | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $56.25 among the page's 6 variants; compare at price differs: recorded not stated, read $69.99 |
| Bells of Steel Residential Power Rack | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $379.99 among the page's 2 variants; 2 variants carry that price |
| Rogue RML-390F Flat Foot Monster Lite Rack | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,247.00 among the page's 4 variants; 2 variants carry that price |
| Concept2 SkiErg | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,167.00 among the page's 3 variants; 2 variants carry that price |
| Bells of Steel Ergo Rubber Hex Dumbbells (Pairs) | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $22.99 among the page's 23 variants |
| Montreal Weights Hex Dumbbell Sets With Rack | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $249.99 among the page's 3 variants; compare at price differs: recorded not stated, read $399.00 |
| Orion Rubber Hex Dumbbells | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $5.25 among the page's 29 variants; compare at price differs: recorded not stated, read $10.00 |
| Orion Neoprene Hex Dumbbells | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1.10 among the page's 12 variants; compare at price differs: recorded not stated, read $2.00 |
| Gorila Black Rubber Hex Dumbbell | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $4.65 among the page's 27 variants |
| Gorila YORK Rubber Hex Dumbbells | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $5.50 among the page's 32 variants |
| Gorila Hex Dumbbell Sets | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $866.50 among the page's 2 variants |
| Bells of Steel Powder Coated Kettlebell | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $23.99 among the page's 13 variants; compare at price differs: recorded not stated, read $29.99 |
| Bells of Steel Competition Kettlebell | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $44.99 among the page's 16 variants; compare at price differs: recorded not stated, read $51.99 |
| Treadmill Factory Element Vinyl Kettlebell | Treadmill Factory | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $6.95 among the page's 17 variants; compare at price differs: recorded not stated, read $9.99 |
| Northern Fitness Orion Cast Iron Kettlebell | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $10.96 among the page's 21 variants; compare at price differs: recorded not stated, read $18.50 |
| Northern Fitness Orion Competition Cast Iron Kettlebell | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $39.25 among the page's 8 variants; compare at price differs: recorded not stated, read $54.99 |
| Northern Fitness Orion Competition Steel Kettlebell | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $39.40 among the page's 10 variants; compare at price differs: recorded not stated, read $52.00 |
| Gorila Cast Iron Kettlebell | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $57.00 among the page's 11 variants |
| Gorila Rubber Coated Kettlebell | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $149.00 among the page's 5 variants |
| Orion Functional Trainer | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,599.00 among the page's 4 variants; compare at price differs: recorded not stated, read $1,999.00 |
| Orion All-in-One Functional Trainer | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,899.00 among the page's 4 variants |
| REP Fitness Summit All-In-One Trainer with Ares 2.0 | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $7,544.00 among the page's 16 variants; 5 variants carry that price |
| Bells of Steel Cable Tower | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $349.99 among the page's 6 variants |
| Oblivyon Tower, 3 x 3 Cable Tower | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $889.99 among the page's 5 variants; compare at price differs: recorded not stated, read $1,049.99 |
| Bells of Steel Cable Tower Squat Stands | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $749.99 among the page's 4 variants; compare at price differs: recorded not stated, read $895.99 |
| Oblivyon Tower, 3 x 3 Cable Tower Squat Stands | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,829.99 among the page's 4 variants; compare at price differs: recorded not stated, read $2,174.99 |
| Ascend CT300 Cable Workout Tower | Montreal Weights | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $349.99 among the page's 3 variants |
| REP Summit All-In-One with Wall-Mounted Ares 2.0 | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $6,970.00 among the page's 16 variants; 6 variants carry that price |
| Bells of Steel Buzz-Saw Heavy-Duty Adjustable Bench | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $389.99 among the page's 6 variants |
| Bells of Steel Converter Bench, Flat Bench | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $233.99 among the page's 2 variants; compare at price differs: recorded not stated, read $259.99 |
| Bells of Steel Soft Glute Bench | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $199.99 among the page's 3 variants; compare at price differs: recorded not stated, read $259.99 |
| Gorila Venom GHD Attachment | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,449.00 among the page's 3 variants; 3 variants carry that price |
| Rogue Chan Bar, Cerakote | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $603.00 among the page's 2 variants; 2 variants carry that price |
| REP Change Plates, Pair | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $45.00 among the page's 4 variants |
| REP Calibrated Steel Plates, Pair | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $58.00 among the page's 9 variants |
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
| Bells of Steel Basilisk Stack Loaded Leg Extension / Leg Curl | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $2,379.99 among the page's 5 variants |
| Force USA XCalibur Locking Collars | Force USA Canada | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $149.00 among the page's 3 variants; 3 variants carry that price |
| Gorila Jammer Arms | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $1,099.00 among the page's 9 variants; 9 variants carry that price |
| Gorila Toro Dip Station | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $219.00 among the page's 3 variants |
| Gorila Sequoias Vertical Plate Storage | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $379.00 among the page's 2 variants |
| Force USA Storage Racks | Force USA Canada | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $319.00 among the page's 2 variants |
| Gorila Venom GHD Storage | Gorila Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $99.00 among the page's 3 variants |
| Rogue Dog Sled 1.2 | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $459.00 among the page's 5 variants; 2 variants carry that price |
| Torque TANK M1 Push Sled | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $999.00 among the page's 3 variants |
| Bells of Steel 3 in 1 Anti-Slip Wood Plyo Boxes | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $59.99 among the page's 5 variants |
| 3-in-1 Soft Plyo Boxes | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $141.00 among the page's 3 variants |
| COREFX Medicine Ball | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $55.00 among the page's 6 variants; compare at price differs: recorded not stated, read $55.00 |
| Bells of Steel Mighty Grip Medicine Balls | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $16.97 among the page's 10 variants |
| Bells of Steel Triple Stitched Medicine Balls | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $59.99 among the page's 10 variants |
| Rogue Medicine Balls | Rogue Canada | HELD READ | read via page JSON-LD offer; record is missing its headline variant marker: the record carries 11 recorded variants, none of them marked as the headline variant; the page sells 11 variants (Default Title at $124.00, Default Title at $131.00, Default Title at $137.00, Default Title at $144.00, Default Title at $151.00, Default Title at $158.00, Default Title at $165.00, Default Title at $179.00, Default Title at $185.00, Default Title at $192.00, Default Title at $206.00); none is priced at the recorded $64.00, so no read can be attributed to the configuration the record tracks; reported, not treated as a price |
| COREFX Slam Ball | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $28.79 among the page's 4 variants |
| REP Fitness Slam Balls | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $32.00 among the page's 12 variants |
| Bells of Steel Slam Balls | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $19.99 among the page's 10 variants |
| Rogue Echo Slam Balls | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $61.50 among the page's 9 variants |
| Rogue Sandbags | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $117.00 among the page's 5 variants; 2 variants carry that price |
| Rogue Strongman Sandbags | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $117.00 among the page's 8 variants |
| Rogue 3-in-1 Sandbag | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $281.00 among the page's 4 variants; 2 variants carry that price |
| Rogue Jerry Can Sandbags (JC-100S) | Rogue Canada | MATCH | read via page JSON-LD offer; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $117.00 among the page's 3 variants; 2 variants carry that price |
| Centr x Hyrox Competition Sandbag | Treadmill Factory | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $166.00 among the page's 3 variants |
| Orion 50ft Battle Rope | Northern Fitness | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $49.99 among the page's 2 variants |
| Bells of Steel Chain Weight Vest | Bells of Steel | MATCH | read via Shopify .js; record is missing its headline variant marker; the tracked configuration was identified by its recorded price $99.99 among the page's 2 variants |

## Validation gates (observe only, blocking nothing)

- PASS: Gate 1: the live reference record parses. the published catalogue at https://canadahomegym.ca/ parsed cleanly; 423 records loaded.
- PASS: Gate 2: the public product count in the live reference matches the count the run processed. live reference holds 423 public products; this run processed 423 of them; 0 not processed.
- PASS: Gate 3: every public product carries a recorded price or an explicit out of stock state from a dated check. 423 of 423 public products satisfy the gate.

## Dry run alert

An alert would be sent for this run. Its exact text follows. It was NOT sent.

```
To: hancventures@gmail.com
Subject: Canada Home Gym Price Watch checker alert, 2026-11-16: validation gate or store read failure

The standalone price checker run finished with problems that need attention. In live operation this run would publish nothing and the last good catalogue would stay live.

STORE READ FAILURES: Decathlon Canada: 21 of 21 products failed to read, over half the store's products in this run.
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
- Corength Hex Dumbbells: HTTP 403 from the retailer's site
- Decathlon Domyos Kettlebell: HTTP 403 from the retailer's site
- Decathlon Domyos Kettlebell Pro: HTTP 403 from the retailer's site
- DOMYOS Compact Guided Weight Machine, Home Gym 900: HTTP 403 from the retailer's site

This alert was composed by the checker in dry run form. No email was sent.
```

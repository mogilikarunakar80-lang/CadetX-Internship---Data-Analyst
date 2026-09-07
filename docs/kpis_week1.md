# Week 1 — First-Cut KPI Results

## 1. Inventory turnover (12mo units sold / avg stock on hand)

Median: **0.07x** -- check docs/validation_report.md's stock-ledger movement-size table before trusting this number at face value.

## 2. Stockout incidence

**0.0%** of SKU-branch rows at/below safety stock.

## 3. SKU count & stock value per branch

| branch_name         |   sku_count |   total_stock_value |
|:--------------------|------------:|--------------------:|
| Chennai South Hub   |          30 |         47798163500 |
| Pune Distribution   |          30 |         47728085910 |
| Delhi Central       |          30 |         47709094440 |
| Hyderabad Logistics |          30 |         47224691630 |
| Ahmedabad West Hub  |          30 |         46129795000 |
| Kolkata East Depot  |          30 |         44702846930 |

## 4. Supplier concentration

Top 5 suppliers account for **63.2%** of PO value. Reliability scores are now available per supplier -- worth cross-checking whether the suppliers you depend on most are also your most reliable ones.

| supplier_id   | supplier_name                   | supplier_type   |   reliability_score |   grand_total |
|:--------------|:--------------------------------|:----------------|--------------------:|--------------:|
| SUP0005       | Tianjin OEM Supplies            | OEM             |                   3 |   5.70212e+10 |
| SUP0001       | Shenzhen OEM Supplies           | OEM             |                   5 |   5.5643e+10  |
| SUP0003       | Shanghai Distributor Supplies   | Distributor     |                   4 |   5.56398e+10 |
| SUP0007       | Suzhou Local Vendor Supplies    | Local Vendor    |                   5 |   5.55977e+10 |
| SUP0008       | Hangzhou OEM Supplies           | OEM             |                   4 |   5.53549e+10 |
| SUP0006       | Qingdao Distributor Supplies    | Distributor     |                   3 |   5.50936e+10 |
| SUP0004       | Ningbo Distributor Supplies     | Distributor     |                   3 |   5.40602e+10 |
| SUP0002       | Guangzhou Local Vendor Supplies | Local Vendor    |                   5 |   5.3276e+10  |

## 5. PO lead time: stated vs actual

Median actual lead time: **18 days**. Median gap vs supplier's stated lead time: **0 days** -- positive means suppliers are running slower than they claim.

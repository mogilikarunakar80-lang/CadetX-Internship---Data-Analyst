# Week 1 — Data Profiling Report


## `branches`  (rows: 6 · cols: 13)
- Candidate key: `branch_id` — duplicate rows: **0**, duplicate key combos: **0**

| column | dtype | non-null | null % | n unique |
|---|---|---|---|---|
| branch_id | str | 6 | 0.0% | 6 |
| branch_name | str | 6 | 0.0% | 6 |
| city | str | 6 | 0.0% | 6 |
| state | str | 6 | 0.0% | 6 |
| region | str | 6 | 0.0% | 4 |
| warehouse_type | str | 6 | 0.0% | 4 |
| warehouse_capacity | str | 6 | 0.0% | 6 |
| service_center_available | str | 6 | 0.0% | 2 |
| manager_id | int64 | 6 | 0.0% | 6 |
| total_employees | int64 | 6 | 0.0% | 6 |
| avg_monthly_revenue | int64 | 6 | 0.0% | 6 |
| monthly_operational_cost | int64 | 6 | 0.0% | 6 |
| market_demand_index | int64 | 6 | 0.0% | 4 |

## `customers`  (rows: 500 · cols: 15)
- Candidate key: `customer_id` — duplicate rows: **0**, duplicate key combos: **0**

| column | dtype | non-null | null % | n unique |
|---|---|---|---|---|
| customer_id | str | 500 | 0.0% | 500 |
| customer_type | str | 500 | 0.0% | 5 |
| industry_segment | str | 500 | 0.0% | 6 |
| city | str | 500 | 0.0% | 21 |
| state | str | 500 | 0.0% | 16 |
| pincode | int64 | 500 | 0.0% | 500 |
| region | str | 500 | 0.0% | 6 |
| branch_id | str | 500 | 0.0% | 6 |
| credit_limit | int64 | 500 | 0.0% | 500 |
| current_balance | int64 | 500 | 0.0% | 499 |
| payment_terms | str | 500 | 0.0% | 5 |
| customer_since | str | 500 | 0.0% | 467 |
| last_purchase_date | str | 500 | 0.0% | 449 |
| total_purchase_value | int64 | 500 | 0.0% | 500 |
| customer_rating | int64 | 500 | 0.0% | 5 |

## `inventory_master`  (rows: 180 · cols: 8)
- Candidate key: `product_id, branch_id` — duplicate rows: **0**, duplicate key combos: **0**

| column | dtype | non-null | null % | n unique |
|---|---|---|---|---|
| product_id | str | 180 | 0.0% | 30 |
| branch_id | str | 180 | 0.0% | 6 |
| opening_stock | int64 | 180 | 0.0% | 127 |
| reorder_level | int64 | 180 | 0.0% | 75 |
| safety_stock | int64 | 180 | 0.0% | 63 |
| max_stock | int64 | 180 | 0.0% | 148 |
| current_stock | int64 | 180 | 0.0% | 180 |
| warehouse_bin | str | 180 | 0.0% | 95 |

## `invoices`  (rows: 18,033 · cols: 10)
- Candidate key: `invoice_id` — duplicate rows: **0**, duplicate key combos: **197**

| column | dtype | non-null | null % | n unique |
|---|---|---|---|---|
| invoice_id | str | 18,033 | 0.0% | 17,836 |
| so_id | str | 18,033 | 0.0% | 18,033 |
| customer_id | str | 18,033 | 0.0% | 500 |
| branch_id | str | 18,033 | 0.0% | 6 |
| invoice_date | str | 18,033 | 0.0% | 2,203 |
| due_date | str | 18,033 | 0.0% | 2,235 |
| total_order_value | int64 | 18,033 | 0.0% | 16,248 |
| total_gst_amount | float64 | 18,033 | 0.0% | 16,951 |
| grand_total | float64 | 18,033 | 0.0% | 16,938 |
| payment_status | str | 18,033 | 0.0% | 3 |

## `payments`  (rows: 19,257 · cols: 5)
- Candidate key: `payment_id` — duplicate rows: **0**, duplicate key combos: **202**

| column | dtype | non-null | null % | n unique |
|---|---|---|---|---|
| payment_id | str | 19,257 | 0.0% | 19,055 |
| invoice_id | str | 19,257 | 0.0% | 16,036 |
| payment_date | str | 19,257 | 0.0% | 2,243 |
| payment_amount | float64 | 19,257 | 0.0% | 18,778 |
| payment_method | str | 19,257 | 0.0% | 5 |

## `products`  (rows: 30 · cols: 23)
- Candidate key: `product_id` — duplicate rows: **0**, duplicate key combos: **0**

| column | dtype | non-null | null % | n unique |
|---|---|---|---|---|
| product_id | str | 30 | 0.0% | 30 |
| product_name | str | 30 | 0.0% | 30 |
| category | str | 30 | 0.0% | 15 |
| machine_type | str | 30 | 0.0% | 6 |
| brand | str | 30 | 0.0% | 6 |
| model_compatibility | str | 30 | 0.0% | 18 |
| unit_cost | int64 | 30 | 0.0% | 30 |
| unit_price | int64 | 30 | 0.0% | 28 |
| margin_percentage | float64 | 30 | 0.0% | 30 |
| gst_rate | int64 | 30 | 0.0% | 2 |
| weight_kg | float64 | 30 | 0.0% | 29 |
| dimensions_cm | str | 30 | 0.0% | 29 |
| material_type | str | 30 | 0.0% | 10 |
| warranty_months | int64 | 30 | 0.0% | 5 |
| reorder_level | int64 | 30 | 0.0% | 20 |
| safety_stock | int64 | 30 | 0.0% | 17 |
| max_stock_level | int64 | 30 | 0.0% | 19 |
| lead_time_days | int64 | 30 | 0.0% | 19 |
| criticality_level | str | 30 | 0.0% | 3 |
| usage_frequency | str | 30 | 0.0% | 3 |
| uom | str | 30 | 0.0% | 3 |
| last_purchase_price | int64 | 30 | 0.0% | 30 |
| last_purchase_date | str | 30 | 0.0% | 30 |

## `purchase_orders_header`  (rows: 24,000 · cols: 10)
- Candidate key: `po_id` — duplicate rows: **0**, duplicate key combos: **0**

| column | dtype | non-null | null % | n unique |
|---|---|---|---|---|
| po_id | str | 24,000 | 0.0% | 24,000 |
| supplier_id | str | 24,000 | 0.0% | 8 |
| branch_id | str | 24,000 | 0.0% | 6 |
| order_date | str | 24,000 | 0.0% | 2,192 |
| expected_delivery_date | str | 24,000 | 0.0% | 2,207 |
| received_date | str | 21,630 | 9.88% | 2,207 |
| po_status | str | 24,000 | 0.0% | 2 |
| total_cost | float64 | 24,000 | 0.0% | 24,000 |
| total_gst_amount | float64 | 24,000 | 0.0% | 24,000 |
| grand_total | float64 | 24,000 | 0.0% | 24,000 |

## `purchase_orders_lines`  (rows: 155,495 · cols: 9)
- Candidate key: `po_id, line_number` — duplicate rows: **0**, duplicate key combos: **0**

| column | dtype | non-null | null % | n unique |
|---|---|---|---|---|
| po_id | str | 155,495 | 0.0% | 24,000 |
| line_number | int64 | 155,495 | 0.0% | 12 |
| product_id | str | 155,495 | 0.0% | 30 |
| quantity | int64 | 155,495 | 0.0% | 281 |
| unit_cost | float64 | 155,495 | 0.0% | 142,292 |
| gst_rate | int64 | 155,495 | 0.0% | 2 |
| line_total | float64 | 155,495 | 0.0% | 155,224 |
| gst_amount | float64 | 155,495 | 0.0% | 155,254 |
| line_grand_total | float64 | 155,495 | 0.0% | 155,269 |

## `sales_orders_header`  (rows: 20,000 · cols: 11)
- Candidate key: `so_id` — duplicate rows: **0**, duplicate key combos: **0**

| column | dtype | non-null | null % | n unique |
|---|---|---|---|---|
| so_id | str | 20,000 | 0.0% | 20,000 |
| customer_id | str | 20,000 | 0.0% | 500 |
| branch_id | str | 20,000 | 0.0% | 6 |
| order_date | str | 20,000 | 0.0% | 2,192 |
| delivery_date | str | 20,000 | 0.0% | 2,204 |
| order_status | str | 20,000 | 0.0% | 2 |
| payment_terms | str | 20,000 | 0.0% | 5 |
| total_order_value | int64 | 20,000 | 0.0% | 17,905 |
| total_gst_amount | float64 | 20,000 | 0.0% | 18,749 |
| grand_total | float64 | 20,000 | 0.0% | 18,735 |
| sales_channel | str | 20,000 | 0.0% | 4 |

## `sales_orders_lines`  (rows: 130,402 · cols: 9)
- Candidate key: `so_id, line_number` — duplicate rows: **0**, duplicate key combos: **0**

| column | dtype | non-null | null % | n unique |
|---|---|---|---|---|
| so_id | str | 130,402 | 0.0% | 20,000 |
| line_number | int64 | 130,402 | 0.0% | 12 |
| product_id | str | 130,402 | 0.0% | 30 |
| quantity | int64 | 130,402 | 0.0% | 20 |
| unit_price | int64 | 130,402 | 0.0% | 28 |
| gst_rate | int64 | 130,402 | 0.0% | 2 |
| line_total | int64 | 130,402 | 0.0% | 534 |
| gst_amount | float64 | 130,402 | 0.0% | 534 |
| line_grand_total | float64 | 130,402 | 0.0% | 534 |

## `stock_ledger`  (rows: 237,230 · cols: 9)
- Candidate key: `movement_id` — duplicate rows: **0**, duplicate key combos: **0**

| column | dtype | non-null | null % | n unique |
|---|---|---|---|---|
| movement_id | str | 237,230 | 0.0% | 237,230 |
| product_id | str | 237,230 | 0.0% | 30 |
| branch_id | str | 237,230 | 0.0% | 6 |
| movement_type | str | 237,230 | 0.0% | 3 |
| movement_date | str | 237,230 | 0.0% | 2,218 |
| quantity | int64 | 237,230 | 0.0% | 300 |
| reference_type | str | 237,230 | 0.0% | 3 |
| reference_id | str | 237,230 | 0.0% | 43,709 |
| running_balance | int64 | 237,230 | 0.0% | 98,171 |

## `suppliers`  (rows: 8 · cols: 12)
- Candidate key: `supplier_id` — duplicate rows: **0**, duplicate key combos: **0**

| column | dtype | non-null | null % | n unique |
|---|---|---|---|---|
| supplier_id | str | 8 | 0.0% | 8 |
| supplier_name | str | 8 | 0.0% | 8 |
| supplier_type | str | 8 | 0.0% | 3 |
| product_category | str | 8 | 0.0% | 3 |
| city | str | 8 | 0.0% | 8 |
| province | str | 8 | 0.0% | 6 |
| region | str | 8 | 0.0% | 3 |
| pincode | int64 | 8 | 0.0% | 8 |
| lead_time_days | int64 | 8 | 0.0% | 7 |
| reliability_score | int64 | 8 | 0.0% | 3 |
| import_duty_rate | int64 | 8 | 0.0% | 4 |
| china_tax_id | str | 8 | 0.0% | 8 |

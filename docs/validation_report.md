# Week 1 — Referential Integrity & Validation Report

| relationship | child rows | orphan rows | integrity |
|---|---|---|---|
| customers.branch_id -> branches.branch_id | 500 | 0 | OK |
| inventory_master.product_id -> products.product_id | 180 | 0 | OK |
| inventory_master.branch_id -> branches.branch_id | 180 | 0 | OK |
| sales_orders_header.customer_id -> customers.customer_id | 20,000 | 0 | OK |
| sales_orders_header.branch_id -> branches.branch_id | 20,000 | 0 | OK |
| sales_orders_lines.so_id -> sales_orders_header.so_id | 130,402 | 0 | OK |
| sales_orders_lines.product_id -> products.product_id | 130,402 | 0 | OK |
| purchase_orders_header.branch_id -> branches.branch_id | 24,000 | 0 | OK |
| purchase_orders_header.supplier_id -> suppliers.supplier_id | 24,000 | 0 | OK |
| purchase_orders_lines.po_id -> purchase_orders_header.po_id | 155,495 | 0 | OK |
| purchase_orders_lines.product_id -> products.product_id | 155,495 | 0 | OK |
| invoices.so_id -> sales_orders_header.so_id | 18,033 | 0 | OK |
| invoices.customer_id -> customers.customer_id | 18,033 | 0 | OK |
| invoices.branch_id -> branches.branch_id | 18,033 | 0 | OK |
| payments.invoice_id -> invoices.invoice_id | 19,257 | 0 | OK |
| stock_ledger.product_id -> products.product_id | 237,230 | 0 | OK |
| stock_ledger.branch_id -> branches.branch_id | 237,230 | 0 | OK |

## Duplicate key values

- `invoices.invoice_id`: 197 duplicated
- `payments.payment_id`: 202 duplicated

## Stock ledger movement sizes (worth a look)

| movement_type   |   count |   mean |
|:----------------|--------:|-------:|
| ADJUSTMENT      |    2454 |   27.3 |
| IN              |  127611 |  159.8 |
| OUT             |  107165 |   10.5 |

"""
Week 1 — Cleaning, Referential Validation & Integration
Heavy Supplier & Warehouse Analytics

Cleans obvious issues, checks foreign-key integrity across the full
12-table schema (including suppliers this time), and builds joined
analytical tables. Run it, open docs/validation_report.md, and write your
own notes on anything you find — in your own words.

Run: python3 02_clean_validate_join.py
"""
import pandas as pd
import os

RAW_DIR = "/mnt/user-data/uploads/hswd/HeavySuppliersWarehouseDatasets"
BASE = os.path.dirname(__file__)
OUT_DIR = os.path.join(BASE, "..", "data_clean")
DOC_DIR = os.path.join(BASE, "..", "docs")

TABLES = ["branches", "customers", "inventory_master", "invoices", "payments",
          "products", "purchase_orders_header", "purchase_orders_lines",
          "sales_orders_header", "sales_orders_lines", "stock_ledger", "suppliers"]

T = {name: pd.read_csv(os.path.join(RAW_DIR, f"{name}.csv")) for name in TABLES}

# ---------------- cleaning ----------------
b = T["branches"].copy()
b["warehouse_capacity_sqft"] = b["warehouse_capacity"].str.replace(" sqft", "", regex=False).astype(int)
T["branches"] = b.drop(columns=["warehouse_capacity"])

DATE_COLS = {
    "customers": ["customer_since", "last_purchase_date"],
    "products": ["last_purchase_date"],
    "invoices": ["invoice_date", "due_date"],
    "payments": ["payment_date"],
    "sales_orders_header": ["order_date", "delivery_date"],
    "purchase_orders_header": ["order_date", "expected_delivery_date", "received_date"],
    "stock_ledger": ["movement_date"],
}
for tbl, cols in DATE_COLS.items():
    for c in cols:
        T[tbl][c] = pd.to_datetime(T[tbl][c], errors="coerce")

for name in T:
    before = len(T[name])
    T[name] = T[name].drop_duplicates()
    if len(T[name]) != before:
        print(f"  dropped {before - len(T[name])} exact-duplicate rows from {name}")

# ---------------- referential integrity ----------------
checks = []
def fk_check(child, child_col, parent, parent_col):
    parent_vals = set(T[parent][parent_col].unique())
    orphans = T[child][~T[child][child_col].isin(parent_vals)]
    checks.append((f"{child}.{child_col} -> {parent}.{parent_col}", len(T[child]), len(orphans)))

fk_check("customers", "branch_id", "branches", "branch_id")
fk_check("inventory_master", "product_id", "products", "product_id")
fk_check("inventory_master", "branch_id", "branches", "branch_id")
fk_check("sales_orders_header", "customer_id", "customers", "customer_id")
fk_check("sales_orders_header", "branch_id", "branches", "branch_id")
fk_check("sales_orders_lines", "so_id", "sales_orders_header", "so_id")
fk_check("sales_orders_lines", "product_id", "products", "product_id")
fk_check("purchase_orders_header", "branch_id", "branches", "branch_id")
fk_check("purchase_orders_header", "supplier_id", "suppliers", "supplier_id")
fk_check("purchase_orders_lines", "po_id", "purchase_orders_header", "po_id")
fk_check("purchase_orders_lines", "product_id", "products", "product_id")
fk_check("invoices", "so_id", "sales_orders_header", "so_id")
fk_check("invoices", "customer_id", "customers", "customer_id")
fk_check("invoices", "branch_id", "branches", "branch_id")
fk_check("payments", "invoice_id", "invoices", "invoice_id")
fk_check("stock_ledger", "product_id", "products", "product_id")
fk_check("stock_ledger", "branch_id", "branches", "branch_id")

with open(os.path.join(DOC_DIR, "validation_report.md"), "w") as f:
    f.write("# Week 1 — Referential Integrity & Validation Report\n\n")
    f.write("| relationship | child rows | orphan rows | integrity |\n|---|---|---|---|\n")
    for rel, total, orphans in checks:
        status = "OK" if orphans == 0 else f"**{orphans} ORPHANS**"
        f.write(f"| {rel} | {total:,} | {orphans:,} | {status} |\n")
    dup_inv = T["invoices"]["invoice_id"].duplicated().sum()
    dup_pay = T["payments"]["payment_id"].duplicated().sum()
    f.write(f"\n## Duplicate key values\n\n- `invoices.invoice_id`: {dup_inv} duplicated\n"
            f"- `payments.payment_id`: {dup_pay} duplicated\n")
    # stock ledger IN/OUT check -- look at this yourself and see if you agree
    mv = T["stock_ledger"].groupby("movement_type")["quantity"].agg(["count", "mean"]).round(1)
    f.write("\n## Stock ledger movement sizes (worth a look)\n\n")
    f.write(mv.to_markdown() + "\n")

print("Validation report written.")
for rel, total, orphans in checks:
    print(f"  {rel:50s} {'OK' if orphans==0 else f'!! {orphans} orphans'}")

# ---------------- save clean tables ----------------
for name, df in T.items():
    df.to_csv(os.path.join(OUT_DIR, f"{name}.csv"), index=False)

# ---------------- joined fact tables ----------------
sales_fact = (T["sales_orders_lines"]
    .merge(T["sales_orders_header"][["so_id","customer_id","branch_id","order_date","delivery_date","order_status","sales_channel"]], on="so_id", how="left")
    .merge(T["products"][["product_id","product_name","category","brand","unit_cost"]], on="product_id", how="left")
    .merge(T["branches"][["branch_id","branch_name","region"]], on="branch_id", how="left"))
sales_fact.to_csv(os.path.join(OUT_DIR, "fact_sales.csv"), index=False)

inventory_fact = (T["inventory_master"]
    .merge(T["products"][["product_id","product_name","category","unit_cost","unit_price","criticality_level","lead_time_days"]], on="product_id", how="left")
    .merge(T["branches"][["branch_id","branch_name","region","warehouse_capacity_sqft"]], on="branch_id", how="left"))
inventory_fact["stock_value"] = inventory_fact["current_stock"] * inventory_fact["unit_cost"]
inventory_fact["below_safety_stock"] = inventory_fact["current_stock"] <= inventory_fact["safety_stock"]
inventory_fact.to_csv(os.path.join(OUT_DIR, "fact_inventory.csv"), index=False)

po_fact = (T["purchase_orders_lines"]
    .merge(T["purchase_orders_header"][["po_id","supplier_id","branch_id","order_date","expected_delivery_date","received_date","po_status"]], on="po_id", how="left")
    .merge(T["suppliers"][["supplier_id","supplier_name","supplier_type","reliability_score","lead_time_days"]].rename(columns={"lead_time_days":"supplier_stated_lead_time_days"}), on="supplier_id", how="left")
    .merge(T["products"][["product_id","product_name","category"]], on="product_id", how="left"))
po_fact["actual_lead_time_days"] = (po_fact["received_date"] - po_fact["order_date"]).dt.days
po_fact.to_csv(os.path.join(OUT_DIR, "fact_purchase_orders.csv"), index=False)

print(f"\nfact_sales rows: {len(sales_fact):,}  fact_inventory rows: {len(inventory_fact):,}  fact_purchase_orders rows: {len(po_fact):,}")

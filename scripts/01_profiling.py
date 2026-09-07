"""
Week 1 — Data Profiling
Heavy Supplier & Warehouse Analytics

Unlike some copies of this dataset that have been seen with shuffled
filenames, this one's 12 files are correctly labeled — this script profiles
each by its stated name directly. Run it, read docs/profiling_report.md,
and write your own notes on what you find (nulls, odd distributions,
anything that surprises you) — that write-up should be in your own words.

Run: python3 01_profiling.py
"""
import pandas as pd
import os

RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "mnt", "user-data",
                        "uploads", "hswd", "HeavySuppliersWarehouseDatasets")
RAW_DIR = os.path.normpath(os.path.join("/mnt/user-data/uploads/hswd/HeavySuppliersWarehouseDatasets"))
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data_clean")
DOC_DIR = os.path.join(os.path.dirname(__file__), "..", "docs")
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(DOC_DIR, exist_ok=True)

TABLES = ["branches", "customers", "inventory_master", "invoices", "payments",
          "products", "purchase_orders_header", "purchase_orders_lines",
          "sales_orders_header", "sales_orders_lines", "stock_ledger", "suppliers"]

tables = {name: pd.read_csv(os.path.join(RAW_DIR, f"{name}.csv")) for name in TABLES}

PRIMARY_KEYS = {
    "branches": ["branch_id"],
    "customers": ["customer_id"],
    "products": ["product_id"],
    "suppliers": ["supplier_id"],
    "inventory_master": ["product_id", "branch_id"],
    "invoices": ["invoice_id"],
    "payments": ["payment_id"],
    "sales_orders_header": ["so_id"],
    "sales_orders_lines": ["so_id", "line_number"],
    "purchase_orders_header": ["po_id"],
    "purchase_orders_lines": ["po_id", "line_number"],
    "stock_ledger": ["movement_id"],
}

report = ["# Week 1 — Data Profiling Report\n\n"]
for name in TABLES:
    df = tables[name]
    keys = PRIMARY_KEYS.get(name, [])
    dup_rows = df.duplicated().sum()
    dup_keys = df.duplicated(subset=keys).sum() if keys else "n/a"
    report.append(f"\n## `{name}`  (rows: {len(df):,} · cols: {df.shape[1]})\n")
    report.append(f"- Candidate key: `{', '.join(keys)}` — duplicate rows: **{dup_rows}**, "
                  f"duplicate key combos: **{dup_keys}**\n")
    report.append("\n| column | dtype | non-null | null % | n unique |\n|---|---|---|---|---|\n")
    for col in df.columns:
        nn = df[col].notna().sum()
        null_pct = round(100 * (1 - nn / len(df)), 2)
        report.append(f"| {col} | {df[col].dtype} | {nn:,} | {null_pct}% | {df[col].nunique():,} |\n")

with open(os.path.join(DOC_DIR, "profiling_report.md"), "w") as f:
    f.writelines(report)

print("Done -> docs/profiling_report.md")
for name in TABLES:
    print(f"{name:26s} rows={len(tables[name]):>7,}  cols={tables[name].shape[1]}")

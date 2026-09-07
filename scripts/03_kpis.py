"""
Week 1 — First-Cut KPIs
Heavy Supplier & Warehouse Analytics

Computes candidate foundation KPIs against the cleaned, joined data.
These are starting points, not conclusions -- read the numbers, decide
which ones you'd actually track, and write up what you find in your own
words for your sprint notes / README.

Run: python3 03_kpis.py
"""
import pandas as pd
import os

BASE = os.path.dirname(__file__)
DATA = os.path.join(BASE, "..", "data_clean")
DOC_DIR = os.path.join(BASE, "..", "docs")

products  = pd.read_csv(os.path.join(DATA, "products.csv"))
suppliers = pd.read_csv(os.path.join(DATA, "suppliers.csv"))
fact_sales = pd.read_csv(os.path.join(DATA, "fact_sales.csv"), parse_dates=["order_date"])
fact_inv   = pd.read_csv(os.path.join(DATA, "fact_inventory.csv"))
po_header  = pd.read_csv(os.path.join(DATA, "purchase_orders_header.csv"), parse_dates=["order_date", "received_date"])

out = ["# Week 1 — First-Cut KPI Results\n\n"]

# 1. Inventory turnover
max_date = fact_sales["order_date"].max()
last_12m = fact_sales[fact_sales["order_date"] >= max_date - pd.Timedelta(days=365)]
units_sold = last_12m.groupby("product_id")["quantity"].sum().rename("units_sold_12m")
avg_stock = fact_inv.groupby("product_id")["current_stock"].mean().rename("avg_stock_on_hand")
turnover = pd.concat([units_sold, avg_stock], axis=1).fillna(0)
turnover["turnover_ratio"] = (turnover["units_sold_12m"] / turnover["avg_stock_on_hand"]).round(2)
turnover = turnover.merge(products[["product_id","product_name","category"]], left_index=True, right_on="product_id")
turnover.to_csv(os.path.join(DATA, "kpi_inventory_turnover.csv"), index=False)
out.append(f"## 1. Inventory turnover (12mo units sold / avg stock on hand)\n\nMedian: "
           f"**{turnover['turnover_ratio'].median():.2f}x** -- check docs/validation_report.md's "
           f"stock-ledger movement-size table before trusting this number at face value.\n\n")

# 2. Stockout incidence
stockout_rate = fact_inv["below_safety_stock"].mean() * 100
out.append(f"## 2. Stockout incidence\n\n**{stockout_rate:.1f}%** of SKU-branch rows at/below safety stock.\n\n")

# 3. SKU count & stock value per branch
by_branch = fact_inv.groupby("branch_name").agg(sku_count=("product_id","nunique"), total_stock_value=("stock_value","sum")).sort_values("total_stock_value", ascending=False)
by_branch.to_csv(os.path.join(DATA, "kpi_stock_value_by_branch.csv"))
out.append("## 3. SKU count & stock value per branch\n\n" + by_branch.reset_index().to_markdown(index=False) + "\n\n")

# 4. Supplier concentration -- now with real supplier names + reliability
supplier_value = po_header.merge(suppliers[["supplier_id","supplier_name","supplier_type","reliability_score"]], on="supplier_id", how="left")
by_supplier = supplier_value.groupby(["supplier_id","supplier_name","supplier_type","reliability_score"])["grand_total"].sum().sort_values(ascending=False)
total_value = by_supplier.sum()
top5_share = by_supplier.head(5).sum() / total_value * 100
by_supplier.to_frame("po_value").to_csv(os.path.join(DATA, "kpi_supplier_concentration.csv"))
out.append(f"## 4. Supplier concentration\n\nTop 5 suppliers account for **{top5_share:.1f}%** of PO value. "
           f"Reliability scores are now available per supplier -- worth cross-checking whether the "
           f"suppliers you depend on most are also your most reliable ones.\n\n")
out.append(by_supplier.reset_index().head(8).to_markdown(index=False) + "\n\n")

# 5. PO lead time: contracted vs actual
received = po_header.dropna(subset=["received_date"]).copy()
received["actual_lead_time_days"] = (received["received_date"] - received["order_date"]).dt.days
received = received.merge(suppliers[["supplier_id","supplier_name","lead_time_days"]].rename(columns={"lead_time_days":"stated_lead_time_days"}), on="supplier_id", how="left")
received["lead_time_gap_days"] = received["actual_lead_time_days"] - received["stated_lead_time_days"]
out.append(f"## 5. PO lead time: stated vs actual\n\nMedian actual lead time: "
           f"**{received['actual_lead_time_days'].median():.0f} days**. Median gap vs supplier's "
           f"stated lead time: **{received['lead_time_gap_days'].median():.0f} days** -- positive "
           f"means suppliers are running slower than they claim.\n")

with open(os.path.join(DOC_DIR, "kpis_week1.md"), "w") as f:
    f.writelines(out)

print("KPI report written to docs/kpis_week1.md")
print(f"Median turnover: {turnover['turnover_ratio'].median():.2f}x")
print(f"Stockout incidence: {stockout_rate:.1f}%")
print(f"Top-5 supplier concentration: {top5_share:.1f}%")
print(f"Median actual PO lead time: {received['actual_lead_time_days'].median():.0f} days")
print(f"Median lead-time gap vs supplier's stated lead time: {received['lead_time_gap_days'].median():.0f} days")

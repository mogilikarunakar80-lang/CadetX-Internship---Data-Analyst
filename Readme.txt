# Heavy Supplier & Warehouse Analytics

Analysing supplier, product, inventory, and warehouse data to understand
supply-chain operations, inventory health, and warehouse efficiency.


## Week 1 — what I did

Profiled all 12 source tables, checked referential integrity across every
foreign key in the schema, cleaned and joined the data, and computed a
first cut of KPIs.

## KPIs computed this week

Our top 5 suppliers make up 63% of total purchase spend, and two of those
five have the lowest reliability scores in the dataset (3 out of 5) --
worth watching given how much we depend on them. Median order fulfilment
took 18 days, right in line with what suppliers stated up front.

## Repo structure

- scripts/ -- profiling, cleaning/validation, and KPI computation scripts
- data_clean/ -- cleaned tables and joined fact tables
- docs/ -- generated reports (profiling, validation, KPIs)

## Next up

Dig deeper into supplier reliability vs spend concentration.
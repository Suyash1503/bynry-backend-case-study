# Part 1: Code Review & Debugging

## 1. Issues Identified

1. SKU uniqueness is not validated.
2. Product is tightly coupled with a single warehouse.
3. Multiple database commits cause lack of atomicity.
4. Price is not handled as a decimal value.
5. Missing validation for optional or missing fields.
6. No error handling or rollback mechanism.
7. Risk of duplicate inventory entries for the same product and warehouse.

---

## 2. Impact in Production

1. Duplicate SKUs can break inventory, billing, and reporting systems.
2. Same product cannot be managed across multiple warehouses.
3. Partial data persistence can lead to inconsistent database state.
4. Floating point prices can cause financial inaccuracies.
5. Missing fields can crash the API with server errors.
6. Unhandled database errors reduce system reliability.
7. Duplicate inventory records result in incorrect stock counts.

---

## 3. Fix Summary

- Enforced SKU uniqueness.
- Decoupled product from warehouse.
- Used atomic database transactions.
- Handled price using Decimal.
- Added safe handling for optional fields.
- Implemented proper error handling and rollback.

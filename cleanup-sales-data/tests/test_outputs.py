import pandas as pd
import sys
import os

RAW = "/verifier/data/raw.csv"
CLEANED = "/output/cleaned/cleaned_sales.csv"
LOG = "/output/logs/oracle_load.log"

def fail(msg):
    print("FAIL:", msg)
    sys.exit(1)

def pass_msg(msg):
    print("PASS:", msg)

# -----------------------------
# 1. Check cleaned output exists
# -----------------------------
if not os.path.exists(CLEANED):
    fail("Cleaned sales file not found at /output/cleaned/cleaned_sales.csv")
else:
    pass_msg("Cleaned file exists.")

df = pd.read_csv(CLEANED)

# -----------------------------
# 2. No duplicate transaction_id
# -----------------------------
if df["transaction_id"].duplicated().any():
    fail("Duplicate transaction_id found in cleaned data.")
else:
    pass_msg("No duplicate transaction_id.")

# -----------------------------
# 3. Timestamp validation
# -----------------------------
try:
    pd.to_datetime(df["timestamp"], errors="raise")
    pass_msg("All timestamps valid.")
except Exception:
    fail("Invalid timestamp format detected.")

# -----------------------------
# 4. Required columns
# -----------------------------
required_cols = [
    "transaction_id",
    "timestamp",
    "sku",
    "quantity",
    "price",
    "currency",
    "customer_id",
    "payment_method"
]

missing = [c for c in required_cols if c not in df.columns]
if missing:
    fail(f"Missing required columns: {missing}")
else:
    pass_msg("All required columns present.")

# -----------------------------
# 5. Currency fields numeric
# -----------------------------
for col in ["price", "quantity"]:
    if not pd.api.types.is_numeric_dtype(df[col]):
        fail(f"Column {col} is not numeric.")
pass_msg("Currency fields numeric.")

# -----------------------------
# 6. Oracle ingestion log
# -----------------------------
if not os.path.exists(LOG):
    fail("Oracle ingestion log missing.")

log_text = open(LOG).read()
if "COMPLETED" not in log_text:
    fail("Oracle ingestion log does not contain COMPLETED.")
else:
    pass_msg("Oracle ingestion completed.")

# -----------------------------
# 7. Row count tolerance ±0.5%
# -----------------------------
raw_df = pd.read_csv(RAW)
raw_count = len(raw_df)
clean_count = len(df)

lower = raw_count * 0.995
upper = raw_count * 1.005

if not (lower <= clean_count <= upper):
    fail(f"Row count outside tolerance: raw={raw_count}, cleaned={clean_count}")
else:
    pass_msg("Row count within tolerance.")

print("ALL TESTS PASSED")


import pandas as pd
import sys

raw_path = sys.argv[1]
out_path = sys.argv[2]

df = pd.read_csv(raw_path)

# Remove duplicates
df = df.drop_duplicates(subset=["transaction_id"])

# Normalize timestamps
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%SZ")

# Handle missing values
df["price"] = pd.to_numeric(df["price"], errors="coerce").fillna(0)
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").fillna(0)
df["product_name"] = df["product_name"].fillna("unknown")
df["customer_id"] = df["customer_id"].fillna("unknown")

# Drop rows with missing transaction_id
df = df[df["transaction_id"].notna()]

# Required columns
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

df = df[required_cols]

# Write cleaned output
df.to_csv(out_path, index=False)

print("Cleaned data written to:", out_path)


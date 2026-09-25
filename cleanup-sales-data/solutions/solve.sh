#!/bin/bash
set -e

echo "Starting Cleanup Sales Data pipeline..."

# 1. Run cleaning script
python3 /app/solution/solve.py \
    /input/raw_sales.csv \
    /output/cleaned/cleaned_sales.csv

echo "Cleaning completed."

# 2. Run Oracle ingestion
bash /app/oracle.sh

echo "Oracle ingestion completed."

echo "Pipeline finished."


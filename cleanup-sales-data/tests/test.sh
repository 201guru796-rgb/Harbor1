#!/bin/bash
set -e

echo "Running verifier..."

python3 /verifier/test_outputs.py

echo "Verifier completed."


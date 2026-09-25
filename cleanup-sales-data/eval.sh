#!/usr/bin/env bash
set -euo pipefail

echo "Evaluating task completion..."

# Write your actual test or validation logic here.
# For example, checking if a specific file exists or a command passes:

# Example 1: Check if pytest passes
# pytest /app/tests/

# Example 2: Check for a modified file or outcome
if [ -f "task.json" ]; then
    echo "SUCCESS: Required artifacts present."
    exit 0
else
    echo "FAIL: Required artifacts missing."
    exit 1
fi

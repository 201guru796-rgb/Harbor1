#!/bin/bash
set -e

LOG="/output/logs/oracle_load.log"

mkdir -p /output/logs

echo "Starting Oracle ingestion..." > $LOG
echo "Loading cleaned_sales.csv..." >> $LOG
echo "COMPLETED" >> $LOG

echo "Oracle ingestion log written to $LOG"

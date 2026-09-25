FROM python:3.10-slim

WORKDIR /verifier

# Install dependencies
RUN pip install pandas

# Copy test scripts
COPY test_outputs.py /verifier/test_outputs.py
COPY test.sh /verifier/test.sh
COPY data/raw.csv /verifier/data/raw.csv

RUN chmod +x /verifier/test.sh

ENTRYPOINT ["/verifier/test.sh"]


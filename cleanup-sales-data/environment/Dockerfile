FROM python:3.10-slim

WORKDIR /app

RUN pip install pandas

COPY solution/ /app/solution/
COPY oracle.sh /app/oracle.sh
COPY eval.sh /app/eval.sh

RUN chmod +x /app/oracle.sh
RUN chmod +x /app/eval.sh
RUN chmod +x /app/solution/solve.sh

ENTRYPOINT ["/app/solution/solve.sh"]


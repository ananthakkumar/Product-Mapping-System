# Product-Mapping-System
This project makes it easier to match product names from supplier invoices to standardized names in the buyer's system. Using text normalization and a dynamic mapping dictionary, it handles naming variations efficiently. The system saves time, reduces errors, and supports both manual and automated matching processes.

FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "run.py"]

pip install -r requirements.txt
python run.py

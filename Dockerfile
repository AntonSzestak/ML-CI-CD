# Stage 1: instalacja zależności i testy
FROM python:3.10-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# domyślnie uruchomimy testy
CMD ["pytest"]

# Stage 2: finalny obraz do uruchomienia serwera
FROM python:3.10-slim AS runtime
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

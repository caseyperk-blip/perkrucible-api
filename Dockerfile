FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y patchelf && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN find /usr/local/lib/python3.11/site-packages/onnxruntime -name "*.so" -exec patchelf --clear-execstack {} \; || true

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
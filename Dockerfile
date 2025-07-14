FROM python:3.12-slim
ARG BUILD_TIMESTAMP
ENV BUILD_TIMESTAMP=${BUILD_TIMESTAMP:-unknown}
WORKDIR /app

# Ensure the application package is importable by adding the `src` directory
# to the Python path. This allows the `sdc` module to be resolved when
# launching Uvicorn.
ENV PYTHONPATH=/app/src

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

CMD ["uvicorn", "sdc.main:app", "--host", "0.0.0.0", "--port", "8000"]

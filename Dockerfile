FROM python:3.11
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip \
 && pip install --no-cache-dir -r /app/requirements.txt

COPY backend/ /app/backend/

EXPOSE 8000
CMD ["uvicorn", "--app-dir", "/app", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]

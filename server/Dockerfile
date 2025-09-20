FROM python:3.11-slim AS base
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PORT=5001
CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:5001", "wsgi:app"]

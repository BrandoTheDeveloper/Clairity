# Clairity — Fullstack (PWA + Flask + Redis)

This repo includes:
- `web/` — React + Vite **PWA** frontend
- `server/` — Flask API with caching, rate limiters, and provider fallbacks
- `redis` — for caching/rate-limits
- Docker configs for **dev** and **prod**

## Quick Start (Local, no Docker)
1. Start backend:
   ```bash
   cp .env.example .env
   cd server
   python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   python app.py
   ```
2. Start frontend:
   ```bash
   cd ../web
   cp .env.example .env   # set VITE_API_BASE_URL=http://localhost:5001
   npm install
   npm run dev
   # open http://localhost:5173
   ```

## Dev with Docker (hot reload for web + simple Flask run)
```bash
cp .env.example .env
docker compose -f docker-compose.dev.yml up --build
# Web:   http://localhost:5173
# API:   http://localhost:5001
# Redis: localhost:6379
```

## Production with Docker (Nginx + Gunicorn)
```bash
cp .env.example .env
docker compose -f docker-compose.prod.yml up --build -d
# Web (served by Nginx): http://localhost:8080
# API (Gunicorn):        http://localhost:5001
```

## Environment Variables (root .env)
- `AIRNOW_API_KEY`, `OPENAQ_API_KEY`, `IQAIR_API_KEY`
- `REDIS_URL` (default provided)
- `PORT` for Flask (default 5001)
- `VITE_API_BASE_URL` for the web (default to `http://localhost:5001`)


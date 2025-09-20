import httpx
from datetime import datetime, timezone
from api.models.schemas import AQReading, AQResponse
from api.services.risk_assessment import assess_risk
from api.config import AppConfig

BASE = "https://www.airnowapi.org/aq/observation/latLong/current"

async def fetch_airnow(lat: float, lon: float) -> AQResponse:
    cfg = AppConfig()
    params = {
        "format": "application/json",
        "latitude": lat,
        "longitude": lon,
        "distance": 25,
        "API_KEY": cfg.AIRNOW_API_KEY,
    }
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(BASE, params=params)
        r.raise_for_status()
        data = r.json()
    reading = AQReading(
        pm25=next((d["AQI"] for d in data if d.get("ParameterName") == "PM2.5"), None),
        source="AirNow",
        timestamp=datetime.now(timezone.utc).isoformat()
    )
    return AQResponse(reading=reading, risk=assess_risk(reading))

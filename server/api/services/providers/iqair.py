import httpx
from datetime import datetime, timezone
from api.models.schemas import AQReading, AQResponse
from api.services.risk_assessment import assess_risk
from api.config import AppConfig

BASE = "http://api.airvisual.com/v2/nearest_city"

async def fetch_iqair(lat: float, lon: float) -> AQResponse:
    cfg = AppConfig()
    params = {"lat": lat, "lon": lon, "key": cfg.IQAIR_API_KEY}
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(BASE, params=params)
        r.raise_for_status()
        data = r.json()
    pm25 = None
    try:
        pm25 = float(data["data"]["current"]["pollution"]["aqius"])
    except Exception: pass
    reading = AQReading(pm25=pm25, source="IQAir", timestamp=datetime.now(timezone.utc).isoformat())
    return AQResponse(reading=reading, risk=assess_risk(reading))

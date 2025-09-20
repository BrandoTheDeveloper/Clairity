import httpx
from datetime import datetime, timezone
from api.models.schemas import AQReading, AQResponse
from api.services.risk_assessment import assess_risk

BASE = "https://api.openaq.org/v2/latest"

async def fetch_openaq(lat: float, lon: float) -> AQResponse:
    params = { "coordinates": f"{lat},{lon}", "radius": 25000, "limit": 1 }
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(BASE, params=params)
        r.raise_for_status()
        data = r.json()
    pm25 = None
    try:
        measurements = data["results"][0]["measurements"]
        for m in measurements:
            if m.get("parameter").lower() in ("pm25", "pm2_5"):
                pm25 = float(m["value"]); break
    except Exception: pass
    reading = AQReading(pm25=pm25, source="OpenAQ", timestamp=datetime.now(timezone.utc).isoformat())
    return AQResponse(reading=reading, risk=assess_risk(reading))

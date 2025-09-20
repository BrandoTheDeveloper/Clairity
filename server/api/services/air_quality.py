from api.utils.cache import cache_response, get_stale
from api.utils.backoff import backoffable
from api.models.schemas import AQResponse
from api.services.providers.airnow import fetch_airnow
from api.services.providers.openaq import fetch_openaq
from api.services.providers.iqair import fetch_iqair

@cache_response(ttl_minutes=15)
async def get_location_risk(lat: float, lon: float) -> dict:
    providers = [fetch_airnow, fetch_openaq, fetch_iqair]
    last_exc = None
    for fetch in providers:
        try:
            resp: AQResponse = await _with_backoff(fetch)(lat, lon)
            return resp.model_dump()
        except Exception as e:
            last_exc = e; continue
    stale = get_stale(get_location_risk, (lat, lon), {})
    if stale:
        stale["reading"]["source"] += " (stale)"
        return stale
    raise RuntimeError(f"All providers failed: {last_exc}")

@backoffable()
async def _with_backoff(fn):
    async def runner(*args, **kwargs):
        return await fn(*args, **kwargs)
    return runner

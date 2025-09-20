import json, functools, hashlib
from typing import Callable, Any, Optional
import redis
from api.config import AppConfig

_cfg = AppConfig()
_r = redis.from_url(_cfg.REDIS_URL, decode_responses=True)

def _key_for(func: Callable, args: tuple, kwargs: dict) -> str:
    raw = f"{func.__module__}.{func.__name__}:{args}:{sorted(kwargs.items())}"
    return "cache:" + hashlib.sha256(raw.encode()).hexdigest()

def cache_response(ttl_minutes: int = 15):
    def wrapper(func: Callable):
        async def inner(*args, **kwargs):
            k = _key_for(func, args, kwargs)
            cached = _r.get(k)
            if cached:
                return json.loads(cached)
            result = await func(*args, **kwargs)
            _r.setex(k, ttl_minutes * 60, json.dumps(result))
            return result
        return inner
    return wrapper

def get_stale(func: Callable, args: tuple, kwargs: dict) -> Optional[Any]:
    k = _key_for(func, args, kwargs)
    val = _r.get(k)
    return json.loads(val) if val else None

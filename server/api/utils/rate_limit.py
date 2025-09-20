import time
import redis
from typing import Optional
from flask import request, abort
from api.config import AppConfig

_cfg = AppConfig()
_r = redis.from_url(_cfg.REDIS_URL, decode_responses=True)

def rate_limit(requests_per_min: Optional[int] = None):
    limit = requests_per_min or _cfg.RATE_LIMIT_REQUESTS_PER_MIN
    window = 60
    def decorator(fn):
        def wrapper(*args, **kwargs):
            ip = request.headers.get("X-Forwarded-For", request.remote_addr) or "anon"
            key = f"rate:{ip}:{int(time.time() // window)}"
            count = _r.incr(key)
            if count == 1:
                _r.expire(key, window)
            if count > limit:
                abort(429, description="Too many requests")
            return fn(*args, **kwargs)
        return wrapper
    return decorator

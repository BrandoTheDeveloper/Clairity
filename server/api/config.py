import os
from typing import Optional
from pydantic import BaseModel

class AppConfig(BaseModel):
    FLASK_ENV: str = os.getenv("FLASK_ENV", "production")
    FLASK_DEBUG: bool = bool(int(os.getenv("FLASK_DEBUG", "0")))
    PORT: int = int(os.getenv("PORT", "5001"))
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")

    AIRNOW_API_KEY: Optional[str] = os.getenv("AIRNOW_API_KEY")
    OPENAQ_API_KEY: Optional[str] = os.getenv("OPENAQ_API_KEY")
    IQAIR_API_KEY: Optional[str] = os.getenv("IQAIR_API_KEY")

    RATE_LIMIT_REQUESTS_PER_MIN: int = int(os.getenv("RATE_LIMIT_REQUESTS_PER_MIN", "60"))

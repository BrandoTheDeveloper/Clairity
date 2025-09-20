from pydantic import BaseModel
from typing import Literal, Optional

class AQReading(BaseModel):
    pm25: Optional[float] = None
    pm10: Optional[float] = None
    o3: Optional[float] = None
    no2: Optional[float] = None
    so2: Optional[float] = None
    co: Optional[float] = None
    source: str
    timestamp: str

class RiskResult(BaseModel):
    label: Literal["Good", "Caution", "Avoid"]
    score: float
    reasons: list[str]

class AQResponse(BaseModel):
    reading: AQReading
    risk: RiskResult

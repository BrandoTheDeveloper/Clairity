from typing import Protocol
from api.models.schemas import AQResponse

class AirQualityProvider(Protocol):
    async def get_air_quality(self, lat: float, lon: float) -> AQResponse: ...

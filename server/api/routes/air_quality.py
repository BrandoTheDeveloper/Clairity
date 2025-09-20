from flask import Blueprint, jsonify, request
import asyncio
from api.utils.rate_limit import rate_limit
from api.services.air_quality import get_location_risk

bp = Blueprint("air_quality", __name__)

@bp.get("/risk")
@rate_limit()
def risk():
    lat = float(request.args.get("lat", "0"))
    lon = float(request.args.get("lon", "0"))
    result = asyncio.run(get_location_risk(lat, lon))
    return jsonify(result), 200

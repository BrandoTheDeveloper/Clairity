from typing import Optional
from api.models.schemas import AQReading, RiskResult

PM25_THRESHOLDS = { "Good": 12.0, "Caution": 35.4 }

def assess_risk(reading: AQReading, profile: Optional[dict] = None) -> RiskResult:
    reasons: list[str] = []
    score = 0.0
    pm25 = reading.pm25

    adj = 1.0
    if profile and profile.get("sensitive", False):
        adj = 0.8
        reasons.append("Sensitive profile: thresholds tightened")

    g_thr = PM25_THRESHOLDS["Good"] * adj
    c_thr = PM25_THRESHOLDS["Caution"] * adj

    if pm25 is None:
        label = "Caution"; reasons.append("PM2.5 missing; defaulting to Caution")
    elif pm25 <= g_thr:
        label = "Good"
    elif pm25 <= c_thr:
        label = "Caution"; score = 0.6; reasons.append(f"PM2.5={pm25}μg/m³ exceeds Good ({g_thr:.1f})")
    else:
        label = "Avoid"; score = 0.9; reasons.append(f"PM2.5={pm25}μg/m³ exceeds Caution ({c_thr:.1f})")
    return RiskResult(label=label, score=score, reasons=reasons)

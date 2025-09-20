How to avoid conflicts & mismatch (practical rules)
1.	Authoritative precedence
o	For US locations use AirNow/AQS first (official EPA). If no local data, fallback to OpenAQ → IQAir. (Avoid averaging sources blindly — prefer authoritative then open then paid.) docs.airnowapi.org+1
2.	Normalize units and timestamps
o	Convert concentrations to µg/m³ for PM and ppb for gases; convert to a single timezone (store ISO8601 with UTC). Always display local time converted from UTC.
3.	Harmonize AQI vs raw concentration
o	Many APIs return concentration and/or AQI. Use EPA AQI breakpoints for the US to compute categories so your thresholds are consistent. AirNow
4.	De-duplicate overlapping stations
o	When multiple stations within a radius report, take a weighted NowCast average (AirNow uses NowCast). If a sensor is flagged as mobile or uncalibrated, deprioritize. OpenAQ provides station metadata for this. OpenAQ Docs+1
5.	Rate-limit & caching
o	Cache per-location responses (5–15 min for AQ/Smoke; 30–60 min for radon). Use exponential backoff for API errors; keep per-key request counters to avoid being cut off.
6.	Licensing & attribution
o	Respect API terms: many (OpenAQ) require attribution; AirNow/AQS require attribution and have usage guidelines. Store metadata for each data point (provider + timestamp + station id). OpenAQ Docs+1
7.	Privacy & compliance
o	Health data: minimal retention, local encryption, clear consent; if you plan to store or process clinical data, consult HIPAA/legal counsel. For wearables, follow OAuth scopes & explain use.
8.	Fallback strategy
o	If primary API returns error: (1) fallback to secondary vendor, (2) show cached data with “stale” badge, (3) show “data unavailable” gracefully.
________________________________________
Minimal architecture (hackathon MVP)
1.	Mobile front end (React Native) — collects GPS + profile + saved places; shows Here-and-Now card.
2.	Backend (Node/Flask server) — handles API keys securely, queries AirNow/OpenAQ, FIRMS, weather, traffic; exposes small REST endpoints to the app.
3.	Database (Firebase / Supabase) — store user profile, saved places, minimal health flags (consent only).
4.	AI layer — server-side call to Gemini via Vertex/Firebase AI Logic for generating the one-sentence rationale and tailored tips (send only non-PII). Google Cloud+1
________________________________________
Integration order (what to implement first — hackathon friendly)
Phase 0 (prep)
•	Register API keys: AirNow, OpenAQ, NASA FIRMS (Earthdata), TomTom/HERE (pick one), OpenWeather, Gemini dev key (or set up Firebase AI Logic).
•	Create shared secrets vault (env vars / secret manager).
Phase 1 (MVP — Day 1)
1.	Backend endpoint: GET /v1/risk?lat={}&lon={} → returns normalized AQ + smoke flag + radon (lookup by county).
o	Query AirNow (or OpenAQ if no AirNow) → normalize to AQI & category. docs.airnowapi.org+1
o	Query NASA FIRMS / NOAA → produce smoke boolean. NASA FIRMS+1
2.	Frontend: Home Dashboard showing Risk Card with one-sentence rationale (initially rule-based).
Phase 2 (Day 2)
3. Add Personalized Profile → tweak thresholds in backend rules.
4. Add Saved Places → query risk endpoint for each pinned location + 6–12h forecast from AirNow/Weather.
5. Polish demo & emergency modal (static guidance).
Phase 3 (if time / stretch)
6. Add Run Coach rule engine (use AQ + smoke + profile) and Gemini for more natural language suggestions.
7. Add traffic overlay only if it maps to NO₂ spikes for saved places.
________________________________________
Quick example: API-call order for a single location (pseudo)
1.	Get lat/lon from device.
2.	Call AirNow/AQS for nearest AQ data (if US). If 404/empty → call OpenAQ → if that fails → IQAir. docs.airnowapi.org+2OpenAQ Docs+2
3.	Call FIRMS (NASA) + NOAA smoke forecast to set smoke flag. NASA FIRMS+1
4.	Call weather API for humidity/temp.
5.	Look up county ZIP in EPA Radon map for radon tile. aqs.epa.gov
6.	Backend computes normalized AQI, applies profile adjustments, returns classification + one-line rationale (optionally ask Gemini to rewrite for clarity).
________________________________________
Final checklist (copy & paste to your repo README)
•	Get API keys: AirNow, OpenAQ, NASA FIRMS, TomTom/HERE, OpenWeather, Gemini (or Firebase AI Logic). Google AI for Developers+4docs.airnowapi.org+4OpenAQ Docs+4
•	Implement secure secret storage (env or secret manager).
•	Backend risk endpoint (AirNow → OpenAQ fallback).
•	Smoke detection (FIRMS + NOAA).
•	Profile adjustments (asthma/elderly/pregnant toggles).
•	Saved places + 6–12h outlook caching.
•	Emergency mode static content.
•	Demo script: show two users (healthy vs asthma) and one wildfire case.

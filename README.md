APP NAME: CLAIRITY
GROUP NAME: CARBON HACKERS
FEATURE IDEAS: SYNC WITH SMART DEVICES, EMERGENCY MODE(A QUICK WHAT-TO-DO GUIDE FOR EMERGENCIES LIKE WILDFIRES)

DATA REQUIREMENTS  
•	Traffic dataset API
•	Health synced dataset
•	Global Weather API
•	Location (Access to GPS)
•	Bluetooth (to sync with smart devices)
•	AI API (Gemini API)
•	Wildfire/Smoke Indicators (Pulls from satellite or government smoke plume data (e.g., NOAA, EPA, or AirNow).)
•	Air Quality APIs: AirNow API, OpenAQ, or IQAir for PM2.5/PM10, O₃, and NO₂
•	Radon Maps: U.S. EPA Radon Zones or local geological survey data.

Prioritized Features (Healthcare Track Focus)
Tier 1 – Must-Have MVP (Core for Hackathon Demo)
✅ Here-and-Now Risk Card
•	Shows PM2.5/PM10, O₃, NO₂, wildfire smoke, radon context.
•	Converts data → Good / Caution / Avoid + rationale.
•	Healthcare impact: Directly addresses air pollution → lung cancer/respiratory risk.
✅ Personalized Profile
•	User inputs: asthma, cardiopulmonary disease, pregnancy, child/older adult.
•	Adjusts thresholds → more sensitive for at-risk groups.
•	Healthcare impact: Connects exposure to individual health vulnerability.
✅ Saved Places
•	Pin home, work, school, gym.
•	One-tap view + 6–12h outlook.
•	Healthcare impact: Supports real-life daily risk management.
⚡ Run Coach (Health Buddy)
•	Suggests safe times/directions for outdoor activity.
•	Uses AQI + smoke signals + profile risk level.
•	Bonus points: small but highly relevant to healthy lifestyle & prevention.

These three are most aligned with the sponsor’s healthcare focus and will make your demo look strong and relevant.
________________________________________
Tier 2 – Strong Add-Ons (If Time Allows)
⚡ Emergency Mode (Quick Guides)
•	What to do during wildfire smoke or bad AQI.
•	Lightweight (static content).
•	Adds a safety-first healthcare angle without much dev overhead.
Tier 3 – Future Roadmap (Pitch but not build in hackathon)
•	Sync with Smart Devices (Fitbit, Apple Health, Garmin).
•	AI Integrated Health Assistant (daily contextual advice).
•	Collect Recent Injury/Condition Data (manual entry or device sync).
Mention these as future growth to show vision, but don’t sink hackathon hours into them.
________________________________________
Requirements to Get Started (Hackathon-Friendly)
Day 1: Core Setup
•	Tech stack:
o	Mobile-first → React Native (cross-platform).
o	Backend: lightweight Flask or Node.js API wrapper.
o	Database: Firebase or Supabase (fast setup for Saved Places + Profiles).
•	Data Sources:
o	AirNow API (PM2.5, PM10, O₃, NO₂).
o	NOAA/NASA wildfire data.
o	EPA Radon Zone Maps (static lookup).
________________________________________
Feature Breakdown
1.	Here-and-Now Risk Card
o	Input: GPS coordinates → API call → AQI values.
o	Logic: Thresholds → Good / Caution / Avoid.
o	Output: UI card with rationale (one sentence).
2.	Personalized Profile
o	Input: user health sensitivities (checkboxes).
o	Logic: Lower thresholds for at-risk groups (e.g., AQI “Caution” for asthma earlier).
o	Output: Adjusted classification.
3.	Saved Places
o	DB or local storage.
o	Query AQI for pinned locations.
o	Display 6–12h forecast.
4.	Emergency Mode (if time)
o	Static JSON with wildfire/poor air quality “what to do.”
o	Triggered by button → modal view.
5.	Run Coach (if time)
o	Input: current AQI + outlook.
o	Logic: Suggest “best time window” for run (or recommend indoor).
________________________________________
Hackathon Strategy:
•	Day 1: Build Home Dashboard + Risk Card logic + APIs.
•	Day 2 (AM): Add Profile sensitivity + Saved Places.
•	Day 2 (PM): Polish UI, add Emergency Mode or Run Coach if time.
•	Demo: Show a user with asthma → personalized caution message. Then switch to healthy user → normal guidance. Judges love that “personalization toggle.”


import React, { useEffect, useState } from "react";
import { getRisk } from "../api/client";
import { useApp } from "../state/AppContext";
import AQSummary from "../components/organisms/AQSummary";

function useGeolocation() {
  const [coords, setCoords] = useState<{ lat: number; lon: number } | null>(null);
  const [error, setError] = useState<string | null>(null);
  useEffect(() => {
    if (!('geolocation' in navigator)) { setError('Geolocation not supported'); return; }
    navigator.geolocation.getCurrentPosition(
      pos => setCoords({ lat: pos.coords.latitude, lon: pos.coords.longitude }),
      err => setError(err.message),
      { enableHighAccuracy: true, maximumAge: 10000, timeout: 15000 }
    );
  }, []);
  return { coords, error };
}

export default function Home() {
  const { coords, error } = useGeolocation();
  const { lastReading, lastRisk, setState } = useApp();
  const [loading, setLoading] = useState(false);

  async function fetchRisk() {
    if (!coords) return;
    try {
      setLoading(true);
      const data = await getRisk(coords.lat, coords.lon);
      setState({ lastReading: data.reading, lastRisk: data.risk });
    } catch (e: any) {
      alert(e?.message ?? "Failed to fetch risk");
    } finally { setLoading(false); }
  }

  useEffect(() => { if (coords) fetchRisk(); }, [coords?.lat, coords?.lon]);

  return (
    <div>
      {lastReading && lastRisk ? (
        <AQSummary pm25={lastReading.pm25} label={lastRisk.label} source={lastReading.source} />
      ) : (
        <div className="container"><div>Please allow location to fetch local air quality.</div></div>
      )}
      <div style={{ marginTop: 12 }}>
        <button onClick={fetchRisk} disabled={!coords || loading}>{loading ? "Loading…" : "Refresh"}</button>
      </div>
      {error && <div style={{ color: "red" }}>{error}</div>}
    </div>
  );
}

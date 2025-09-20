import React from "react";
import { useApp } from "../state/AppContext";

export default function Details() {
  const { lastReading, lastRisk } = useApp();
  return (
    <div>
      <h3>Details</h3>
      <div>Timestamp: {lastReading?.timestamp ?? "—"}</div>
      <div>PM2.5: {lastReading?.pm25 ?? "—"} μg/m³</div>
      <div>Risk: {lastRisk?.label ?? "—"} (score {lastRisk?.score ?? 0})</div>
      <ul>{(lastRisk?.reasons ?? []).map((r,i)=><li key={i}>{r}</li>)}</ul>
    </div>
  );
}

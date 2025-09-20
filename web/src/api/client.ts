import axios from "axios";

const BASE = import.meta.env.VITE_API_BASE_URL || "http://localhost:5001";

export const api = axios.create({ baseURL: `${BASE}/api`, timeout: 10000 });

export async function getRisk(lat: number, lon: number) {
  const { data } = await api.get(`/air-quality/risk`, { params: { lat, lon } });
  return data as {
    reading: { pm25?: number; source: string; timestamp: string };
    risk: { label: "Good" | "Caution" | "Avoid"; score: number; reasons: string[] };
  };
}

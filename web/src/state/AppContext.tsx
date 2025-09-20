import React, { createContext, useContext, useState, ReactNode } from "react";

export type Reading = { pm25?: number; source: string; timestamp: string };
export type Risk = { label: "Good" | "Caution" | "Avoid"; score: number; reasons: string[] };

type AppState = { lastReading?: Reading; lastRisk?: Risk; setState: (s: Partial<AppState>) => void };

const Ctx = createContext<AppState | null>(null);

export const AppProvider = ({ children }: { children: ReactNode }) => {
  const [state, setStateInternal] = useState<AppState>({ setState: () => {} });
  const setState = (s: Partial<AppState>) => setStateInternal(prev => ({ ...prev, ...s, setState }));
  return <Ctx.Provider value={{ ...state, setState }}>{children}</Ctx.Provider>;
};

export const useApp = () => {
  const ctx = useContext(Ctx);
  if (!ctx) throw new Error("useApp must be used within AppProvider");
  return ctx;
};

import React from "react";
import { Outlet, Link, useLocation } from "react-router-dom";
import { AppProvider } from "./state/AppContext";

export default function App() {
  const loc = useLocation();
  return (
    <AppProvider>
      <div className="container">
        <nav style={{display:"flex",gap:12,marginBottom:20}}>
          <Link to="/" aria-current={loc.pathname === "/" ? "page" : undefined}>Home</Link>
          <Link to="/details" aria-current={loc.pathname === "/details" ? "page" : undefined}>Details</Link>
        </nav>
        <Outlet />
      </div>
    </AppProvider>
  );
}

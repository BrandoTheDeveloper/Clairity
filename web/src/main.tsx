import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import App from "./App";
import Home from "./screens/Home";
import Details from "./screens/Details";
import "./index.css";

const router = createBrowserRouter([
  { element: <App />, children: [
    { path: "/", element: <Home /> },
    { path: "/details", element: <Details /> }
  ]}
]);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

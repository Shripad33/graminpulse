import { useEffect, useState } from "react";

const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000";

/**
 * GraminPulse dashboard — starter scaffold.
 * Replace with the full enterprise list / forecast chart / alerts UI.
 */
export default function App() {
  const [enterprises, setEnterprises] = useState([]);

  useEffect(() => {
    fetch(`${API_BASE}/enterprises`)
      .then((res) => res.json())
      .then(setEnterprises)
      .catch((err) => console.error("Failed to load enterprises:", err));
  }, []);

  return (
    <div style={{ fontFamily: "sans-serif", padding: "2rem" }}>
      <h1>GraminPulse</h1>
      <p>Confidence-Aware Cash Flow Forecasting & Action Recommendation</p>

      <h2>Enterprises</h2>
      <ul>
        {enterprises.map((e) => (
          <li key={e.id}>
            {e.name} — <strong>{e.risk}</strong>
          </li>
        ))}
      </ul>
    </div>
  );
}

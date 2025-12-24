import React from 'react';

const exposureData = [
  { label: 'Social Profiles', value: 72 },
  { label: 'Data Brokers', value: 45 },
  { label: 'Marketing Lists', value: 61 },
];

const accounts = [
  { name: 'github.com/ghostuser', action: 'Keep' },
  { name: 'twitter.com/ghostuser', action: 'Delete' },
  { name: 'linkedin.com/in/ghostuser', action: 'Delete' },
];

export default function App() {
  return (
    <div className="app">
      <header className="app__header">
        <div>
          <p className="app__eyebrow">GhostProtocol</p>
          <h1>Privacy Exposure Dashboard</h1>
          <p className="app__subhead">
            Automated footprint discovery and right-to-erasure orchestration.
          </p>
        </div>
        <button className="primary">Start Footprint Scan</button>
      </header>

      <section className="card grid">
        <div>
          <h2>Privacy Health Score</h2>
          <p className="score">68</p>
          <p className="muted">Based on discovered accounts, data brokers, and inbox metadata.</p>
        </div>
        <div className="map-placeholder">
          <span>Interactive exposure map</span>
        </div>
      </section>

      <section className="card">
        <h2>Exposure Overview</h2>
        <div className="bars">
          {exposureData.map((item) => (
            <div key={item.label} className="bar">
              <div className="bar__label">{item.label}</div>
              <div className="bar__track">
                <span style={{ width: `${item.value}%` }} />
              </div>
              <span className="bar__value">{item.value}%</span>
            </div>
          ))}
        </div>
      </section>

      <section className="card">
        <h2>Found Accounts</h2>
        <div className="account-list">
          {accounts.map((account) => (
            <div key={account.name} className="account-item">
              <span>{account.name}</span>
              <button className={account.action === 'Delete' ? 'danger' : 'ghost'}>
                {account.action}
              </button>
            </div>
          ))}
        </div>
      </section>

      <section className="card">
        <h2>Legal Request Tracker</h2>
        <div className="tracker">
          <div>
            <p className="tracker__label">Requests Sent</p>
            <p className="tracker__value">12</p>
          </div>
          <div>
            <p className="tracker__label">Awaiting Response</p>
            <p className="tracker__value">4</p>
          </div>
          <div>
            <p className="tracker__label">Completed</p>
            <p className="tracker__value">8</p>
          </div>
        </div>
      </section>
    </div>
  );
}

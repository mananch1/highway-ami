import React, { useEffect, useState } from 'react';
import { useSearchParams, Link } from 'react-router-dom';
import { getEmergencyStatus } from '../api/api';
import StatusBadge from '../components/StatusBadge';
import Chat from '../components/Chat';

const STEPS = [
  { key: 'REPORTED', label: 'Logged', desc: 'Request Received' },
  { key: 'ASSIGNED', label: 'Dispatched', desc: 'Unit Assigned' },
  { key: 'IN_PROGRESS', label: 'En Route', desc: 'On-Site Response' },
  { key: 'RESOLVED', label: 'Resolved', desc: 'Service Completed' }
];

const getStepIndex = (status) => {
  switch (status) {
    case 'REPORTED': return 0;
    case 'ASSIGNED': return 1;
    case 'IN_PROGRESS': return 2;
    case 'RESOLVED': return 3;
    case 'CANCELLED': return -1;
    default: return 0;
  }
};

const EmergencyStatus = () => {
  const [searchParams] = useSearchParams();
  const token = searchParams.get('token');
  
  const [incident, setIncident] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchStatus = async () => {
      if (!token) {
        setError('No tracking token provided.');
        setLoading(false);
        return;
      }

      try {
        const data = await getEmergencyStatus(token);
        setIncident(data);
      } catch (err) {
        setError('Failed to fetch emergency status. Invalid or expired tracking token.');
      } finally {
        setLoading(false);
      }
    };

    fetchStatus();
    
    // Poll for status updates every 15 seconds
    const interval = setInterval(fetchStatus, 15000);
    return () => clearInterval(interval);
  }, [token]);

  if (loading && !incident) {
    return (
      <div className="container status-page-container" style={{ padding: '4rem 1rem', textAlign: 'center' }}>
        <h2>Connecting to Dispatch Center...</h2>
        <p style={{ color: 'var(--text-muted)' }}>Retrieving live incident status and technician coordinates.</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="container status-page-container" style={{ padding: '4rem 1rem', textAlign: 'center' }}>
        <h2 style={{ color: 'var(--danger)' }}>Tracking Error</h2>
        <p style={{ color: 'var(--text-muted)', marginBottom: '1.5rem' }}>{error}</p>
        <Link to="/" className="btn-primary" style={{ display: 'inline-block' }}>
          Return to Dispatch Intake
        </Link>
      </div>
    );
  }

  if (!incident) return null;

  const currentStep = getStepIndex(incident.status);

  return (
    <div className="container status-page-container">
      {/* Header */}
      <div className="dispatch-status-header">
        <div className="status-meta-row">
          <span className="dispatch-badge">DISPATCH CONSOLE</span>
          <span className="incident-ref-badge">TICKET #{incident.id}</span>
        </div>
        <h1 className="status-page-title">Live Incident Tracking</h1>
        <p className="status-page-subtitle">Real-time status feed and technician communication channel</p>
      </div>

      {/* Progress Stepper Card */}
      <div className="card stepper-panel">
        <div className="stepper-track">
          {STEPS.map((step, idx) => {
            const isCompleted = currentStep > idx;
            const isCurrent = currentStep === idx;
            return (
              <div
                key={step.key}
                className={`stepper-node ${isCompleted ? 'node-completed' : ''} ${isCurrent ? 'node-active' : ''}`}
              >
                <div className="node-marker">
                  {isCompleted ? (
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                  ) : (
                    idx + 1
                  )}
                </div>
                <div className="node-info">
                  <span className="node-label">{step.label}</span>
                  <span className="node-desc">{step.desc}</span>
                </div>
                {idx < STEPS.length - 1 && <div className="node-connector"></div>}
              </div>
            );
          })}
        </div>
      </div>

      {/* Grid: Details + Chat */}
      <div className="status-layout-grid">
        {/* Incident Summary Card */}
        <div className="card incident-card-panel">
          <div className="panel-header-row">
            <div>
              <h2 className="panel-heading">Incident Overview</h2>
              <span className="panel-subheading">Priority Dispatch Record</span>
            </div>
            <StatusBadge status={incident.status} />
          </div>

          <div className="data-table-list">
            <div className="data-row">
              <span className="data-key">Service Category</span>
              <span className="data-value highlight-text">
                {incident.type?.replace('_', ' ')}
              </span>
            </div>

            <div className="data-row">
              <span className="data-key">Reported Location</span>
              <span className="data-value">{incident.location}</span>
            </div>

            <div className="data-row">
              <span className="data-key">Caller Name</span>
              <span className="data-value">{incident.guestName || 'Public Caller'}</span>
            </div>

            <div className="data-row">
              <span className="data-key">Assigned Unit</span>
              <div className="unit-assignment-box">
                {incident.technicianName ? (
                  <>
                    <span className="unit-name">Unit: {incident.technicianName}</span>
                    <a
                      href="tel:+919876543210"
                      className="btn-call-unit"
                      title="Direct telephone line"
                    >
                      Telephone Contact
                    </a>
                  </>
                ) : (
                  <span className="unit-pending">Routing to nearest available unit...</span>
                )}
              </div>
            </div>

            {incident.description && (
              <div className="data-row">
                <span className="data-key">Report Notes</span>
                <span className="data-value notes-block">{incident.description}</span>
              </div>
            )}
          </div>

          <div className="protocol-notice-box">
            <strong>Safety Advisory:</strong> Remain inside your vehicle with hazard lights activated. Use the dispatch terminal below to communicate landmarks directly with your assigned unit.
          </div>
        </div>

        {/* Real-time WebSocket Chat */}
        <div className="chat-panel-wrapper">
          <Chat incidentId={incident.id} guestToken={token} guestName={incident.guestName} />
        </div>
      </div>
    </div>
  );
};

export default EmergencyStatus;

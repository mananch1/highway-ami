import React, { useEffect, useState } from 'react';
import { useSearchParams, Link } from 'react-router-dom';
import { getEmergencyStatus } from '../api/api';
import StatusBadge from '../components/StatusBadge';
import Chat from '../components/Chat';

const STEPS = [
  { key: 'REPORTED', label: 'Reported', desc: 'Request Received' },
  { key: 'ASSIGNED', label: 'Dispatched', desc: 'Technician Assigned' },
  { key: 'IN_PROGRESS', label: 'In Progress', desc: 'En Route / On-Site' },
  { key: 'RESOLVED', label: 'Resolved', desc: 'Assistance Complete' }
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
        setError('Failed to fetch emergency status. Invalid or expired token.');
      } finally {
        setLoading(false);
      }
    };

    fetchStatus();
    
    // Poll for status updates every 15 seconds for rapid updates
    const interval = setInterval(fetchStatus, 15000);
    return () => clearInterval(interval);
  }, [token]);

  if (loading && !incident) {
    return (
      <div className="container status-page-wrapper" style={{ padding: '4rem 1rem', textAlign: 'center' }}>
        <div className="loading-spinner">⏳</div>
        <h2>Locating Emergency Dispatch...</h2>
        <p style={{ color: 'var(--text-muted)' }}>Connecting to regional highway patrol dispatch...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="container status-page-wrapper" style={{ padding: '4rem 1rem', textAlign: 'center' }}>
        <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>⚠️</div>
        <h2 style={{ color: 'var(--danger)' }}>Tracking Error</h2>
        <p style={{ color: 'var(--text-muted)', marginBottom: '1.5rem' }}>{error}</p>
        <Link to="/" className="primary" style={{ display: 'inline-block', padding: '0.75rem 1.5rem' }}>
          Return to Emergency Request Form
        </Link>
      </div>
    );
  }

  if (!incident) return null;

  const currentStep = getStepIndex(incident.status);

  return (
    <div className="container status-page-wrapper">
      {/* Header */}
      <div className="status-header">
        <div className="status-live-pill">
          <span className="live-dot"></span> LIVE DISPATCH FEED
        </div>
        <h1>Emergency Dispatch Tracker</h1>
        <p className="subtitle">Reference Ticket: #{incident.id} • Live connection established</p>
      </div>

      {/* 5-Step Visual Dispatch Stepper */}
      <div className="card stepper-card">
        <div className="stepper-container">
          {STEPS.map((step, idx) => {
            const isCompleted = currentStep > idx;
            const isCurrent = currentStep === idx;
            return (
              <div
                key={step.key}
                className={`stepper-step ${isCompleted ? 'completed' : ''} ${isCurrent ? 'active' : ''}`}
              >
                <div className="step-circle">
                  {isCompleted ? '✓' : idx + 1}
                </div>
                <div className="step-content">
                  <div className="step-label">{step.label}</div>
                  <div className="step-desc">{step.desc}</div>
                </div>
                {idx < STEPS.length - 1 && <div className="step-line"></div>}
              </div>
            );
          })}
        </div>
      </div>

      {/* Main Grid: Details + Chat */}
      <div className="status-grid">
        {/* Incident Summary Card */}
        <div className="card incident-summary-card">
          <div className="card-top-header">
            <div>
              <h2>Assistance Details</h2>
              <span className="timestamp">Active Incident</span>
            </div>
            <StatusBadge status={incident.status} />
          </div>

          <div className="details-list">
            <div className="detail-item">
              <span className="detail-label">Issue Category</span>
              <span className="detail-value highlight-value">
                {incident.type?.replace('_', ' ')}
              </span>
            </div>

            <div className="detail-item">
              <span className="detail-label">Reported Location</span>
              <span className="detail-value">📍 {incident.location}</span>
            </div>

            <div className="detail-item">
              <span className="detail-label">Caller Name</span>
              <span className="detail-value">{incident.guestName || 'Anonymous Guest'}</span>
            </div>

            <div className="detail-item">
              <span className="detail-label">Assigned Technician</span>
              <div className="technician-info-box">
                {incident.technicianName ? (
                  <>
                    <span className="tech-name">🛠️ {incident.technicianName}</span>
                    <a
                      href="tel:+919876543210"
                      className="call-tech-btn"
                      title="Direct telephone connection to technician"
                    >
                      📞 Call Technician
                    </a>
                  </>
                ) : (
                  <span className="tech-searching">🔍 Dispatching nearest responder...</span>
                )}
              </div>
            </div>

            {incident.description && (
              <div className="detail-item">
                <span className="detail-label">Landmark / Notes</span>
                <span className="detail-value notes-text">{incident.description}</span>
              </div>
            )}
          </div>

          <div className="emergency-tip-box">
            <strong>💡 Safety Protocol:</strong> Stay inside your vehicle with hazard lights on and seatbelt fastened while parked on the shoulder. Use the chat window to share additional landmarks with your responder.
          </div>
        </div>

        {/* Real-time WebSocket Chat */}
        <div className="chat-card-container">
          <Chat incidentId={incident.id} guestToken={token} guestName={incident.guestName} />
        </div>
      </div>
    </div>
  );
};

export default EmergencyStatus;

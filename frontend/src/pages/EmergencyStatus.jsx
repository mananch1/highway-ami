import React, { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import { getEmergencyStatus } from '../api/api';
import StatusBadge from '../components/StatusBadge';
import Chat from '../components/Chat';

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
    
    // Poll for status updates every 30 seconds
    const interval = setInterval(fetchStatus, 30000);
    return () => clearInterval(interval);
  }, [token]);

  if (loading && !incident) return <div className="container" style={{ padding: '4rem 0', textAlign: 'center' }}>Loading status...</div>;
  if (error) return <div className="container" style={{ padding: '4rem 0', textAlign: 'center', color: 'var(--danger)' }}>{error}</div>;
  if (!incident) return null;

  return (
    <div className="container" style={{ maxWidth: '900px', margin: '2rem auto' }}>
      <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
        <h1 style={{ color: 'var(--danger)' }}>Emergency Status Tracker</h1>
        <p style={{ color: 'var(--text-muted)' }}>Keep this page open to track your assistance and communicate with your technician.</p>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 350px', gap: '2rem' }}>
        <div className="card">
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
            <h2 style={{ margin: 0 }}>Incident Info</h2>
            <StatusBadge status={incident.status} />
          </div>

          <div style={{ display: 'grid', gap: '1rem' }}>
            <div>
              <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>Type</p>
              <p style={{ fontWeight: '500' }}>{incident.type}</p>
            </div>
            <div>
              <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>Location</p>
              <p style={{ fontWeight: '500' }}>{incident.location}</p>
            </div>
            <div>
              <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>Assigned Technician</p>
              <p style={{ fontWeight: '500' }}>{incident.technicianName || 'Looking for available technicians...'}</p>
            </div>
          </div>
          
          <div style={{ marginTop: '2rem', padding: '1rem', backgroundColor: '#f0f9ff', borderRadius: '8px', border: '1px solid #bae6fd' }}>
            <p style={{ color: '#0369a1', margin: 0, fontSize: '0.9rem' }}>
              <strong>Tip:</strong> If you need to provide additional details to the assigned technician, use the chat box.
            </p>
          </div>
        </div>

        <div>
          <Chat incidentId={incident.id} guestToken={token} guestName={incident.guestName} />
        </div>
      </div>
    </div>
  );
};

export default EmergencyStatus;

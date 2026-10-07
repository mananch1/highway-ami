import React, { useEffect, useState, useContext } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { getIncident, updateIncidentStatus } from '../api/api';
import { AuthContext } from '../context/AuthContext';
import StatusBadge from '../components/StatusBadge';
import Chat from '../components/Chat';

const IncidentDetail = () => {
  const { id } = useParams();
  const [incident, setIncident] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const { user } = useContext(AuthContext);
  const navigate = useNavigate();

  const fetchIncident = async () => {
    try {
      const data = await getIncident(id);
      setIncident(data);
    } catch (err) {
      setError('Failed to fetch incident details.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchIncident();
  }, [id]);

  const handleStatusChange = async (newStatus) => {
    try {
      await updateIncidentStatus(id, newStatus);
      fetchIncident();
    } catch (err) {
      alert('Failed to update status');
    }
  };

  if (loading) return <div className="container"><p>Loading...</p></div>;
  if (error || !incident) return <div className="container"><p>{error}</p></div>;

  return (
    <div className="container">
      <button onClick={() => navigate(-1)} style={{ marginBottom: '1rem', background: 'none', border: '1px solid var(--border)', padding: '0.5rem 1rem' }}>
        &larr; Back
      </button>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 350px', gap: '2rem' }}>
        <div className="card">
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
            <h2 style={{ margin: 0 }}>Incident Details</h2>
            <StatusBadge status={incident.status} />
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginBottom: '2rem' }}>
            <div>
              <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>Type</p>
              <p style={{ fontWeight: '500' }}>{incident.type}</p>
            </div>
            <div>
              <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>Location</p>
              <p style={{ fontWeight: '500' }}>{incident.location}</p>
            </div>
            <div>
              <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>Created At</p>
              <p style={{ fontWeight: '500' }}>{new Date(incident.createdAt).toLocaleString()}</p>
            </div>
            <div>
              <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>Assigned Technician</p>
              <p style={{ fontWeight: '500' }}>{incident.technicianName || 'Unassigned'}</p>
            </div>
            <div style={{ gridColumn: 'span 2' }}>
              <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>Description</p>
              <p style={{ fontWeight: '500' }}>{incident.description || 'No description provided.'}</p>
            </div>
          </div>

          <div style={{ borderTop: '1px solid var(--border)', paddingTop: '1.5rem', display: 'flex', gap: '1rem' }}>
            {/* Action Buttons based on Role and Status */}
            {user.role === 'CUSTOMER' && (incident.status === 'REQUESTED' || incident.status === 'AUTO_ASSIGNED') && (
              <button className="danger" onClick={() => handleStatusChange('CANCELLED')}>Cancel Request</button>
            )}
            
            {user.role === 'TECHNICIAN' && incident.status === 'AUTO_ASSIGNED' && (
              <button className="primary" onClick={() => handleStatusChange('IN_PROGRESS')}>Start Work</button>
            )}
            {user.role === 'TECHNICIAN' && incident.status === 'IN_PROGRESS' && (
              <button className="success" onClick={() => handleStatusChange('RESOLVED')}>Mark as Resolved</button>
            )}

            {user.role === 'ADMIN' && (
              <>
                <button className="danger" onClick={() => handleStatusChange('CANCELLED')}>Cancel Incident</button>
                {(incident.status === 'RESOLVED') && (
                  <button className="primary" onClick={() => handleStatusChange('CLOSED')}>Close Incident</button>
                )}
              </>
            )}
          </div>
        </div>

        <div>
          <Chat incidentId={id} />
        </div>
      </div>
    </div>
  );
};

export default IncidentDetail;

import React from 'react';
import { useNavigate } from 'react-router-dom';
import StatusBadge from './StatusBadge';

const IncidentCard = ({ incident }) => {
  const navigate = useNavigate();

  const handleCardClick = () => {
    navigate(`/incidents/${incident.id}`);
  };

  const formatDate = (dateString) => {
    if (!dateString) return '';
    return new Date(dateString).toLocaleString();
  };

  return (
    <div className="card" style={{ cursor: 'pointer', transition: 'transform 0.2s', ':hover': { transform: 'translateY(-2px)' } }} onClick={handleCardClick}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '1rem' }}>
        <h3 style={{ margin: 0, color: 'var(--text-main)' }}>{incident.type}</h3>
        <StatusBadge status={incident.status} />
      </div>
      
      <p style={{ margin: '0.5rem 0', color: 'var(--text-muted)' }}>
        <strong>Location:</strong> {incident.location}
      </p>
      
      <p style={{ margin: '0.5rem 0', color: 'var(--text-muted)' }}>
        <strong>Created:</strong> {formatDate(incident.createdAt)}
      </p>

      {incident.technicianName && (
        <p style={{ margin: '0.5rem 0', color: 'var(--text-muted)' }}>
          <strong>Technician:</strong> {incident.technicianName}
        </p>
      )}
    </div>
  );
};

export default IncidentCard;

import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { getIncidents } from '../api/api';
import IncidentCard from '../components/IncidentCard';

const CustomerDashboard = () => {
  const [incidents, setIncidents] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchIncidents = async () => {
      try {
        const data = await getIncidents();
        setIncidents(data);
      } catch (err) {
        console.error('Failed to fetch incidents', err);
      } finally {
        setLoading(false);
      }
    };
    fetchIncidents();
  }, []);

  return (
    <div className="container">
      <div className="dashboard-header">
        <h2>My Incidents</h2>
        <button className="primary" onClick={() => navigate('/create-incident')}>
          + New Incident
        </button>
      </div>

      {loading ? (
        <p>Loading incidents...</p>
      ) : incidents.length === 0 ? (
        <div className="card" style={{ textAlign: 'center', padding: '3rem' }}>
          <p>You don't have any incidents reported.</p>
        </div>
      ) : (
        <div className="incident-list">
          {incidents.map(inc => (
            <IncidentCard key={inc.id} incident={inc} />
          ))}
        </div>
      )}
    </div>
  );
};

export default CustomerDashboard;

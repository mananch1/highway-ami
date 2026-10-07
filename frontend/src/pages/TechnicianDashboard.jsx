import React, { useEffect, useState, useContext } from 'react';
import { getIncidents, toggleAvailability, getUsers } from '../api/api';
import IncidentCard from '../components/IncidentCard';
import { AuthContext } from '../context/AuthContext';

const TechnicianDashboard = () => {
  const [incidents, setIncidents] = useState([]);
  const [isAvailable, setIsAvailable] = useState(false);
  const [loading, setLoading] = useState(true);
  const { user } = useContext(AuthContext);

  useEffect(() => {
    fetchData();
  }, [user]);

  const fetchData = async () => {
    try {
      setLoading(true);
      try {
        const incidentsData = await getIncidents();
        setIncidents(incidentsData || []);
      } catch (e) {
        console.error('Failed to load incidents', e);
      }

      try {
        const usersData = await getUsers();
        const me = usersData?.find(u => u.id === user?.userId);
        if (me) {
          setIsAvailable(me.isAvailable !== undefined ? me.isAvailable : me.available);
        }
      } catch (e) {
        console.error('Failed to load user availability', e);
      }
    } finally {
      setLoading(false);
    }
  };

  const handleToggle = async () => {
    try {
      const res = await toggleAvailability(user.userId);
      const newAvail = res?.isAvailable !== undefined ? res.isAvailable : res?.available;
      if (newAvail !== undefined) {
        setIsAvailable(newAvail);
      } else {
        setIsAvailable(prev => !prev);
      }
    } catch (err) {
      console.error('Failed to toggle availability', err);
    }
  };

  return (
    <div className="container">
      <div className="dashboard-header">
        <h2>Assigned Incidents</h2>
        <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
          <span style={{ fontWeight: '500' }}>Status: {isAvailable ? 'Available' : 'Busy/Offline'}</span>
          <button className={isAvailable ? 'danger' : 'success'} onClick={handleToggle}>
            Toggle Availability
          </button>
        </div>
      </div>

      {loading ? (
        <p>Loading...</p>
      ) : incidents.length === 0 ? (
        <div className="card" style={{ textAlign: 'center', padding: '3rem' }}>
          <p>No incidents assigned to you right now.</p>
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

export default TechnicianDashboard;

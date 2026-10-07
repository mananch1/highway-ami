import React, { useEffect, useState } from 'react';
import { getDashboardSummary } from '../api/api';
import { PieChart, Pie, Cell, BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';
import { Link } from 'react-router-dom';
import StatusBadge from '../components/StatusBadge';

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#a855f7', '#ef4444'];

const AdminDashboard = () => {
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchSummary = async () => {
      try {
        const data = await getDashboardSummary();
        setSummary(data);
      } catch (err) {
        console.error('Failed to fetch summary', err);
      } finally {
        setLoading(false);
      }
    };
    fetchSummary();
  }, []);

  if (loading) return <div className="container"><p>Loading dashboard...</p></div>;
  if (!summary) return <div className="container"><p>Error loading dashboard.</p></div>;

  const pieData = Object.keys(summary.incidentsByStatus || {}).map(key => ({
    name: key,
    value: summary.incidentsByStatus[key]
  }));

  const barData = Object.keys(summary.incidentsByType || {}).map(key => ({
    name: key.replace('_', ' '),
    value: summary.incidentsByType[key]
  }));

  return (
    <div className="container">
      <div className="dashboard-header">
        <h2>Admin Dashboard</h2>
      </div>

      <div className="dashboard-stats">
        <div className="card stat-card">
          <h3>Total Incidents</h3>
          <div className="value">{summary.totalIncidents}</div>
        </div>
        <div className="card stat-card">
          <h3>Today's Incidents</h3>
          <div className="value">{summary.todayIncidents}</div>
        </div>
        <div className="card stat-card">
          <h3>Available Technicians</h3>
          <div className="value">{summary.availableTechnicians}</div>
        </div>
        <div className="card stat-card">
          <h3>Avg Resolution (mins)</h3>
          <div className="value">{summary.averageResolutionTimeMinutes.toFixed(1)}</div>
        </div>
      </div>

      <div className="charts-container">
        <div className="card" style={{ height: '300px' }}>
          <h3 style={{ marginBottom: '1rem' }}>Incidents by Status</h3>
          <ResponsiveContainer width="100%" height="100%">
            <PieChart>
              <Pie data={pieData} cx="50%" cy="50%" outerRadius={80} fill="#8884d8" dataKey="value" label>
                {pieData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
        <div className="card" style={{ height: '300px' }}>
          <h3 style={{ marginBottom: '1rem' }}>Incidents by Type</h3>
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={barData}>
              <XAxis dataKey="name" tick={{fontSize: 12}} />
              <YAxis />
              <Tooltip />
              <Bar dataKey="value" fill="#2563eb" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className="card">
        <h3 style={{ marginBottom: '1rem' }}>Recent Incidents</h3>
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr style={{ borderBottom: '2px solid var(--border)', textAlign: 'left' }}>
              <th style={{ padding: '0.5rem' }}>ID</th>
              <th style={{ padding: '0.5rem' }}>Type</th>
              <th style={{ padding: '0.5rem' }}>Status</th>
              <th style={{ padding: '0.5rem' }}>Customer</th>
              <th style={{ padding: '0.5rem' }}>Actions</th>
            </tr>
          </thead>
          <tbody>
            {(summary.recentIncidents || []).map(inc => (
              <tr key={inc.id} style={{ borderBottom: '1px solid var(--border)' }}>
                <td style={{ padding: '0.5rem' }}>{inc.id.substring(0,8)}...</td>
                <td style={{ padding: '0.5rem' }}>{inc.type}</td>
                <td style={{ padding: '0.5rem' }}><StatusBadge status={inc.status} /></td>
                <td style={{ padding: '0.5rem' }}>{inc.customerName || inc.guestName}</td>
                <td style={{ padding: '0.5rem' }}>
                  <Link to={`/incidents/${inc.id}`}>View</Link>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default AdminDashboard;

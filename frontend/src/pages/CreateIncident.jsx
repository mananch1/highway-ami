import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { createIncident } from '../api/api';

const CreateIncident = () => {
  const [formData, setFormData] = useState({
    type: 'FLAT_TIRE',
    location: '',
    description: ''
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    try {
      const res = await createIncident(formData);
      navigate(`/incidents/${res.id}`);
    } catch (err) {
      setError(err.response?.data?.message || 'Failed to create incident.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container" style={{ maxWidth: '600px', margin: '2rem auto' }}>
      <div className="card">
        <h2 style={{ marginBottom: '1.5rem' }}>Report New Incident</h2>
        {error && <div style={{ color: 'var(--danger)', marginBottom: '1rem' }}>{error}</div>}
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Incident Type</label>
            <select name="type" value={formData.type} onChange={handleChange}>
              <option value="FLAT_TIRE">Flat Tire</option>
              <option value="ENGINE_FAILURE">Engine Failure</option>
              <option value="ACCIDENT">Accident</option>
              <option value="LOCKOUT">Lockout</option>
              <option value="FUEL_EMPTY">Out of Fuel</option>
            </select>
          </div>
          <div className="form-group">
            <label>Location</label>
            <input type="text" name="location" required value={formData.location} onChange={handleChange} placeholder="Be as specific as possible" />
          </div>
          <div className="form-group">
            <label>Description</label>
            <textarea name="description" value={formData.description} onChange={handleChange} rows="4" placeholder="Additional details..." />
          </div>
          <div style={{ display: 'flex', gap: '1rem', marginTop: '1.5rem' }}>
            <button type="submit" className="primary" disabled={loading}>
              {loading ? 'Submitting...' : 'Submit Request'}
            </button>
            <button type="button" onClick={() => navigate(-1)} style={{ background: '#f1f5f9', color: '#475569' }}>
              Cancel
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default CreateIncident;

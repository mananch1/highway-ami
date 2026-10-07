import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { createEmergency } from '../api/api';

const Landing = () => {
  const [formData, setFormData] = useState({
    name: '',
    phone: '',
    location: '',
    type: 'FLAT_TIRE',
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
      const res = await createEmergency(formData);
      // res contains guestToken
      navigate(`/emergency/status?token=${res.guestToken}`);
    } catch (err) {
      setError(err.response?.data?.message || 'Failed to submit emergency request.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div style={{ textAlign: 'center', padding: '4rem 0' }}>
        <h1 style={{ fontSize: '3rem', color: 'var(--primary)', marginBottom: '1rem' }}>Roadside Assistance Portal</h1>
        <p style={{ fontSize: '1.25rem', color: 'var(--text-muted)' }}>Fast, reliable help when you need it most.</p>
      </div>

      <div style={{ maxWidth: '600px', margin: '0 auto', backgroundColor: '#fee2e2', padding: '2rem', borderRadius: '8px', border: '1px solid #fca5a5' }}>
        <h2 style={{ color: 'var(--danger)', marginBottom: '1.5rem', textAlign: 'center' }}>Emergency Help</h2>
        {error && <div style={{ color: 'var(--danger)', marginBottom: '1rem', textAlign: 'center' }}>{error}</div>}
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Name</label>
            <input type="text" name="name" required value={formData.name} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label>Phone Number</label>
            <input type="tel" name="phone" required value={formData.phone} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label>Location</label>
            <input type="text" name="location" required value={formData.location} onChange={handleChange} placeholder="e.g. I-95 North, Mile Marker 42" />
          </div>
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
            <label>Description (Optional)</label>
            <textarea name="description" value={formData.description} onChange={handleChange} rows="3" />
          </div>
          <button type="submit" className="danger" style={{ width: '100%', fontSize: '1.1rem', padding: '0.75rem' }} disabled={loading}>
            {loading ? 'Submitting...' : 'Request Emergency Assistance'}
          </button>
        </form>
      </div>
    </div>
  );
};

export default Landing;

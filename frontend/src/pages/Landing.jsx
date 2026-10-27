import React, { useState, useEffect } from 'react';
import { Link, useNavigate, useSearchParams } from 'react-router-dom';
import { createEmergency } from '../api/api';
import QrPlacardModal from '../components/QrPlacardModal';

const Landing = () => {
  const [searchParams] = useSearchParams();
  const [formData, setFormData] = useState({
    name: '',
    phone: '',
    location: '',
    type: 'FLAT_TIRE',
    description: ''
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [qrDetected, setQrDetected] = useState(false);
  const [isQrModalOpen, setIsQrModalOpen] = useState(false);
  const navigate = useNavigate();

  // Auto-detect URL query parameters from highway QR code scan
  useEffect(() => {
    const locParam = searchParams.get('loc') || searchParams.get('location');
    const typeParam = searchParams.get('type');
    const descParam = searchParams.get('desc') || searchParams.get('description');

    if (locParam || typeParam || descParam) {
      setFormData((prev) => ({
        ...prev,
        location: locParam || prev.location,
        type: typeParam ? typeParam.toUpperCase() : prev.type,
        description: descParam || prev.description
      }));
      setQrDetected(true);
    }
  }, [searchParams]);

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

  const handleApplyPreset = (presetData) => {
    setFormData((prev) => ({
      ...prev,
      location: presetData.location,
      type: presetData.type,
      description: presetData.description
    }));
    setQrDetected(true);
  };

  return (
    <div className="container">
      {/* Hero Header */}
      <div className="hero-section">
        <span className="hero-pill">🚨 24/7 Rapid Emergency Response</span>
        <h1 className="hero-title">Roadside Assistance Portal</h1>
        <p className="hero-subtitle">Fast, reliable breakdown recovery and technician dispatch when you need it most.</p>

        {/* Action button to open QR Generator */}
        <div style={{ marginTop: '1.5rem', display: 'flex', justifyContent: 'center', gap: '1rem', flexWrap: 'wrap' }}>
          <button
            type="button"
            className="secondary-btn"
            onClick={() => setIsQrModalOpen(true)}
            style={{ display: 'inline-flex', alignItems: 'center', gap: '0.5rem', padding: '0.65rem 1.25rem' }}
          >
            🪧 <strong>Highway QR Placard Generator</strong>
          </button>
        </div>
      </div>

      {/* Emergency Request Form Card */}
      <div className="emergency-card-wrapper">
        <div className="card emergency-card">
          <div className="emergency-card-header">
            <span className="emergency-icon">⚠️</span>
            <h2>Emergency Assistance Request</h2>
            <p>Immediate 1-Click Dispatch — No Registration Required</p>
          </div>

          {/* QR Scan Banner Notification */}
          {qrDetected && (
            <div className="qr-detected-banner">
              <div className="qr-banner-icon">📍</div>
              <div className="qr-banner-text">
                <strong>Highway Placard Auto-Filled</strong>
                <span>Location and incident type pre-populated from highway marker.</span>
              </div>
              <button
                type="button"
                className="qr-banner-clear"
                onClick={() => setQrDetected(false)}
                title="Dismiss banner"
              >
                ✕
              </button>
            </div>
          )}

          {error && <div className="error-banner">{error}</div>}

          <form onSubmit={handleSubmit} className="emergency-form">
            <div className="form-row">
              <div className="form-group flex-1">
                <label htmlFor="input-name">Your Full Name <span className="req">*</span></label>
                <input
                  id="input-name"
                  type="text"
                  name="name"
                  required
                  value={formData.name}
                  onChange={handleChange}
                  placeholder="e.g. John Doe"
                  autoComplete="name"
                />
              </div>

              <div className="form-group flex-1">
                <label htmlFor="input-phone">Phone Number <span className="req">*</span></label>
                <input
                  id="input-phone"
                  type="tel"
                  name="phone"
                  required
                  value={formData.phone}
                  onChange={handleChange}
                  placeholder="e.g. +91 98765 43210"
                  autoComplete="tel"
                />
              </div>
            </div>

            <div className="form-group">
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.25rem' }}>
                <label htmlFor="input-location" style={{ margin: 0 }}>Breakdown Location <span className="req">*</span></label>
                {formData.location && (
                  <span style={{ fontSize: '0.75rem', color: 'var(--success)', fontWeight: '600' }}>
                    ✓ Location Captured
                  </span>
                )}
              </div>
              <input
                id="input-location"
                type="text"
                name="location"
                required
                value={formData.location}
                onChange={handleChange}
                placeholder="e.g. Mumbai-Pune Expressway, Km 42 or Western Express Hwy"
              />
            </div>

            <div className="form-group">
              <label htmlFor="select-type">Incident Type <span className="req">*</span></label>
              <select id="select-type" name="type" value={formData.type} onChange={handleChange}>
                <option value="FLAT_TIRE">🛞 Flat Tire Assistance</option>
                <option value="ENGINE_FAILURE">🔧 Engine Breakdown / Towing</option>
                <option value="ACCIDENT">🚑 Traffic Accident / Multi-Agency</option>
                <option value="LOCKOUT">🔑 Vehicle Lockout Service</option>
                <option value="FUEL_EMPTY">⛽ Emergency Fuel Delivery</option>
              </select>
            </div>

            <div className="form-group">
              <label htmlFor="textarea-desc">Description & Landmark (Optional)</label>
              <textarea
                id="textarea-desc"
                name="description"
                value={formData.description}
                onChange={handleChange}
                rows="3"
                placeholder="e.g. White SUV parked on left shoulder with hazard lights on"
              />
            </div>

            <button
              type="submit"
              className="danger submit-btn"
              disabled={loading}
            >
              {loading ? (
                <span>⏳ Dispatching Rescue Team...</span>
              ) : (
                <span>🚀 Request Emergency Assistance Now</span>
              )}
            </button>
          </form>

          {/* Quick Info Badges */}
          <div className="emergency-perks">
            <div className="perk-item">
              <span>⏱️</span>
              <p>Average dispatch response &lt; 5 mins</p>
            </div>
            <div className="perk-item">
              <span>💬</span>
              <p>Live driver-technician chat</p>
            </div>
            <div className="perk-item">
              <span>🛡️</span>
              <p>Verified certified highway patrol</p>
            </div>
          </div>
        </div>
      </div>

      {/* Highway QR Placard Modal */}
      <QrPlacardModal
        isOpen={isQrModalOpen}
        onClose={() => setIsQrModalOpen(false)}
        onApplyPreset={handleApplyPreset}
      />
    </div>
  );
};

export default Landing;

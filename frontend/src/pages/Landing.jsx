import React, { useState, useEffect } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
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
      navigate(`/emergency/status?token=${res.guestToken}`);
    } catch (err) {
      setError(err.response?.data?.message || 'Failed to submit emergency dispatch request.');
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
    <div className="container main-container">
      {/* Formal Header Section */}
      <section className="portal-header-section">
        <div className="section-eyebrow">HIGHWAY EMERGENCY DISPATCH SYSTEM</div>
        <h1 className="portal-title">Roadside Assistance Portal</h1>
        <p className="portal-subtitle">
          Rapid breakdown response and certified emergency assistance dispatch across highway corridors.
        </p>

        <div className="header-actions">
          <button
            type="button"
            className="btn-outline"
            onClick={() => setIsQrModalOpen(true)}
          >
            Highway Mile Marker Placard Tool
          </button>
        </div>
      </section>

      {/* Main Intake Card */}
      <div className="form-card-wrapper">
        <div className="card intake-card">
          <div className="card-header-bar">
            <div>
              <h2 className="card-title">Dispatch Request Form</h2>
              <p className="card-desc">Public Emergency Access &bull; Direct Queue Routing</p>
            </div>
            <span className="live-status-badge">
              <span className="status-indicator-dot"></span> System Operational
            </span>
          </div>

          {/* QR Detected Banner */}
          {qrDetected && (
            <div className="alert-box alert-success">
              <div className="alert-content">
                <strong>Highway Marker Parameter Detected</strong>
                <p>Location and service requirements have been pre-populated from the highway marker.</p>
              </div>
              <button
                type="button"
                className="alert-close-btn"
                onClick={() => setQrDetected(false)}
                aria-label="Dismiss notice"
              >
                Dismiss
              </button>
            </div>
          )}

          {error && (
            <div className="alert-box alert-danger">
              <strong>Error:</strong> {error}
            </div>
          )}

          <form onSubmit={handleSubmit} className="intake-form">
            <div className="form-grid-row">
              <div className="form-field flex-1">
                <label htmlFor="input-name">
                  Full Name <span className="required-star">*</span>
                </label>
                <input
                  id="input-name"
                  type="text"
                  name="name"
                  required
                  value={formData.name}
                  onChange={handleChange}
                  placeholder="Enter caller or driver name"
                  autoComplete="name"
                />
              </div>

              <div className="form-field flex-1">
                <label htmlFor="input-phone">
                  Contact Phone Number <span className="required-star">*</span>
                </label>
                <input
                  id="input-phone"
                  type="tel"
                  name="phone"
                  required
                  value={formData.phone}
                  onChange={handleChange}
                  placeholder="Mobile contact number"
                  autoComplete="tel"
                />
              </div>
            </div>

            <div className="form-field">
              <div className="field-label-group">
                <label htmlFor="input-location">
                  Breakdown Location <span className="required-star">*</span>
                </label>
                {formData.location && (
                  <span className="field-verified-text">Location set</span>
                )}
              </div>
              <input
                id="input-location"
                type="text"
                name="location"
                required
                value={formData.location}
                onChange={handleChange}
                placeholder="Expressway corridor, mile marker, or nearest landmark"
              />
            </div>

            <div className="form-field">
              <label htmlFor="select-type">
                Service Category <span className="required-star">*</span>
              </label>
              <select id="select-type" name="type" value={formData.type} onChange={handleChange}>
                <option value="FLAT_TIRE">Flat Tire Replacement</option>
                <option value="ENGINE_FAILURE">Mechanical Breakdown / Towing</option>
                <option value="ACCIDENT">Collision / Traffic Incident</option>
                <option value="LOCKOUT">Vehicle Lockout Assistance</option>
                <option value="FUEL_EMPTY">Emergency Fuel Delivery</option>
              </select>
            </div>

            <div className="form-field">
              <label htmlFor="textarea-desc">
                Incident Description & Additional Landmarks (Optional)
              </label>
              <textarea
                id="textarea-desc"
                name="description"
                value={formData.description}
                onChange={handleChange}
                rows="3"
                placeholder="Provide vehicle make/model, shoulder location, or hazard details"
              />
            </div>

            <div className="form-actions">
              <button
                type="submit"
                className="btn-danger submit-dispatch-btn"
                disabled={loading}
              >
                {loading ? 'Transmitting Dispatch...' : 'Dispatch Emergency Assistance Unit'}
              </button>
            </div>
          </form>

          <div className="intake-footer-notes">
            <div className="footer-note-item">
              <strong>Priority Routing</strong>
              <span>Immediate dispatch to designated highway patrol</span>
            </div>
            <div className="footer-note-item">
              <strong>Direct Communication</strong>
              <span>Encrypted live connection with dispatched unit</span>
            </div>
            <div className="footer-note-item">
              <strong>Coverage Guarantee</strong>
              <span>Standard operating response under regional SLA</span>
            </div>
          </div>
        </div>
      </div>

      {/* Highway Placard Modal */}
      <QrPlacardModal
        isOpen={isQrModalOpen}
        onClose={() => setIsQrModalOpen(false)}
        onApplyPreset={handleApplyPreset}
      />
    </div>
  );
};

export default Landing;

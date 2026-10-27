import React, { useState } from 'react';
import { QRCodeSVG } from 'qrcode.react';

const PRESETS = [
  {
    title: 'NH-48 Expressway Km 42',
    subtitle: 'Mumbai-Pune Expressway (Mile 42)',
    location: 'Mumbai-Pune Expressway, Km 42 (Westbound)',
    type: 'FLAT_TIRE',
    desc: 'Emergency Mile Marker 42. Driver stranded in emergency lane.'
  },
  {
    title: 'Western Express Highway Exit 7',
    subtitle: 'Kandivali Flyover Northbound',
    location: 'Western Express Highway, Exit 7 (Kandivali)',
    type: 'ENGINE_FAILURE',
    desc: 'Vehicle stalled near exit ramp. Hazard lights active.'
  },
  {
    title: 'Bandra-Worli Sea Link Toll',
    subtitle: 'Southbound Toll Plaza Bay 4',
    location: 'Bandra-Worli Sea Link, Southbound Toll Bay 4',
    type: 'FUEL_EMPTY',
    desc: 'Fuel emergency at toll approach.'
  }
];

const QrPlacardModal = ({ isOpen, onClose, onApplyPreset }) => {
  if (!isOpen) return null;

  const [selectedPresetIndex, setSelectedPresetIndex] = useState(0);
  const [customLocation, setCustomLocation] = useState('');
  const [customType, setCustomType] = useState('FLAT_TIRE');
  const [isCustom, setIsCustom] = useState(false);

  // Default to live cloud host if on localhost so phone cameras can scan it worldwide
  const currentOrigin = window.location.origin;
  const defaultHost = currentOrigin.includes('localhost') 
    ? 'http://15.252.18.123' 
    : currentOrigin;

  const [targetHost, setTargetHost] = useState(defaultHost);

  const activePreset = PRESETS[selectedPresetIndex];
  const activeLocation = isCustom ? (customLocation || 'Highway Marker 101') : activePreset.location;
  const activeType = isCustom ? customType : activePreset.type;
  const activeDesc = isCustom ? 'Custom highway emergency scan' : activePreset.desc;

  // Construct query URL
  const queryParams = new URLSearchParams({
    loc: activeLocation,
    type: activeType,
    desc: activeDesc
  });

  const fullQrUrl = `${targetHost}/?${queryParams.toString()}`;

  const handleSimulateScan = () => {
    if (onApplyPreset) {
      onApplyPreset({
        location: activeLocation,
        type: activeType,
        description: activeDesc
      });
    }
    onClose();
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content placard-modal" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <div>
            <h2>🪧 Highway Emergency QR Placard</h2>
            <p className="subtitle">Scan with your smartphone camera to auto-fill location & dispatch</p>
          </div>
          <button className="close-btn" onClick={onClose} aria-label="Close modal">✕</button>
        </div>

        <div className="placard-grid">
          {/* Left Column: Placard Visual Display */}
          <div className="placard-card">
            <div className="placard-top-bar">
              <span className="placard-badge">HIGHWAY SOS SYSTEM</span>
              <span className="placard-sub">SCAN FOR IMMEDIATE DISPATCH</span>
            </div>

            <div className="qr-container">
              <QRCodeSVG
                value={fullQrUrl}
                size={210}
                level="H"
                includeMargin={true}
                fgColor="#0f172a"
              />
            </div>

            <div className="placard-info">
              <div className="placard-loc-label">LOCATION MARKER</div>
              <div className="placard-loc-value">{activeLocation}</div>
              <div className="placard-type-pill">ISSUE: {activeType.replace('_', ' ')}</div>
            </div>

            <div className="placard-instructions">
              Point phone camera at QR code. No app download required.
            </div>
          </div>

          {/* Right Column: Controls & Presets */}
          <div className="placard-controls">
            <div className="control-group">
              <label>Select Highway Preset Marker:</label>
              <div className="preset-buttons">
                {PRESETS.map((p, idx) => (
                  <button
                    key={p.title}
                    type="button"
                    className={`preset-btn ${!isCustom && selectedPresetIndex === idx ? 'active' : ''}`}
                    onClick={() => {
                      setSelectedPresetIndex(idx);
                      setIsCustom(false);
                    }}
                  >
                    <strong>{p.title}</strong>
                    <span>{p.subtitle}</span>
                  </button>
                ))}
              </div>
            </div>

            <div className="control-group">
              <label>
                <input
                  type="checkbox"
                  checked={isCustom}
                  onChange={(e) => setIsCustom(e.target.checked)}
                  style={{ width: 'auto', marginRight: '0.5rem' }}
                />
                Use Custom Marker / Location
              </label>

              {isCustom && (
                <div className="custom-fields">
                  <input
                    type="text"
                    placeholder="e.g. NH-48 Expressway Exit 12"
                    value={customLocation}
                    onChange={(e) => setCustomLocation(e.target.value)}
                  />
                  <select value={customType} onChange={(e) => setCustomType(e.target.value)}>
                    <option value="FLAT_TIRE">Flat Tire</option>
                    <option value="ENGINE_FAILURE">Engine Failure</option>
                    <option value="ACCIDENT">Accident</option>
                    <option value="LOCKOUT">Lockout</option>
                    <option value="FUEL_EMPTY">Out of Fuel</option>
                  </select>
                </div>
              )}
            </div>

            <div className="control-group">
              <label>Target Domain / Host (for QR URL):</label>
              <input
                type="text"
                value={targetHost}
                onChange={(e) => setTargetHost(e.target.value)}
                placeholder="http://15.252.18.123"
              />
              <small className="help-text">
                Tip: When testing on phone camera, use your AWS Public IP so phone can connect.
              </small>
            </div>

            <div className="placard-actions">
              <button
                type="button"
                className="primary"
                onClick={handleSimulateScan}
                style={{ width: '100%', marginBottom: '0.5rem' }}
              >
                ⚡ Simulate Mobile Scan (Apply Pre-fill Now)
              </button>
              <button
                type="button"
                onClick={onClose}
                style={{ width: '100%', backgroundColor: '#e2e8f0', color: '#1e293b' }}
              >
                Close Placard
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default QrPlacardModal;

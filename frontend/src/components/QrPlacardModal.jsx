import React, { useState } from 'react';
import { QRCodeSVG } from 'qrcode.react';

const HIGHWAY_SECTORS = [
  {
    title: 'Sector 4 - NH-48 Expressway Km 42',
    subtitle: 'Corridor: Mumbai-Pune Western Approach',
    location: 'Mumbai-Pune Expressway, Km 42 (Westbound)',
    type: 'FLAT_TIRE',
    desc: 'Marker 42. Vehicle stationed on outer shoulder.'
  },
  {
    title: 'Sector 12 - Western Corridor Exit 7',
    subtitle: 'Corridor: Kandivali North Interchange',
    location: 'Western Express Highway, Exit 7 (Kandivali)',
    type: 'ENGINE_FAILURE',
    desc: 'Mechanical failure on exit ramp approach.'
  },
  {
    title: 'Sector 1 - Coastal Highway Toll Plaza',
    subtitle: 'Corridor: Sea Link Southbound Bay 4',
    location: 'Bandra-Worli Sea Link, Southbound Toll Bay 4',
    type: 'FUEL_EMPTY',
    desc: 'Fuel depletion incident near toll approach.'
  }
];

const QrPlacardModal = ({ isOpen, onClose, onApplyPreset }) => {
  if (!isOpen) return null;

  const [selectedPresetIndex, setSelectedPresetIndex] = useState(0);
  const [customLocation, setCustomLocation] = useState('');
  const [customType, setCustomType] = useState('FLAT_TIRE');
  const [isCustom, setIsCustom] = useState(false);

  const currentOrigin = window.location.origin;
  const defaultHost = currentOrigin.includes('localhost') 
    ? 'http://15.252.18.123' 
    : currentOrigin;

  const [targetHost, setTargetHost] = useState(defaultHost);

  const activeSector = HIGHWAY_SECTORS[selectedPresetIndex];
  const activeLocation = isCustom ? (customLocation || 'Highway Sector Marker 101') : activeSector.location;
  const activeType = isCustom ? customType : activeSector.type;
  const activeDesc = isCustom ? 'Custom highway emergency intake' : activeSector.desc;

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
      <div className="modal-content placard-modal-container" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header-bar">
          <div>
            <h2 className="modal-heading">Highway Emergency Marker Placard</h2>
            <p className="modal-subheading">Standard roadside emergency QR placard specification</p>
          </div>
          <button className="btn-close-modal" onClick={onClose} aria-label="Close dialog">
            Close
          </button>
        </div>

        <div className="placard-layout-grid">
          {/* Official Highway Placard Sign */}
          <div className="dot-placard-sign">
            <div className="dot-placard-header">
              <span className="dot-authority">EMERGENCY ASSISTANCE CALL POST</span>
              <span className="dot-code">SECTOR ID #{selectedPresetIndex + 101}</span>
            </div>

            <div className="dot-qr-surface">
              <QRCodeSVG
                value={fullQrUrl}
                size={200}
                level="H"
                includeMargin={true}
                fgColor="#0f172a"
              />
            </div>

            <div className="dot-marker-details">
              <div className="dot-meta-label">DESIGNATED LOCATION</div>
              <div className="dot-location-text">{activeLocation}</div>
              <div className="dot-service-indicator">SERVICE: {activeType.replace('_', ' ')}</div>
            </div>

            <div className="dot-placard-footer">
              Scan with mobile device camera to open immediate dispatch intake.
            </div>
          </div>

          {/* Configuration & Controls */}
          <div className="placard-options-panel">
            <div className="option-section">
              <label className="section-title-label">Highway Marker Presets:</label>
              <div className="sector-list">
                {HIGHWAY_SECTORS.map((sector, idx) => (
                  <button
                    key={sector.title}
                    type="button"
                    className={`sector-option-btn ${!isCustom && selectedPresetIndex === idx ? 'selected' : ''}`}
                    onClick={() => {
                      setSelectedPresetIndex(idx);
                      setIsCustom(false);
                    }}
                  >
                    <div className="sector-btn-title">{sector.title}</div>
                    <div className="sector-btn-sub">{sector.subtitle}</div>
                  </button>
                ))}
              </div>
            </div>

            <div className="option-section">
              <label className="checkbox-toggle-label">
                <input
                  type="checkbox"
                  checked={isCustom}
                  onChange={(e) => setIsCustom(e.target.checked)}
                />
                Define Custom Mile Marker / Coordinates
              </label>

              {isCustom && (
                <div className="custom-marker-inputs">
                  <input
                    type="text"
                    placeholder="e.g. NH-48 Mile Marker 58 (Eastbound)"
                    value={customLocation}
                    onChange={(e) => setCustomLocation(e.target.value)}
                  />
                  <select value={customType} onChange={(e) => setCustomType(e.target.value)}>
                    <option value="FLAT_TIRE">Flat Tire Replacement</option>
                    <option value="ENGINE_FAILURE">Mechanical Breakdown / Towing</option>
                    <option value="ACCIDENT">Collision / Traffic Incident</option>
                    <option value="LOCKOUT">Vehicle Lockout Assistance</option>
                    <option value="FUEL_EMPTY">Emergency Fuel Delivery</option>
                  </select>
                </div>
              )}
            </div>

            <div className="option-section">
              <label className="section-title-label">Target Dispatch Portal Host:</label>
              <input
                type="text"
                value={targetHost}
                onChange={(e) => setTargetHost(e.target.value)}
                placeholder="http://15.252.18.123"
              />
              <span className="field-hint">
                Configures the target URL encoded in the QR code for external camera scanning.
              </span>
            </div>

            <div className="panel-button-row">
              <button
                type="button"
                className="btn-primary flex-1"
                onClick={handleSimulateScan}
              >
                Simulate Scanned Intake
              </button>
              <button
                type="button"
                className="btn-secondary"
                onClick={onClose}
              >
                Dismiss
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default QrPlacardModal;

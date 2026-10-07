import React from 'react';

const StatusBadge = ({ status }) => {
  const getStyle = () => {
    switch (status) {
      case 'REQUESTED': return { bg: '#fef3c7', color: '#d97706' }; // yellow
      case 'AUTO_ASSIGNED': return { bg: '#dbeafe', color: '#2563eb' }; // blue
      case 'IN_PROGRESS': return { bg: '#ffedd5', color: '#ea580c' }; // orange
      case 'RESOLVED': return { bg: '#dcfce7', color: '#16a34a' }; // green
      case 'CLOSED': return { bg: '#f1f5f9', color: '#475569' }; // gray
      case 'CANCELLED': return { bg: '#fee2e2', color: '#dc2626' }; // red
      default: return { bg: '#f1f5f9', color: '#475569' };
    }
  };

  const style = getStyle();

  return (
    <span style={{
      backgroundColor: style.bg,
      color: style.color,
      padding: '0.25rem 0.75rem',
      borderRadius: '9999px',
      fontSize: '0.875rem',
      fontWeight: 'bold',
      display: 'inline-block'
    }}>
      {status}
    </span>
  );
};

export default StatusBadge;

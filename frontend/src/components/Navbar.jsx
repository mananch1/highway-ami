import React, { useContext, useState } from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';

const Navbar = () => {
  const { isAuthenticated, user, logout } = useContext(AuthContext);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();

  const handleLogout = () => {
    logout();
    setMobileMenuOpen(false);
    navigate('/');
  };

  const closeMenu = () => setMobileMenuOpen(false);

  const getDashboardLink = () => {
    if (!user) return '/';
    switch (user.role) {
      case 'CUSTOMER': return '/customer';
      case 'TECHNICIAN': return '/technician';
      case 'ADMIN': return '/admin';
      default: return '/';
    }
  };

  return (
    <header className="navbar-header">
      <div className="container navbar-container">
        {/* Brand */}
        <Link to="/" className="navbar-brand" onClick={closeMenu}>
          <span className="brand-icon">🚗</span>
          <span className="brand-name">Road Helper</span>
          <span className="brand-tag">SOS</span>
        </Link>

        {/* Mobile Hamburger Toggle Button */}
        <button
          type="button"
          className="mobile-toggle-btn"
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          aria-label="Toggle navigation menu"
        >
          {mobileMenuOpen ? '✕' : '☰'}
        </button>

        {/* Navigation Links */}
        <nav className={`navbar-links ${mobileMenuOpen ? 'mobile-open' : ''}`}>
          <Link
            to="/"
            className={`nav-link ${location.pathname === '/' ? 'active' : ''}`}
            onClick={closeMenu}
          >
            🚨 Emergency
          </Link>

          {isAuthenticated ? (
            <>
              <Link
                to={getDashboardLink()}
                className={`nav-link ${location.pathname === getDashboardLink() ? 'active' : ''}`}
                onClick={closeMenu}
              >
                📊 Dashboard
              </Link>
              <Link
                to="/search"
                className={`nav-link ${location.pathname === '/search' ? 'active' : ''}`}
                onClick={closeMenu}
              >
                🔍 Search
              </Link>
              <div className="user-badge">
                <span className="user-name">{user?.name}</span>
                <span className="user-role-pill">{user?.role}</span>
              </div>
              <button
                type="button"
                className="danger logout-btn"
                onClick={handleLogout}
              >
                Logout
              </button>
            </>
          ) : (
            <div className="auth-buttons">
              <Link to="/login" className="nav-link login-link" onClick={closeMenu}>
                Login
              </Link>
              <Link to="/register" className="register-btn" onClick={closeMenu}>
                Sign Up
              </Link>
            </div>
          )}
        </nav>
      </div>
    </header>
  );
};

export default Navbar;

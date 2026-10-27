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
          <div className="brand-mark">RH</div>
          <div className="brand-text-group">
            <span className="brand-name">RoadHelper</span>
            <span className="brand-sub">DISPATCH PORTAL</span>
          </div>
        </Link>

        {/* Mobile Hamburger Toggle Button */}
        <button
          type="button"
          className="mobile-toggle-btn"
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          aria-label="Toggle navigation menu"
        >
          <span className="hamburger-icon"></span>
        </button>

        {/* Navigation Links */}
        <nav className={`navbar-links ${mobileMenuOpen ? 'mobile-open' : ''}`}>
          <Link
            to="/"
            className={`nav-link ${location.pathname === '/' ? 'active' : ''}`}
            onClick={closeMenu}
          >
            Emergency Intake
          </Link>

          {isAuthenticated ? (
            <>
              <Link
                to={getDashboardLink()}
                className={`nav-link ${location.pathname === getDashboardLink() ? 'active' : ''}`}
                onClick={closeMenu}
              >
                Console
              </Link>
              <Link
                to="/search"
                className={`nav-link ${location.pathname === '/search' ? 'active' : ''}`}
                onClick={closeMenu}
              >
                Search Records
              </Link>
              <div className="user-profile-badge">
                <span className="user-name">{user?.name}</span>
                <span className="user-role-badge">{user?.role}</span>
              </div>
              <button
                type="button"
                className="btn-secondary btn-sm"
                onClick={handleLogout}
              >
                Sign Out
              </button>
            </>
          ) : (
            <div className="auth-group">
              <Link to="/login" className="nav-link login-nav-link" onClick={closeMenu}>
                Operator Sign In
              </Link>
              <Link to="/register" className="btn-primary btn-sm" onClick={closeMenu}>
                Create Account
              </Link>
            </div>
          )}
        </nav>
      </div>
    </header>
  );
};

export default Navbar;

import React, { useContext } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';

const Navbar = () => {
  const { isAuthenticated, user, logout } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/');
  };

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
    <nav style={styles.nav}>
      <div className="container" style={styles.container}>
        <Link to="/" style={styles.brand}>Road Helper</Link>
        
        <div style={styles.links}>
          {isAuthenticated ? (
            <>
              <span style={styles.userInfo}>{user?.name} ({user?.role})</span>
              <Link to={getDashboardLink()} style={styles.link}>Dashboard</Link>
              <Link to="/search" style={styles.link}>Search</Link>
              <button className="danger" onClick={handleLogout}>Logout</button>
            </>
          ) : (
            <>
              <Link to="/login" style={styles.link}>Login</Link>
              <Link to="/register" style={styles.link}>Register</Link>
            </>
          )}
        </div>
      </div>
    </nav>
  );
};

const styles = {
  nav: {
    backgroundColor: '#ffffff',
    borderBottom: '1px solid var(--border)',
    padding: '1rem 0'
  },
  container: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center'
  },
  brand: {
    fontSize: '1.5rem',
    fontWeight: 'bold',
    color: 'var(--primary)'
  },
  links: {
    display: 'flex',
    gap: '1.5rem',
    alignItems: 'center'
  },
  link: {
    fontWeight: '500',
    color: 'var(--text-main)'
  },
  userInfo: {
    color: 'var(--text-muted)',
    fontSize: '0.9rem'
  }
};

export default Navbar;

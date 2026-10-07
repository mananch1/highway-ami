import React, { useContext } from 'react';
import { Navigate } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';

const ProtectedRoute = ({ children, requiredRole }) => {
  const { isAuthenticated, loading, user } = useContext(AuthContext);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (!isAuthenticated) {
    return <Navigate to="/login" />;
  }

  if (requiredRole && user?.role !== requiredRole) {
    // redirect to their respective dashboard if they try to access wrong role route
    let redirectPath = '/';
    if (user?.role === 'CUSTOMER') redirectPath = '/customer';
    if (user?.role === 'TECHNICIAN') redirectPath = '/technician';
    if (user?.role === 'ADMIN') redirectPath = '/admin';
    return <Navigate to={redirectPath} />;
  }

  return children;
};

export default ProtectedRoute;

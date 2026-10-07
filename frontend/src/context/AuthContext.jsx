import React, { createContext, useState, useEffect } from 'react';
import { login as apiLogin } from '../api/api';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem('token'));
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // If we have a token, we parse user info from localStorage if available
    const storedUser = localStorage.getItem('user');
    if (token && storedUser) {
      setUser(JSON.parse(storedUser));
    } else if (!token) {
      setUser(null);
    }
    setLoading(false);
  }, [token]);

  const login = async (email, password) => {
    const data = await apiLogin(email, password);
    const { token, role, name, userId } = data;
    const userData = { role, name, userId };
    
    localStorage.setItem('token', token);
    localStorage.setItem('user', JSON.stringify(userData));
    
    setToken(token);
    setUser(userData);
    return data;
  };
  
  const loginWithData = (data) => {
    const { token, role, name, userId } = data;
    const userData = { role, name, userId };
    
    localStorage.setItem('token', token);
    localStorage.setItem('user', JSON.stringify(userData));
    
    setToken(token);
    setUser(userData);
  }

  const logout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    setToken(null);
    setUser(null);
  };

  const isAuthenticated = !!token;

  return (
    <AuthContext.Provider value={{ user, token, isAuthenticated, login, loginWithData, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

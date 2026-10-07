import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import Navbar from './components/Navbar';
import ProtectedRoute from './components/ProtectedRoute';

// Pages
import Landing from './pages/Landing';
import Login from './pages/Login';
import Register from './pages/Register';
import EmergencyStatus from './pages/EmergencyStatus';
import CustomerDashboard from './pages/CustomerDashboard';
import TechnicianDashboard from './pages/TechnicianDashboard';
import AdminDashboard from './pages/AdminDashboard';
import IncidentDetail from './pages/IncidentDetail';
import CreateIncident from './pages/CreateIncident';
import Search from './pages/Search';

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="app">
          <Navbar />
          <main className="main-content">
            <Routes>
              {/* Public Routes */}
              <Route path="/" element={<Landing />} />
              <Route path="/login" element={<Login />} />
              <Route path="/register" element={<Register />} />
              <Route path="/emergency/status" element={<EmergencyStatus />} />

              {/* Protected Routes - General (Any logged-in user) */}
              <Route path="/search" element={
                <ProtectedRoute>
                  <Search />
                </ProtectedRoute>
              } />
              <Route path="/incidents/:id" element={
                <ProtectedRoute>
                  <IncidentDetail />
                </ProtectedRoute>
              } />

              {/* Protected Routes - Customer Only */}
              <Route path="/customer" element={
                <ProtectedRoute requiredRole="CUSTOMER">
                  <CustomerDashboard />
                </ProtectedRoute>
              } />
              <Route path="/create-incident" element={
                <ProtectedRoute requiredRole="CUSTOMER">
                  <CreateIncident />
                </ProtectedRoute>
              } />

              {/* Protected Routes - Technician Only */}
              <Route path="/technician" element={
                <ProtectedRoute requiredRole="TECHNICIAN">
                  <TechnicianDashboard />
                </ProtectedRoute>
              } />

              {/* Protected Routes - Admin Only */}
              <Route path="/admin" element={
                <ProtectedRoute requiredRole="ADMIN">
                  <AdminDashboard />
                </ProtectedRoute>
              } />
            </Routes>
          </main>
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;

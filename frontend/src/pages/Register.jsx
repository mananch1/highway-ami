import React, { useState, useContext } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { register } from '../api/api';
import { AuthContext } from '../context/AuthContext';

const Register = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    role: 'CUSTOMER'
  });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  
  const { loginWithData } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    try {
      const data = await register(formData.name, formData.email, formData.password, formData.role);
      loginWithData(data);
      if (data.role === 'CUSTOMER') navigate('/customer');
      else if (data.role === 'TECHNICIAN') navigate('/technician');
    } catch (err) {
      setError(err.response?.data?.message || 'Registration failed.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-container card">
      <h2>Register</h2>
      {error && <div style={{ color: 'var(--danger)', marginBottom: '1rem', textAlign: 'center' }}>{error}</div>}
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Full Name</label>
          <input type="text" name="name" required value={formData.name} onChange={handleChange} />
        </div>
        <div className="form-group">
          <label>Email</label>
          <input type="email" name="email" required value={formData.email} onChange={handleChange} />
        </div>
        <div className="form-group">
          <label>Password</label>
          <input type="password" name="password" required value={formData.password} onChange={handleChange} />
        </div>
        <div className="form-group">
          <label>Role</label>
          <select name="role" value={formData.role} onChange={handleChange}>
            <option value="CUSTOMER">Customer</option>
            <option value="TECHNICIAN">Technician</option>
          </select>
        </div>
        <button type="submit" className="primary" style={{ width: '100%' }} disabled={loading}>
          {loading ? 'Registering...' : 'Register'}
        </button>
      </form>
      <div style={{ textAlign: 'center', marginTop: '1rem' }}>
        <p>Already have an account? <Link to="/login">Login here</Link></p>
      </div>
    </div>
  );
};

export default Register;

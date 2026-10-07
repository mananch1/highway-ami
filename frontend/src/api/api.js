import axios from 'axios';

const api = axios.create({
  baseURL: '' // Same origin
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
}, (error) => {
  return Promise.reject(error);
});

export const login = async (email, password) => {
  const res = await api.post('/api/v1/auth/login', { email, password });
  return res.data;
};

export const register = async (name, email, password, role) => {
  const res = await api.post('/api/v1/auth/register', { name, email, password, role });
  return res.data;
};

export const createEmergency = async (data) => {
  const res = await api.post('/api/v1/emergency', data);
  return res.data;
};

export const getEmergencyStatus = async (token) => {
  const res = await api.get(`/api/v1/emergency/status?token=${token}`);
  return res.data;
};

export const getIncidents = async () => {
  const res = await api.get('/api/v1/incidents');
  return res.data;
};

export const createIncident = async (data) => {
  const res = await api.post('/api/v1/incidents', data);
  return res.data;
};

export const getIncident = async (id) => {
  const res = await api.get(`/api/v1/incidents/${id}`);
  return res.data;
};

export const searchIncidents = async (query) => {
  const res = await api.get(`/api/v1/incidents/search?query=${encodeURIComponent(query)}`);
  return res.data;
};

export const updateIncidentStatus = async (id, status) => {
  const res = await api.patch(`/api/v1/incidents/${id}/status`, { status });
  return res.data;
};

export const getDashboardSummary = async () => {
  const res = await api.get('/api/v1/dashboard/summary');
  return res.data;
};

export const getUsers = async () => {
  const res = await api.get('/api/v1/users');
  return res.data;
};

export const toggleAvailability = async (userId) => {
  const res = await api.patch(`/api/v1/users/${userId}/availability`);
  return res.data;
};

export const getChatMessages = async (incidentId) => {
  const res = await api.get(`/api/v1/incidents/${incidentId}/chat`);
  return res.data;
};

export default api;

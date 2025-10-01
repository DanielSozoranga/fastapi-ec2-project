import axios from 'axios';

// Para desarrollo local
const API_BASE_URL = 'ip-172-31-23-133.ec2.internal';

const api = axios.create({
  baseURL: API_BASE_URL,
});

export const taskService = {
  getTasks: async () => {
    const response = await api.get('/tasks');
    return response.data;
  },

  createTask: async (task) => {
    const response = await api.post('/tasks', task);
    return response.data;
  },

  updateTask: async (id, task) => {
    const response = await api.put(`/tasks/${id}`, task);
    return response.data;
  },

  deleteTask: async (id) => {
    const response = await api.delete(`/tasks/${id}`);
    return response.data;
  },
};

export default api;
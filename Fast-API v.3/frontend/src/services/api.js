import axios from 'axios';

const API_BASE_URL = 'http://localhost:8080';

const api = axios.create({
  baseURL: API_BASE_URL,
});

export const taskService = {
  // Obtener todas las tareas
  getTasks: async () => {
    const response = await api.get('/tasks');
    return response.data;
  },

  // Obtener una tarea por ID
  getTask: async (id) => {
    const response = await api.get(`/tasks/${id}`);
    return response.data;
  },

  // Crear una nueva tarea
  createTask: async (task) => {
    const response = await api.post('/tasks', task);
    return response.data;
  },

  // Actualizar una tarea
  updateTask: async (id, task) => {
    const response = await api.put(`/tasks/${id}`, task);
    return response.data;
  },

  // Eliminar una tarea
  deleteTask: async (id) => {
    const response = await api.delete(`/tasks/${id}`);
    return response.data;
  },
};

export default api;
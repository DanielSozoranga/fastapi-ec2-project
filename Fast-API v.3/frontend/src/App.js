import React, { useState, useEffect } from 'react';
import { taskService } from './services/api';
import TaskForm from './components/TaskForm';
import TaskList from './components/TaskList';
import './App.css';

function App() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Cargar tareas al iniciar
  useEffect(() => {
    loadTasks();
  }, []);

  const loadTasks = async () => {
    try {
      setLoading(true);
      const tasksData = await taskService.getTasks();
      setTasks(tasksData);
      setError('');
    } catch (error) {
      console.error('Error loading tasks:', error);
      setError('Error al cargar las tareas. Verifica que el backend esté corriendo.');
    } finally {
      setLoading(false);
    }
  };

  const handleTaskCreated = async (newTask) => {
    try {
      const createdTask = await taskService.createTask(newTask);
      setTasks(prevTasks => [...prevTasks, createdTask]);
    } catch (error) {
      console.error('Error creating task:', error);
      setError('Error al crear la tarea');
    }
  };

  const handleTaskUpdated = async (taskId, updatedData) => {
    try {
      const updatedTask = await taskService.updateTask(taskId, updatedData);
      setTasks(prevTasks => 
        prevTasks.map(task => task.id === taskId ? updatedTask : task)
      );
    } catch (error) {
      console.error('Error updating task:', error);
      setError('Error al actualizar la tarea');
    }
  };

  const handleTaskDeleted = async (taskId) => {
    try {
      await taskService.deleteTask(taskId);
      setTasks(prevTasks => prevTasks.filter(task => task.id !== taskId));
    } catch (error) {
      console.error('Error deleting task:', error);
      setError('Error al eliminar la tarea');
    }
  };

  if (loading) {
    return <div className="app">Cargando...</div>;
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>📝 ToDo App</h1>
        <p>Gestiona tus tareas de forma sencilla</p>
      </header>

      {error && (
        <div className="error-message">
          {error}
          <button onClick={() => setError('')}>×</button>
        </div>
      )}

      <main className="app-main">
        <div className="container">
          <TaskForm onTaskCreated={handleTaskCreated} />
          <TaskList 
            tasks={tasks}
            onTaskUpdated={handleTaskUpdated}
            onTaskDeleted={handleTaskDeleted}
          />
        </div>
      </main>

      <footer className="app-footer">
        <p>Total de tareas: {tasks.length}</p>
        <button onClick={loadTasks} className="btn-refresh">
          🔄 Actualizar
        </button>
      </footer>
    </div>
  );
}

export default App;
import React, { useState } from 'react';

const TaskItem = ({ task, onTaskUpdated, onTaskDeleted }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [editedTitle, setEditedTitle] = useState(task.title);
  const [editedDescription, setEditedDescription] = useState(task.description || '');

  const handleToggleComplete = async () => {
    try {
      await onTaskUpdated(task.id, {
        ...task,
        completed: !task.completed
      });
    } catch (error) {
      console.error('Error updating task:', error);
    }
  };

  const handleSaveEdit = async () => {
    try {
      await onTaskUpdated(task.id, {
        ...task,
        title: editedTitle,
        description: editedDescription
      });
      setIsEditing(false);
    } catch (error) {
      console.error('Error updating task:', error);
    }
  };

  const handleDelete = async () => {
    if (window.confirm('¿Estás seguro de que quieres eliminar esta tarea?')) {
      try {
        await onTaskDeleted(task.id);
      } catch (error) {
        console.error('Error deleting task:', error);
      }
    }
  };

  return (
    <div className={`task-item ${task.completed ? 'completed' : ''}`}>
      {isEditing ? (
        <div className="edit-form">
          <input
            type="text"
            value={editedTitle}
            onChange={(e) => setEditedTitle(e.target.value)}
          />
          <textarea
            value={editedDescription}
            onChange={(e) => setEditedDescription(e.target.value)}
            rows="2"
          />
          <div className="edit-actions">
            <button onClick={handleSaveEdit}>Guardar</button>
            <button onClick={() => setIsEditing(false)}>Cancelar</button>
          </div>
        </div>
      ) : (
        <>
          <div className="task-content">
            <h4>{task.title}</h4>
            {task.description && <p>{task.description}</p>}
            <div className="task-meta">
              <span>Estado: {task.completed ? 'Completada' : 'Pendiente'}</span>
            </div>
          </div>
          
          <div className="task-actions">
            <button 
              onClick={handleToggleComplete}
              className={task.completed ? 'btn-complete' : 'btn-incomplete'}
            >
              {task.completed ? 'Marcar Pendiente' : 'Marcar Completada'}
            </button>
            
            <button 
              onClick={() => setIsEditing(true)}
              className="btn-edit"
            >
              Editar
            </button>
            
            <button 
              onClick={handleDelete}
              className="btn-delete"
            >
              Eliminar
            </button>
          </div>
        </>
      )}
    </div>
  );
};

export default TaskItem;
import React from 'react';
import TaskItem from './TaskItem';

const TaskList = ({ tasks, onTaskUpdated, onTaskDeleted }) => {
  if (tasks.length === 0) {
    return (
      <div className="task-list">
        <h3>Lista de Tareas</h3>
        <p>No hay tareas pendientes</p>
      </div>
    );
  }

  return (
    <div className="task-list">
      <h3>Lista de Tareas ({tasks.length})</h3>
      
      {tasks.map(task => (
        <TaskItem
          key={task.id}
          task={task}
          onTaskUpdated={onTaskUpdated}
          onTaskDeleted={onTaskDeleted}
        />
      ))}
    </div>
  );
};

export default TaskList;
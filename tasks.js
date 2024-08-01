const axios = require('axios');

const fetchTasks = async () => {
  try {
    const response = await axios.get('http://localhost:3000/api/tasks/');
    if (response.status !== 200) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    console.log('Tasks:', response.data);
  } catch (error) {
    console.error('Error fetching tasks:', error.message);
  }
};

const addTask = async (title, description) => {
  const newTask = {
    title,
    description,
  };

  try {
    const response = await axios.post('http://localhost:3000/api/tasks/', newTask, {
      headers: {
        'Content-Type': 'application/json',
      },
    });
    if (response.status !== 201) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    console.log('Task added:', response.data);
  } catch (error) {
    console.error('Error adding task:', error.message);
  }
};

// Example usage
fetchTasks();

addTask('New Task', 'This is a new task description.');

<template>
    <div>
      <h1>Tasks</h1>
      <form @submit.prevent="addTask">
        <input v-model="newTask.title" placeholder="Title" />
        <input v-model="newTask.description" placeholder="Description" />
        <button type="submit">Add Task</button>
      </form>
      <ul>
        <li v-for="task in tasks" :key="task.id">
          <h2>{{ task.title }}</h2>
          <p>{{ task.description }}</p>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'TaskList',
    data() {
      return {
        tasks: [],
        newTask: {
          title: "",
          description: ""
        },
        error: null
      };
    },
    methods: {
      async fetchTasks() {
        try {
          const response = await fetch("/api/tasks/");
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          this.tasks = await response.json();
        } catch (error) {
          this.error = error.message;
        }
      },
      async addTask() {
        try {
          const response = await fetch("/api/tasks/", {
            method: "POST",
            headers: {
              "Content-Type": "application/json"
            },
            body: JSON.stringify(this.newTask)
          });
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          const newTask = await response.json();
          this.tasks.push(newTask);
          this.newTask.title = "";
          this.newTask.description = "";
        } catch (error) {
          this.error = error.message;
        }
      }
    },
    mounted() {
      this.fetchTasks();
    }
  };
  </script>
  
  <style>
  /* Add your styles here */
  </style>
  
<script>
    import { onMount } from 'svelte';
    import axios from 'axios';
  
    let items = [];
    let errorMessage = '';
  
    onMount(async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/admin/data');
        items = response.data;
        console.log(items)
      } catch (error) {
        errorMessage = "Error fetching data: " + error.message;
        console.error(error);
      }
    });
  </script>
  
  <h2>Fetched Data from MySQL:</h2>
  {#if errorMessage}
    <p style="color: red;">{errorMessage}</p>
  {/if}
  <table>
    <thead>
      <tr>
        <th>Name</th>
        <th>Course</th>
        <th>Mobile</th>
        <th>Location</th>
      </tr>
    </thead>
    <tbody>
      {#each items as item}
        <tr>
          <td>{item.name}</td>
          <td>{item.course}</td>
          <td>{item.mobile}</td>
          <td>{item.location}</td>
        </tr>
      {/each}
    </tbody>
  </table>
  <style>
    table{
        width:100%;
        text-align: center;
    }
    thead{
        Background-color:green;
        color:white;
        height:2.2rem;
    }
    tbody tr{
        border-bottom:1px solid black;
        height:2.2rem;
        
    }
  </style>
  
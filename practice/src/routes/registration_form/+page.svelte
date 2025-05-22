<script>
  import { onMount } from 'svelte';
    import { logout } from '$lib/api/logout.js';
  import { redirect } from '@sveltejs/kit';
  let successmessage = "";
  let errormessage = "";
  let name = "";
  let course = "";
  let mobile = "";
  let location = "";

  async function enterdata(event) {
    event.preventDefault();

    // Trim inputs to remove unnecessary whitespace
    const trimmedName = name.trim();
    const trimmedCourse = course.trim();
    const trimmedMobile = mobile.trim();
    const trimmedLocation = location.trim();

    // Client-side validation
    if (!trimmedName || !trimmedCourse || !trimmedMobile || !trimmedLocation) {
      errormessage = "All fields are required.";
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:5000/datasubmission", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: trimmedName,
          course: trimmedCourse,
          mobile: trimmedMobile,
          location: trimmedLocation,
        }),
      });

      if (response.ok) {
        successmessage = "Registration Successful!";
        errormessage = "";
        name = "";
        course = "";
        mobile = "";
        location = "";
        setTimeout(() => {
          successmessage = "";
        }, 3000);
      } else {
        const errorData = await response.json();
        errormessage = errorData.message || "Submission failed.";
      }
    } catch (error) {
      console.error("Error:", error);
      errormessage = "An error occurred during submission.";
    }
  }
  async function logout_fun() {
  try {
    await logout();  
    redirect('/login')
  } catch (err) {
    console.error('Logout failed:', err);
  }
}
</script>

<div class="logout">
  <button on:click={logout_fun}>Logout</button>
</div>
<div class="main">
  <div class="box">
    <form on:submit={enterdata}>
      <h2>Registration Form</h2>
      <input type="text" bind:value={name} placeholder="Name" required />
      <input
        type="text"
        bind:value={course}
        placeholder="Course/Program"
        required
      />
      <input type="text" bind:value={mobile} placeholder="Mobile Number" />
      <input type="text" bind:value={location} placeholder="Location" />
      <div class="butt">
        {#if successmessage}
          <div class="successmessage">
            {successmessage}
          </div>{/if}
        {#if errormessage}
          <div class="errormessage">{errormessage}</div>
        {/if}
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</div>

<style>
  .main {
    height: 100vh;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .successmessage {
    color: green;
  }
  .box {
    border: none;
    box-shadow: 5px 5px 20px grey;
    padding: 10px;
    width: auto;
    border-radius: 15px;
  }
  .box form {
    display: flex;
    flex-direction: column;
    text-align: center;
    margin: 30px;
  }
  .box form input {
    padding: 10px;
    font-size: 15px;
    margin: 5px;
    border: 0.5px solid grey;
  }
  .successmessage {
    color: green;
    font-weight: bold;
  }
  .errormessage {
  color: red;
  font-weight: bold;
  margin-top: 10px;
}

  .butt {
    height: 1.5em;
    margin-top: 10px;
    overflow: hidden;
  }
  button {
    background-color: green;
    padding: 8px 20px;
    border-radius: 10px;
    color: white;
    border: none;
    font-size: 20px;
    cursor: pointer;
    margin-top: 15px;
  }
</style>

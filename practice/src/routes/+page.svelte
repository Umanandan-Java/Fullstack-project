<script>
  import "boxicons/css/boxicons.min.css";
</script>

<!-- Link to Google Fonts for Roboto -->
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">

<div class="main">
  <h1>Welcome</h1>
  <div class="section">
    <!-- Staff Section -->
    <div class="staff">
      <h3>If you are a staff member</h3>
      <button class="staff-login" on:click={() => (location.href = "/staff-login")}> Staff - Login </button>
    </div>

    <!-- Student Section -->
    <div class="buttons">
      <h3>If you are a student</h3>
      <button on:click={() => (location.href = "/Student-login")}> Student - Login </button>
      <button on:click={() => (location.href = "/Student-createaccount")}>
        Student - Sign Up <i class="bx bx-chevron-right"></i>
      </button>
    </div>
  </div>
</div>

<style>
  /* Apply Roboto font throughout the site */
  

  .main {
    height: 100vh;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
  }

  .main .section {
    width: 80%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    gap: 20px;
  }

  .buttons, .staff {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  h1 {
    font-size: 36px;
    font-weight: 700;  /* Bold */
    margin-bottom: 20px;
  }

  h3 {
    font-size: 24px;
    font-weight: 500;  /* Medium weight */
    margin-bottom: 10px;
  }

  .buttons button, .staff button {
    font-size: 18px;
    background-color: #4CAF50; /* Green for consistency */
    color: white;
    border: none;
    padding: 12px 18px;
    margin: 10px;
    border-radius: 5px;
    cursor: pointer;
    width: 200px;
    font-family: 'Roboto', sans-serif;  /* Ensures buttons also use Roboto */
  }

  .staff button {
    background-color: #2196F3; /* Blue for Staff */
  }

  .buttons button:hover, .staff button:hover {
    background-color: #45a049; /* Darker shade for hover effect */
  }
</style>

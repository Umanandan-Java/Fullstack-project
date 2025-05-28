<script>
  import { goto } from '$app/navigation';
  let username = '';
  let password = '';
  let reg_no = '';
  let confirmPassword = '';
  let error = '';
    function goToAnotherPage() {
        goto('/Student-login');
      }
  async function handleSubmit(event) {
    event.preventDefault();

    // Check if passwords match
    if (password !== confirmPassword) {
      error = "Passwords don't match!";
      return;
    } else {
      error = '';

      // Send data to Flask backend
      try {
        const response = await fetch('http://localhost:5000/create_account', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            username: username,
            password: password,
            reg_no:reg_no,
          }),
        });

        const data = await response.json();

        if (data.success) {
          goto('/Student-login'); 
        } else {
          error = data.message || "An error occurred!";
        }
      } catch (err) {

        console.error(err);
        error = "Error sending data to server!";
      }
    }
  }
</script>

<div class="main">
  <div class="box">
    <form on:submit|preventDefault={handleSubmit}>
      <h2>Create Account</h2>
      <input
        type="text"
        placeholder="Registration Number"
        bind:value={reg_no}
        required
      />
      <input
        type="text"
        placeholder="Username"
        bind:value={username}
        required
      />
      <input
        type="password"
        placeholder="Password"
        minlength="6"
        bind:value={password}
        required
      />
      <input
        type="password"
        placeholder="Confirm Password"
        minlength="6"
        bind:value={confirmPassword}
        required
      />

      {#if error}
        <p class=error >{error}</p>
      {/if}
        <div class="but">
      <button type="button" class="login" on:click={goToAnotherPage}>Login</button>
      <button type="submit">Create account</button>
      </div>
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
  .but{
    display: flex;
    justify-content: space-around;
    gap:50px;
  }
  .but .login, .but button{
    padding:10px 30px;
    cursor: pointer;
  }
  .box form {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .error {
    color: green;
    min-height: 20px; 
    margin-top: 10px;
}

  .box {
    padding: 20px 40px;
    box-shadow: 10px 10px 20px rgb(220, 220, 220);
    width: 320px;
    border-radius: 35px;
  }

  form h2 {
    color: green;
  }

  form input {
    font-size: 15px;
    margin: 5px 10px;
    padding: 10px;
    width: 100%;
  }

  form button {
    background-color: green;
    color: white;
    padding: 15px;
    border: none;
    border-radius: 10px;
    margin-top: 20px;
  }
</style>

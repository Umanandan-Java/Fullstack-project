<script>
    import { goto } from '$app/navigation';
    import { isAuthenicated, role_name } from '../../store/auth';
    
    let username = '';  // This is actually the role (Admin or Registrer)
    let password = '';
    let registration_no='';

    // Handle form submission
    async function handleSubmit(event) {
        event.preventDefault();
        console.log("triggered")
        try {
            const response = await fetch('http://localhost:5000/api/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password,registration_no }),
                // credentials: 'include'  // Send role as username
            });
                
         if (!response.ok) {
        throw new Error('Login failed');
    }

        const result = await response.json();  // <-- assign result here

        if (result.success) {
        goto(result.redirect);  // <-- now result is defined
    } 
            else {
                const errorData = await response.json()
                console.error("Login failed:", errorData.message);
                alert("Login failed: " + errorData.message);
            }
        } catch (error) {
            console.error("Error during login:", error);
            alert("Error during login. Please try again.");
        }
    }
    function gotoanotherpage(){
        goto('/Student-createaccount')
    }
</script>

<div class="main">
    <div class="box">
        <form on:submit={handleSubmit}>
            <h2>Login</h2>

            <!-- Role selection -->
            <!-- <select name="role" id="roleselect" bind:value={username} required>
                <option value="">Select Role</option>
                <option value="Admin">Admin</option>
                <option value="Registrer">Registrer</option>
            </select> -->
            <input type="text" placeholder="registration_no" bind:value={registration_no}>
            <input type="text" placeholder="username" bind:value={username}>
            <!-- Password input -->
            <input type="password" placeholder="Password" bind:value={password} required>

            <!-- Submit button -->
            <div class="butt">
                <button class="signup" style="background-color:blue;color:white;" type="button" on:click={gotoanotherpage}>Signup</button>
                <button type="submit" class="login" disabled={!username || !password}>Login</button>
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

    .box {
        border: none;
        box-shadow: 5px 5px 20px grey;
        padding: 20px;
        width: 300px;
        border-radius: 15px;
        background-color:white;
    }

    .box form {
        display: flex;
        flex-direction: column;
        text-align: center;
    }
    .box form h2{
        color:green;
    }
    
    .box form select,
    .box form input {
        padding: 10px;
        font-size: 15px;
        margin: 5px 0;
        border: 1px solid grey;
        border-radius: 5px;
    }

    .butt {
        margin-top: 15px;
        display: flex;
        justify-content: center;
        gap:50px;
    }
    .signup{
        background-color: blue;
        font-size: 15px;
        padding:10px 20px;
        color:white;
        border-radius: 10px;
        border:none; 
        cursor: pointer; 
    }

    .butt .login {
        background-color: green;
        color: white;
        padding: 8px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
    }

    .butt button:disabled {
        background-color: grey;
        cursor: not-allowed;
    }
</style>

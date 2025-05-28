<div class="main">
        <button on:click={() => (location.href = "/registration_form")}> Register a Student</button>
        <button on:click={() => (location.href = "/staff-get-details")}>Get Details</button>
</div>
<style>
    .main{
        height: 100vh;
        width:100%;
        display: flex;
        justify-content: center;
        align-items: center;
        gap:20px;
    }
    button{
        background-color: green;
        color:white;
        font-size:20px;
        padding:10px 20px;
        border:none;
        border-radius: 5px;
        cursor: pointer;
    }
    
</style>
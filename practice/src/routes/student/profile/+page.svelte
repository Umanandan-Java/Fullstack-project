<script>
  import { page } from '$app/stores';
  import { onMount } from 'svelte';

  let registration_no;
  let userData = null;

  $: registration_no = $page.url.searchParams.get("Registration_no");

  onMount(async () => {
    if (registration_no) {
      try {
        const res = await fetch(`http://localhost:5000/user-details?registration_number=${registration_no}`);
        if (res.ok) {
          userData = await res.json();
        } else {
          console.error("Failed to fetch user data");
        }
      } catch (error) {
        console.error("Error fetching user data:", error);
      }
    }
  });
</script>

<div class="main">
  <div class="dashboard">
    <div class="box">
      {#if userData}
        <img src={userData.image_url} alt="Profile Photo" class="profile" />
      {/if}
    </div>

    {#if userData}
      <div class="details">
        <h2>Student Information</h2>
        <div class="info-grid">
          <p><strong>Name:</strong> {userData.firstname} {userData.middlename} {userData.lastname}</p>
          <p><strong>Father's Name:</strong> {userData.fathername}</p>
          <p><strong>Qualification:</strong> {userData.qualification}</p>
          <p><strong>Passed Out Year:</strong> {userData.year}</p>
          <p><strong>Application Status</strong> {userData.application_status}</p>
        </div>
      </div>
    {/if}
  </div>
</div>

<style>
  :root {
    --primary-color:#0063ff ;
    --text-color: #333;
    --bg-color: #f9f9f9;
    --card-bg: #ffffff;
    --border-radius: 12px;
  }

  .main {
    display: flex;
    justify-content: center;
    padding: 2rem;
    background-color: var(--bg-color);
    min-height: 100vh;
    /* width:100%; */
  }

  .dashboard {
    background-color: var(--card-bg);
    border-radius: var(--border-radius);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    padding: 2rem;
    display: flex;
    gap: 2rem;
    align-items: flex-start;
    flex-wrap: wrap;
    /* max-width: 800px; */
    width: 100%;
    padding:20px;

  }
  p strong{
    color: #7b7485;
  }
  P{
    color:#352b48;
  }
  .box {
    width: 180px;
    height: 180px;
    border-radius: 50%;
    overflow: hidden;
    /* border: 4px solid var(--primary-color); */
    /* box-shadow: 0 0 10px rgba(79, 70, 229, 0.3); */
    flex-shrink: 0;
    margin:26px;
    position:relative;
  }

  .profile {
    width: 100%;
    height: 100%;
    position:absolute;
    object-fit: cover;
    top:0px;
    
  }

  .details {
    flex: 1;
    color: var(--text-color);
  }

  .details h2 {
    margin-bottom: 1rem;
    color: var(--primary-color);
    font-size: 1.5rem;
  }

  .info-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
  }

  .info-grid p {
    background-color: #f0f0f0;
    padding: 0.75rem 1rem;
    border-radius: 8px;
    font-size: 1rem;
  }

  @media (max-width: 600px) {
    .dashboard {
      flex-direction: column;
      align-items: center;
    }

    .info-grid {
      grid-template-columns: 1fr;
    }

    .box {
      width: 150px;
      height: 150px;
    }
  }
</style>

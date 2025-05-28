<header>
  <div class="logo">
    <img src="/logo-anu.png" alt="" />
  </div>
  <div class="main-heading">
    <h3>Centre For Distance Education</h3>
    <h3>Acharya Nagarjuna University</h3>
    <p>(Recognised by Distance Education Bureau, New Delhi)</p>
  </div>
  <div class="logo2">
    <img src="/download.jpg" alt="" />
  </div>
</header>

<main class="page-content">
  <slot />
</main>

<style>
  header {
    position:relative;
    top: 0;
    left: 0;
    right: 0;
    height: 100px; /* fixed height */
    background-color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    padding: 0 20px;
    z-index: 1000;
  }

  .logo,
  .logo2,
  .main-heading {
    padding: 0;
  }

  header .logo img {
    max-width: 70px;
    margin: 0;
  }

  header .logo2 img {
    max-width: 50px;
    margin: 0;
  }

  header .main-heading {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 0;
    margin: 0;
  }

  header .main-heading h3,
  header .main-heading p {
    margin: 0;
  }

  .page-content {
    /* padding-top: 100px; exactly same as header height */
    max-width: 80%;
    margin: 0 auto;
  }
</style>

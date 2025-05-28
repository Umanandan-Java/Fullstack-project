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
  <slot />
  <style>
  header {
    width: 100%;
    height: 25%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
  }
  .logo,
  .logo2,
  .main-heading {
    padding: 0px;
  }
  header .logo img {
    max-width: 70px;
    margin: 0px;
  }
  header .logo2 img {
    max-width: 50px;
    margin: 0px;
  }
  header .main-heading {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    padding: 0px;
  }
  header .main-heading h3,
  header .main-heading p {
    margin: 0px;
  }
  </style>
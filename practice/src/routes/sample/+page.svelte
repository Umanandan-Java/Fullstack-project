<section class="hero">
  <div class="overlay">
    <div class="content">
      <h1>When life keeps you busy,<br />we keep your dreams alive.</h1>
      <p>Acharya Nagarjuna University – Centre for Distance Education</p>
      <div class="button">
        <button>Scroll Down <img src="/arrow-down-stroke-circle.png" alt=""></button>
      </div>
    </div>
  </div>
</section>

<style>
  .hero {
    position: relative;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    color: white;
  }

  .hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: url('/finalaerialview.png');
    background-size: cover;
    background-position: center;
    filter: blur(2px);
    z-index: 0;
    transform: scale(1); /* prevent edges from showing when blurred */
  }

  .overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(to bottom, rgba(0,0,0,0.6), rgba(0,0,0,0.8));
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem;
    text-align: center;
    z-index: 1;
  }

  .content {
    background: rgba(255, 255, 255, 0.2);
    padding: 2rem 3rem;
    border-radius: 16px;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.2);
    display: inline-block;
    max-width: 90vw;
    z-index: 2;
    backdrop-filter: blur(4px);
  }

  .content h1 {
    font-size: 2.5rem;
    font-weight: 700;
    margin: 0 0 1rem 0;
    line-height: 1.2;
  }

  .content p {
    font-size: 1.2rem;
    font-weight: 400;
    color: #ccc;
    margin: 0;
  }

  .button {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 30px;
    justify-content: space-evenly;
  }

  .button button {
    background-color: rgba(0, 0, 0, 0.2);
    width: 200px;
    color: white;
    padding: 10px 25px;
    font-weight: bold;
    border-radius: 50px;
    border: 1px solid white;
    font-size: 17px;
    display: flex;
    justify-content: space-evenly;
    align-items: center;
  }

  .button button img {
    width: 25px;
    height: 25px;
    filter: invert(1);
  }

  .button button:hover {
    background-color: white;
    color: black;
  }

  .button button:hover img {
    filter: invert(0);
  }

  @media (max-width: 768px) {
    .hero {
      height: 70vh;
    }

    .content {
      padding: 1rem 1.2rem;
      border-radius: 8px;
    }

    .content h1 {
      font-size: 1.8rem;
    }

    .content p {
      font-size: 1rem;
    }
  }
</style>

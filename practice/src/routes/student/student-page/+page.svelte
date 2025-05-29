<script>
  import { goto } from "$app/navigation";

  // Personal details
  let student_name = "";
  let father_name = "";
  let mother_name = "";
  let gender = "";
  let marital_status = "";
  let dob = "";
  let religion = "";
  let caste = "";
  let nationality = "";
  let aadhar_number = "";
  let mobile_number = "";
  let physically_challenged = "";
  let locality = "";

  // Course
  let course_category = "";
  let course_of_application = "";

  // Degree
  let degree_group = "";
  let degree_college_name = "";
  let degree_year_of_passing = "";
  let degree_reg_number = "";
  let degree_aggregate_percentage = "";

  // Inter
  let inter_group = "";
  let inter_college_name = "";
  let inter_year_of_passing = "";
  let inter_reg_number = "";
  let inter_aggregate_percentage = "";

  // Tenth
  let tenth_school_name = "";
  let tenth_year_of_passing = "";
  let tenth_reg_number = "";
  let tenth_aggregate_percentage = "";

  // Upload refs
  let pms, tms, ims, dms, dts;

  let courseDetailsRef;
  let academicDetailsRef;

  const courseCategories = [
    { value: "UG", label: "Undergraduate (UG)" },
    { value: "PG", label: "Postgraduate (PG)" },
  ];

  const subCourses = {
    UG: [
      { value: "ba", label: "BA (English, Hindi, History, etc.)" },
      { value: "bcom", label: "BCom (General, Computer Applications, Accounts)" },
      { value: "bba", label: "BBA" },
      { value: "bca", label: "BCA" },
      { value: "blis", label: "BLIS (Library & Information Sciences)" },
      { value: "bsc", label: "BSc (Computer Science, Maths, IT, etc.)" },
    ],
    PG: [
      { value: "ma", label: "MA (English, History, Sociology, etc.)" },
      { value: "mcom", label: "MCom (General, Financial Management)" },
      { value: "mba", label: "MBA (General, Finance, HR, Marketing, etc.)" },
      { value: "mca", label: "MCA" },
      { value: "mlis", label: "MLIS (Library & Information Sciences)" },
      { value: "msc", label: "MSc (Maths, Computer Science, Chemistry, etc.)" },
    ],
  };

  const max_image_size = 500; // in KB

  function isUnderKB(file) {
    if (!file) return false;
    return file.size / 1024 <= max_image_size;
  }

  async function handledetails() {
    const formData = new FormData();

    formData.append("student_name", student_name);
    formData.append("father_name", father_name);
    formData.append("mother_name", mother_name);
    formData.append("gender", gender);
    formData.append("marital_status", marital_status);
    formData.append("dob", dob);
    formData.append("religion", religion);
    formData.append("caste", caste);
    formData.append("nationality", nationality);
    formData.append("aadhar_number", aadhar_number);
    formData.append("mobile_number", mobile_number);
    formData.append("physically_challenged", physically_challenged);
    formData.append("locality", locality);
    formData.append("course_category", course_category);
    formData.append("course_of_application", course_of_application);
    formData.append("degree_group", degree_group);
    formData.append("degree_college_name", degree_college_name);
    formData.append("degree_year_of_passing", degree_year_of_passing);
    formData.append("degree_reg_number", degree_reg_number);
    formData.append("degree_aggregate_percentage", degree_aggregate_percentage);
    formData.append("inter_group", inter_group);
    formData.append("inter_college_name", inter_college_name);
    formData.append("inter_year_of_passing", inter_year_of_passing);
    formData.append("inter_reg_number", inter_reg_number);
    formData.append("inter_aggregate_percentage", inter_aggregate_percentage);
    formData.append("tenth_school_name", tenth_school_name);
    formData.append("tenth_year_of_passing", tenth_year_of_passing);
    formData.append("tenth_reg_number", tenth_reg_number);
    formData.append("tenth_aggregate_percentage", tenth_aggregate_percentage);

    try {
      if (tms?.files[0] && isUnderKB(tms.files[0])) formData.append("tenth_memo", tms.files[0]);
      if (pms?.files[0] && isUnderKB(pms.files[0])) formData.append("passport_size_photo", pms.files[0]);
      if (ims?.files[0] && isUnderKB(ims.files[0])) formData.append("inter_marksheet", ims.files[0]);
      if (dms?.files[0] && isUnderKB(dms.files[0])) formData.append("degree_marksheet", dms.files[0]);
      if (dts?.files[0] && isUnderKB(dts.files[0])) formData.append("degree_tc", dts.files[0]);
    } catch (err) {
      console.error("Image upload error", err);
    }

    const response = await fetch("http://localhost:5000/student-registration", {
      method: "POST",
      body: formData,
    });

    if (response.ok) {
      goto("/staff-page");
    } else {
      const error = await response.json();
      console.error(error.message);
    }
  }

  // Scroll helper for Next buttons
  function scrollToSection(sectionRef) {
    sectionRef.scrollIntoView({ behavior: "smooth" });
  }
</script>

<div class="main">
  <form on:submit|preventDefault={handledetails}>

    <!-- Personal Details -->
    <section class="section">
      <h2>Personal Details</h2>
      <div class="grid">
        <div class="form-group">
          <label for="student_name">Name of the Candidate</label>
          <input id="student_name" type="text" bind:value={student_name} required />
        </div>

        <div class="form-group">
          <label for="father_name">Father's Name</label>
          <input id="father_name" type="text" bind:value={father_name} required />
        </div>

        <div class="form-group">
          <label for="mother_name">Mother's Name</label>
          <input id="mother_name" type="text" bind:value={mother_name} required />
        </div>

        <div class="form-group full-width">
          <label>Gender</label>
          <div class="radio-group">
            <label><input type="radio" name="gender" value="male" bind:group={gender} required /> Male</label>
            <label><input type="radio" name="gender" value="female" bind:group={gender} /> Female</label>
          </div>
        </div>

        <div class="form-group">
          <label for="marital_status">Marital Status</label>
          <input id="marital_status" type="text" bind:value={marital_status} />
        </div>

        <div class="form-group">
          <label for="dob">Date of Birth</label>
          <input id="dob" type="date" bind:value={dob} required />
        </div>

        <div class="form-group">
          <label for="religion">Religion</label>
          <input id="religion" type="text" bind:value={religion} />
        </div>

        <div class="form-group">
          <label for="caste">Caste</label>
          <input id="caste" type="text" bind:value={caste} />
        </div>

        <div class="form-group">
          <label for="nationality">Nationality</label>
          <input id="nationality" type="text" bind:value={nationality} required />
        </div>

        <div class="form-group">
          <label for="aadhar_number">Aadhar Number</label>
          <input id="aadhar_number" type="text" bind:value={aadhar_number} />
        </div>

        <div class="form-group">
          <label for="mobile_number">Mobile Number</label>
          <input id="mobile_number" type="tel" bind:value={mobile_number} required />
        </div>

        <div class="form-group full-width">
          <label>Physically Challenged</label>
          <div class="radio-group">
            <label><input type="radio" name="physically_challenged" value="yes" bind:group={physically_challenged} required /> Yes</label>
            <label><input type="radio" name="physically_challenged" value="no" bind:group={physically_challenged} /> No</label>
          </div>
        </div>

        <div class="form-group full-width">
          <label for="locality">Locality</label>
          <textarea id="locality" rows="2" bind:value={locality}></textarea>
        </div>
      </div>

      <button type="button" class="btn-next" on:click={() => scrollToSection(courseDetailsRef)}>Next</button>
    </section>

    <!-- Course Details -->
    <section bind:this={courseDetailsRef} class="section">
      <h2>Course Details</h2>
      <div class="grid">
        <div class="form-group">
          <label for="course_category">Course Category</label>
          <select id="course_category" bind:value={course_category} required>
            <option value="" disabled selected>Select Course Category</option>
            {#each courseCategories as cat}
              <option value={cat.value}>{cat.label}</option>
            {/each}
          </select>
        </div>

        <div class="form-group">
          <label for="course_of_application">Course of Application</label>
          <select
            id="course_of_application"
            bind:value={course_of_application}
            required
            disabled={!course_category}
          >
            <option value="" disabled selected>Select Course</option>
            {#if course_category}
              {#each subCourses[course_category] as sub}
                <option value={sub.value}>{sub.label}</option>
              {/each}
            {/if}
          </select>
        </div>
      </div>

      <button type="button" class="btn-next" on:click={() => scrollToSection(academicDetailsRef)}>Next</button>
    </section>

    <!-- Academic Details -->
    <section bind:this={academicDetailsRef} class="section">
      <h2>Academic Details</h2>
        {#if course_category==="PG"}
      <fieldset>
        <legend>Degree Details</legend>
        <div class="grid">
          <div class="form-group">
            <label for="degree_group">Degree Group</label>
            <input id="degree_group" type="text" bind:value={degree_group} required />
          </div>

          <div class="form-group">
            <label for="degree_college_name">College Name</label>
            <input id="degree_college_name" type="text" bind:value={degree_college_name} required />
          </div>

          <div class="form-group">
            <label for="degree_year_of_passing">Year of Passing</label>
            <input id="degree_year_of_passing" type="number" min="1900" max="2100" bind:value={degree_year_of_passing} required />
          </div>

          <div class="form-group">
            <label for="degree_reg_number">Register Number</label>
            <input id="degree_reg_number" type="text" bind:value={degree_reg_number} required />
          </div>

          <div class="form-group">
            <label for="degree_aggregate_percentage">Aggregate %</label>
            <input id="degree_aggregate_percentage" type="number" step="0.01" min="0" max="100" bind:value={degree_aggregate_percentage} required />
          </div>

          <div class="form-group">
            <label for="dms">Degree Marksheet (max 500KB)</label>
            <input id="dms" type="file" bind:this={dms} accept=".jpg,.jpeg,.png,.pdf" />
          </div>

          <div class="form-group">
            <label for="dts">Degree Transfer Certificate (max 500KB)</label>
            <input id="dts" type="file" bind:this={dts} accept=".jpg,.jpeg,.png,.pdf" />
          </div>
        </div>
      </fieldset>
      {/if}

      <fieldset>
        <legend>Intermediate (12th) Details</legend>
        <div class="grid">
          <div class="form-group">
            <label for="inter_group">Group</label>
            <input id="inter_group" type="text" bind:value={inter_group} required />
          </div>

          <div class="form-group">
            <label for="inter_college_name">College Name</label>
            <input id="inter_college_name" type="text" bind:value={inter_college_name} required />
          </div>

          <div class="form-group">
            <label for="inter_year_of_passing">Year of Passing</label>
            <input id="inter_year_of_passing" type="number" min="1900" max="2100" bind:value={inter_year_of_passing} required />
          </div>

          <div class="form-group">
            <label for="inter_reg_number">Register Number</label>
            <input id="inter_reg_number" type="text" bind:value={inter_reg_number} required />
          </div>

          <div class="form-group">
            <label for="inter_aggregate_percentage">Aggregate %</label>
            <input id="inter_aggregate_percentage" type="number" step="0.01" min="0" max="100" bind:value={inter_aggregate_percentage} required />
          </div>

          <div class="form-group">
            <label for="ims">Intermediate Marksheet (max 500KB)</label>
            <input id="ims" type="file" bind:this={ims} accept=".jpg,.jpeg,.png,.pdf" />
          </div>
        </div>
      </fieldset>

      <fieldset>
        <legend>Tenth Details</legend>
        <div class="grid">
          <div class="form-group">
            <label for="tenth_school_name">School Name</label>
            <input id="tenth_school_name" type="text" bind:value={tenth_school_name} required />
          </div>

          <div class="form-group">
            <label for="tenth_year_of_passing">Year of Passing</label>
            <input id="tenth_year_of_passing" type="number" min="1900" max="2100" bind:value={tenth_year_of_passing} required />
          </div>

          <div class="form-group">
            <label for="tenth_reg_number">Register Number</label>
            <input id="tenth_reg_number" type="text" bind:value={tenth_reg_number} required />
          </div>

          <div class="form-group">
            <label for="tenth_aggregate_percentage">Aggregate %</label>
            <input id="tenth_aggregate_percentage" type="number" step="0.01" min="0" max="100" bind:value={tenth_aggregate_percentage} required />
          </div>

          <div class="form-group">
            <label for="tms">Tenth Marksheet (max 500KB)</label>
            <input id="tms" type="file" bind:this={tms} accept=".jpg,.jpeg,.png,.pdf" />
          </div>

          <div class="form-group">
            <label for="pms">Passport Size Photo (max 500KB)</label>
            <input id="pms" type="file" bind:this={pms} accept=".jpg,.jpeg,.png" />
          </div>
        </div>
      </fieldset>

      <div class="buttons">
        <button type="submit" class="btn-submit">Submit</button>
      </div>
    </section>
  </form>
</div>

<style>
  .main {
    width: 100%;
    /* margin: 2rem auto; */
    padding: 2rem;
    background: white;
    border-radius: 8px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }

  h2 {
    font-size: 1.8rem;
    color: #333;
    margin-bottom: 1rem;
    border-bottom: 2px solid #f0f0f0;
    padding-bottom: 0.5rem;
  }

  .section {
    margin-bottom: 3rem;
  }

  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1rem 2rem;
    margin-bottom: 1.5rem;
  }

  .form-group {
    display: flex;
    flex-direction: column;
  }

  .form-group.full-width {
    grid-column: 1 / -1;
  }

  label {
    font-weight: 600;
    margin-bottom: 0.4rem;
    color: #555;
  }

  input[type="text"],
  input[type="number"],
  input[type="tel"],
  input[type="date"],
  select,
  textarea {
    padding: 0.5rem 0.75rem;
    font-size: 1rem;
    border: 1.8px solid #ccc;
    border-radius: 6px;
    transition: border-color 0.3s ease;
    font-family: inherit;
  }

  input[type="text"]:focus,
  input[type="number"]:focus,
  input[type="tel"]:focus,
  input[type="date"]:focus,
  select:focus,
  textarea:focus {
    outline: none;
    border-color: #2b6cb0;
    box-shadow: 0 0 5px rgba(43, 108, 176, 0.4);
  }

  textarea {
    resize: vertical;
  }

  .radio-group {
    display: flex;
    gap: 1.5rem;
  }

  .radio-group label {
    font-weight: normal;
  }

  input[type="file"] {
    padding: 0.3rem;
  }

  fieldset {
    border: 1px solid #ddd;
    padding: 1rem 1.5rem 1.5rem;
    margin-bottom: 2rem;
    border-radius: 6px;
  }

  legend {
    font-weight: 700;
    padding: 0 10px;
    color: #444;
  }

  .buttons {
    display: flex;
    justify-content: space-between;
    margin-top: 1rem;
  }

  button {
    padding: 0.65rem 1.6rem;
    font-size: 1.1rem;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-weight: 600;
    transition: background-color 0.3s ease;
    font-family: inherit;
  }

  .btn-next {
    background-color: #3182ce;
    color: white;
  }
  .btn-next:hover {
    background-color: #2c5282;
  }

  .btn-prev {
    background-color: #a0aec0;
    color: white;
  }
  .buttons {
    display: flex;
    justify-content: center;
    align-items: center;
       
  }
  .buttons .btn-submit{
    background-color: #38a169;
    color: white;
  }
  .btn-submit:hover {
    background-color: #276749;
  }

  @media (max-width: 600px) {
    .buttons {
      flex-direction: column;
      gap: 0.75rem;
    }
  }
</style>

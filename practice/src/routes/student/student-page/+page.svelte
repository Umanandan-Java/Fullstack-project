<script>
	import { goto } from "$app/navigation";

	// Personal
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

	// Uploads
	let pms, tms, ims, dms, dts;

	const max_image_size = 500;
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

		// File uploads
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
			body: formData
		});

		if (response.ok) {
			goto("/staff-page");
		} else {
			const error = await response.json();
			console.error(error.message);
		}
	}
</script>

<div class="main">
    
    <div class="form">
        <form on:submit|preventDefault={handledetails}>
            
            <h2>Application Form</h2>
            <!-- <input type="text" bind:value={Application_no} placeholder="Application Number">
            <input type="text" bind:value={Registration_no} placeholder="Registration Number"> -->
            <section class ="personal_details parent">
                <div class="grid">
            <input type="text" bind:value={student_name} placeholder="Name of the Candidate">
            <input type="text" bind:value={father_name} placeholder="Father Name">
            <input type="text" bind:value={mother_name} placeholder="Mother's Name">
            <input type="text" bind:value={gender} placeholder="Gender">
            <input type="text" bind:value={marital_status} placeholder="Marital Status">
            <input type="text" bind:value={dob} placeholder="Date of Birth">
            <input type="text" bind:value={religion} placeholder="Religion">
            <input type="text" bind:value={caste} placeholder="Caste">
            <input type="text" bind:value={nationality} placeholder="Nationality">
            <input type="text" bind:value={aadhar_number} placeholder="Aadhar Number">
            <input type="text" bind:value={mobile_number} placeholder="Mobile Number">
            <input type="text" bind:value={physically_challenged} placeholder="Physically Challenged">
            <input type="text" bind:value={locality} placeholder="Locality">
            </div>
            </section>

            <!-- section 2 -->
            <section class="course_details">
            <input type="text" bind:value={course_category} placeholder="Course Category">
            <input type="text" bind:value={course_of_application} placeholder="Course Category">
            </section>

            <section class="academic_details">
            <div class="details_of_qualifying_passed">
                <div class="degree">
                    <div class="degree_info">
                                    <input type="text" bind:value={degree_group} placeholder="Group">
                                    <input type="text" bind:value={degree_college_name} placeholder="Name of the College/University">
                                    <input type="text" bind:value={degree_year_of_passing} placeholder="Year of Passing">
                                    <input type="text" bind:value={degree_reg_number} placeholder="Regd. No of Degree">          
                                    <input type="text" bind:value={degree_aggregate_percentage} placeholder="Aggregate Percentage">          
                    </div>
                    <div class="intermediate_info">
                                    <input type="text" bind:value={inter_group} placeholder="Group">
                                    <input type="text" bind:value={inter_college_name} placeholder="Name of the College/University">
                                    <input type="text" bind:value={inter_year_of_passing} placeholder="Year of Passing">
                                    <input type="text" bind:value={inter_reg_number} placeholder="Hall ticket No of Degree">          
                                    <input type="text" bind:value={inter_aggregate_percentage} placeholder="Aggregate Percentage">          
                    </div>
                    <div class="tenth_info">
                                    <input type="text" bind:value={tenth_school_name} placeholder="Name of the School">
                                    <input type="text" bind:value={tenth_year_of_passing} placeholder="Year of Passing">
                                    <input type="text" bind:value={tenth_reg_number} placeholder="Hall ticket No of 10th class">          
                                    <input type="text" bind:value={tenth_aggregate_percentage} placeholder="Aggregate Percentage">          
                    </div>
                </div>
                
            </div>
            </section>
            <div class="marksheets">
            <div class="passportsizephoto">
            <label for="pms">Passport Size Photo</label>
            <input type="file"  accept="image/*" bind:this={pms} id="pms">
            </div>
            <div class="tenthmarksheet">
            <label for="tms">10th Memo</label>
            <input type="file"  accept="image/*" bind:this={tms} id="tms">
            </div>
            <div class="intermarksheet">
            <label for="ims">Inter Marksheet</label>
            <input type="file"  accept="image/*" bind:this={ims} id="ims">
            </div>
            <div class="degreemarksheet">
            <label for="dms">Degree Marksheet</label>
            <input type="file" accept="image/*" bind:this={dms}  id="dms">
            </div>
            <div class="degreetc">
            <label for="dts">Degree TC</label>
            <input type="file"  accept="image/*" bind:this={dts} id="dts">
            </div>
            </div>
            <div class="submit_button">
            <button type="submit">Enter</button>
            </div>
        </form>
    </div>
</div>

<style>
.main {
	height: 100vh;
	overflow-y: scroll;
	scroll-snap-type: y mandatory;
}

form {
	width: 100%;
	height: 100%;
	display: flex;
	flex-direction: column;
	scroll-snap-type: y mandatory;
}

section {
	scroll-snap-align: start;
	height: 100vh;
	padding: 20px;
}
.parent{
display: grid;
grid-template-columns: repeat(6, 1fr);
grid-template-rows: repeat(6, 1fr);
grid-column-gap: 50px;
grid-row-gap: 25px;
display: flex;
flex:1;
justify-content: center;

}
section .grid{
    grid-area: 1 / 1 / 6 / 3; 
}
/* section input{
    max-width: 70px;
    display: flex;
    justify-content: space-evenly;
    flex-direction: row;
} */

.personal_details {
	background-color: skyblue;
}

.course_details {
	background-color: lightgreen;
}

.academic_details {
	background-color: lightcoral;
}

.marksheets {
	background-color: lightyellow;
	display: flex;
	flex-wrap: wrap;
	gap: 20px;
	padding: 20px;
}

.marksheets > div {
	flex: 1 1 45%;
	min-width: 200px;
	display: flex;
	flex-direction: column;
}

input, select, textarea {
	padding: 10px;
	margin-bottom: 10px;
	font-size: 16px;
	border: 1px solid #ccc;
	border-radius: 5px;
}

.submit_button {
	text-align: center;
	margin: 20px 0;
}

button {
	padding: 10px 20px;
	border: none;
	border-radius: 5px;
	background: green;
	color: white;
	cursor: pointer;
}

button:hover {
	background: darkgreen;
}
</style>

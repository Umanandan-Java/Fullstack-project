<script>
	import { json } from "@sveltejs/kit";
    import { onMount } from "svelte";
	let students = [];
    let filters = {
        Application_no:'',
        Registration_no:''
	};
    onMount(()=>{
        const res = fetch('http://localhost:5000/alldata')
        if (res.ok) {
			students = res.json();
		} else {
			console.error("Error fetching filtered data");
		}
    })
    // onMount(() => {
	// 	loadData();
	// });
    async function loadData() {
        const table = document.getElementById('table');
		const res = await fetch('http://localhost:5000/id_search', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify(filters)
		});

		if (res.ok) {
			students = await res.json();
		} else {
			console.error("Error fetching filtered data");
		}
	}
    function clear(){
        filters = {
        Application_no:'',
        Registration_no:'',
	};
    loadData();
    }
    
</script>

<div class="main">
    <div class="search">
        <form on:submit|preventDefault={loadData} style="margin-bottom: 20px;">
    <input placeholder="Application Number" bind:value={filters.Application_no} />
	<input placeholder="Registration Number" bind:value={filters.Registration_no} />
    <div class="buttons">
	<button type="SHOW">Search</button>
    <button type="button" on:click={clear}>CLEAR</button>
    </div>
</form>
    </div>
    
    <div class="table-container">
        <table id="table">
            <thead>
                <tr>
                    <th>Application Number</th>
                    <th>Registration Number</th>
                    <th>Firstname</th>
                    <th>Middlename</th>
                    <th>Lastname</th>
                    <th>Father's Name</th>
                    <th>Qualification</th>
                    <th>Year</th>
                    <th>Application Status</th>
                </tr>
            </thead>
            <tbody>
                {#each students as student}
                <tr>
                    <td>{student.Application_no}</td>
                    <td>{student.Registration_no}</td>
                    <td>{student.firstname}</td>
                    <td>{student.middlename}</td>
                    <td>{student.lastname}</td>
                    <td>{student.fathername}</td>
                    <td>{student.qualification}</td>
                    <td>{student.year}</td>
                    <td>{student.application_status}</td>
                </tr>
                {/each}
            </tbody>
        </table>
    </div>
</div>

<style>
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    .main {
        min-height: 100vh;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        background-color: white;
        padding: 20px;
        font-family: Arial, sans-serif;
    }

    .search {
        margin-bottom: 20px;
    }

    .search form {
        display: flex;
        gap: 15px;
        flex-wrap: wrap;
    }

    .search input {
        font-size: 16px;
        padding: 8px 15px;
        border-radius: 8px;
        border: 1px solid #ccc;
        min-width: 200px;
    }

    .search button {
        padding: 10px 20px;
        background-color: #28a745;
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .search button:hover {
        background-color: #218838;
    }
    .buttons{
        display: flex;
        align-items: center;
        gap:30px;
    }

    .table-container {
        width: 100%;
        overflow-x: auto;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
        background-color: grey;
        border-radius: 8px;
        overflow: hidden;
    }

    th, td {
        padding: 12px 16px;
        text-align: center;
        border-bottom: 1px solid #ddd;
    }

    thead {
        background-color: #343a40;
        color: black;
    }

    tr:nth-child(even) {
        background-color: #f2f2f2;
    }

    tr:nth-child(odd) {
        background-color: #e9ecef;
    }

    @media (max-width: 768px) {
        .search form {
            flex-direction: column;
            align-items: stretch;
        }

        .search input, .search button {
            width: 100%;
        }
    }
</style>

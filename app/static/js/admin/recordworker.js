// Display workerman 

document.querySelector("#btn-display-recoredworker").onclick = () => {
    let bindDataIntable = document.querySelector("#display-recordworker");
    let  forms = new FormData(document.getElementById("recordworker-hidden-form"));
    bindDataIntable.textContent = "Data loading...";

    fetch("/main/api/record_worker/", {
        method: "POST",
        credentials: "same-origin",
        body: forms,
    }).then(response => response.json())
    .then(result => {
        if (result.error){
            console.log(result.error);
        }
        else {
            let outputs = `
            <table class="order-table table" style="width: 100%" id="main_recordworker_tbl">
            <thead>
                <tr>
                    <th>Id</th>
                    <th>Worker Names</th>
                    <th>Sex</th>
                    <th>Address</th>
                    <th>Contact</th>
                    <th>Salary</th>
                    <th>Recorded Date</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody >`;

            for(let data in result.datas){
                outputs += `<tr>`;
                outputs += `<td>${result.datas[data].id}</td>`;
                outputs += `<td>${result.datas[data].name } ${result.datas[data].lastname}</td>`;
                outputs += `<td>${result.datas[data].gender}</td>`;
                outputs += `<td>${result.datas[data].address}</td>`;
                outputs += `<td>${result.datas[data].contacts}</td>`;
                outputs += `<td>${result.datas[data].currency_type} ${result.datas[data].salary}</td>`;
                outputs += `<td>${result.datas[data].date}</td>`;
                outputs += `<td><center>
                                <a class="btn-editworker" name="${result.datas[data].id}">Edit</a>
                                <a class="btn-delete-worker" name="${result.datas[data].id}">Delete</a>
                            <center></td>`;

                outputs += `</tr>`;
                
            }
                outputs +=`
                </tbody>
            </table>`;
            bindDataIntable.innerHTML = outputs;
            addPagerToTables('#main_provision_tbl', 20);

        }
    }).catch((error) => {
        console.log(error);
    })
}


// Record new workerman

document.querySelector("#btn-recordworker").onclick = () => {
    let bindDataIntable = document.querySelector("#display-recordworker");
    let  forms = new FormData(document.getElementById("recordworker-form"));
    bindDataIntable.textContent = "Data loading...";
    
    fetch("/main/api/record_worker/", {
        method: "POST",
        credentials: "same-origin",
        body: forms,
    }).then(response => response.json())
    .then(result => {
        if (result.error){
            console.log(result.error);
        }
        else {
            let outputs = `
            <table class="order-table table" style="width: 100%" id="main_recordworker_tbl">
            <thead>
                <tr>
                    <th>Id</th>
                    <th>Worker Names</th>
                    <th>Sex</th>
                    <th>Address</th>
                    <th>Contact</th>
                    <th>Salary</th>
                    <th>Recorded Date</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody >`;

            for(let data in result.datas){
                outputs += `<tr>`;
                outputs += `<td>${result.datas[data].id}</td>`;
                outputs += `<td>${result.datas[data].name } ${result.datas[data].lastname}</td>`;
                outputs += `<td>${result.datas[data].gender}</td>`;
                outputs += `<td>${result.datas[data].address}</td>`;
                outputs += `<td>${result.datas[data].contacts}</td>`;
                outputs += `<td>${result.datas[data].currency_type} ${result.datas[data].salary}</td>`;
                outputs += `<td>${result.datas[data].date}</td>`;
                outputs += `<td><center>
                                <a class="btn-editworker" name="${result.datas[data].id}">Edit</a>
                                <a class="btn-delete-worker" name="${result.datas[data].id}">Delete</a>
                            <center></td>`;
                outputs += `</tr>`;
            }
                outputs +=`
                </tbody>
            </table>`;
            bindDataIntable.innerHTML = outputs;
            addPagerToTables('#main_provision_tbl', 20);

        }
    }).catch((error) => {
        console.log(error);
    })
}

// Update worker data "send request to db"

$(document).on('click', '.btn-editworker', function() {
    $id = $(this).attr('name');
    document.getElementById("add-pop-update-worker").style.display ="block";
    document.getElementById("get-worker-hidden").value = $id;

    let forms = new FormData(document.getElementById("get-worker-hidden-form"));

    fetch("/main/api/record_worker/", {
        method: "POST",
        credentials: "same-origin",
        body: forms,
    }).then(response => response.json())
    .then(result => {
        if (result.error){
            console.log(result.error);
        }
        else {
            for(var data in result.datas){
                document.getElementById("worker_name_edt").value = result.datas[data].name;
                document.getElementById("worker_lastname_edt").value = result.datas[data].lastname;
                // document.getElementById("age_edt").value = result.datas[data].age;
                document.getElementById("sex_edt").value = result.datas[data].gender;
                document.getElementById("salary_edt").value = result.datas[data].salary;
                document.getElementById("currency_id_edt").value = result.datas[data].currency_type;
                document.getElementById("contact_edt").value = result.datas[data].contacts;
                document.getElementById("address_edt").value = result.datas[data].address
                document.getElementById("record_worker_updated").value = result.datas[data].id;
            }
        }

    }).catch((error) => {
        console.log(error);
    })
})

// Update worker data 

document.querySelector("#btn-updateworkers").onclick = () => {
    let bindDataIntable = document.querySelector("#display-recordworker");
    let  forms = new FormData(document.getElementById("updateworkers-form"));
    bindDataIntable.textContent = "Data loading...";

   
    fetch("/main/api/record_worker/", {
        method: "POST",
        credentials: "same-origin",
        body: forms,
    })
.then(response => response.json())
    .then(result => {
        if (result.error){
            console.log(result.error);
        }
        else {
            let outputs = `
            <table class="order-table table" style="width: 100%" id="main_recordworker_tbl">
            <thead>
                <tr>
                    <th>Id</th>
                    <th>Worker Names</th>
                    <th>Sex</th>
                    <th>Address</th>
                    <th>Contact</th>
                    <th>Salary</th>
                    <th>Recorded Date</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody >`;

            for(let data in result.datas){
                outputs += `<tr>`;
                outputs += `<td>${result.datas[data].id}</td>`;
                outputs += `<td>${result.datas[data].name } ${result.datas[data].lastname}</td>`;
                outputs += `<td>${result.datas[data].gender}</td>`;
                outputs += `<td>${result.datas[data].address}</td>`;
                outputs += `<td>${result.datas[data].contacts}</td>`;
                outputs += `<td>${result.datas[data].currency_type} ${result.datas[data].salary}</td>`;
                outputs += `<td>${result.datas[data].date}</td>`;
                outputs += `<td><center>
                                <a class="btn-editworker" name="${result.datas[data].id}">Edit</a>
                                <a class="btn-delete-worker" name="${result.datas[data].id}">Delete</a>
                            <center></td>`;
                outputs += `</tr>`;
            }
                outputs +=`
                </tbody>
            </table>`;
            bindDataIntable.innerHTML = outputs;
            document.getElementById("add-pop-update-worker").style.display ="none";
            addPagerToTables('#main_provision_tbl', 20);

        }
    }).catch((error) => {
        console.log(error);
    })
}

// Remove Workerman from db 
// Open pop screen

$(document).on('click', '.btn-delete-worker', function(){
    $id = $(this).attr('name')
    document.getElementById('add-pop-remove-worker').style.display = "block";
    document.getElementById('remove_worker').value = $id;
});

// Remove content
document.querySelector("#btn-removeworker").onclick = () => {
    let bindDataIntable = document.querySelector("#display-recordworker");
    let  forms = new FormData(document.getElementById("removeworker-form"));
    bindDataIntable.textContent = "Data loading...";

    fetch("/main/api/record_worker/", {
        method: "POST",
        credentials: "same-origin",
        body: forms,
    }).then(response => response.json())
    .then(result => {
        if (result.error){
            console.log(result.error);
        }
        else {
            let outputs = `
            <table class="order-table table" style="width: 100%" id="main_recordworker_tbl">
            <thead>
                <tr>
                    <th>Id</th>
                    <th>Worker Names</th>
                    <th>Sex</th>
                    <th>Address</th>
                    <th>Contact</th>
                    <th>Salary</th>
                    <th>Recorded Date</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody >`;

            for(let data in result.datas){
                outputs += `<tr>`;
                outputs += `<td>${result.datas[data].id}</td>`;
                outputs += `<td>${result.datas[data].name } ${result.datas[data].lastname}</td>`;
                outputs += `<td>${result.datas[data].gender}</td>`;
                outputs += `<td>${result.datas[data].address}</td>`;
                outputs += `<td>${result.datas[data].contacts}</td>`;
                outputs += `<td>${result.datas[data].currency_type} ${result.datas[data].salary}</td>`;
                outputs += `<td>${result.datas[data].date}</td>`;
                outputs += `<td><center>
                                <a class="btn-editworker" name="${result.datas[data].id}">Edit</a>
                                <a class="btn-delete-worker" name="${result.datas[data].id}">Delete</a>
                            <center></td>`;
                outputs += `</tr>`;
            }
                outputs +=`
                </tbody>
            </table>`;
            bindDataIntable.innerHTML = outputs;
            document.getElementById('add-pop-remove-worker').style.display = "none";
            addPagerToTables('#main_provision_tbl', 20);

        }
    }).catch((error) => {
        console.log(error);
    })
}
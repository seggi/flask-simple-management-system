// Display all expenses 

document.querySelector("#btn-display-all-expenses").onclick = () => {
    let bindDataIntable = document.querySelector("#display-expenses-tbl");
    let forms = new FormData(document.getElementById('get-all-expenses-form'));
    bindDataIntable.textContent = "Data loading...";

    document.getElementById("payment-box").style.display ="none";
    document.getElementById("display-expenses-tbl").style.display = "block";
    

    fetch("/main/api/expenses/", {
        method:"POST",
        credentials: "same-origin",
        body: forms,
    }).then(response => response.json())
    .then(result => {
        if(result.error) {
            console.log(result.error);
        }

        let outputs = `
        <table class="order-table table" style="width: 100%" id="main_expenses_tbl">
        <thead>
            <tr>
                <th>Id</th>
                <th>Designation</th>
                <th>Amount</th>
                <th>Date</th>
            </tr>
        </thead>
        <tbody >`;

        for(let data in result.datas){
        
            outputs +=`<tr>`
            outputs += `<td>${result.datas[data].id}</td>`;
            outputs += `<td>${result.datas[data].description}</td>`;
            outputs += `<td>${result.datas[data].amount}</td>`;
            outputs += `<td>${result.datas[data].date}</td>`;
            outputs +=`</tr>`;
            
        }

        outputs +=`
                </tbody>
            </table>`;
        bindDataIntable.innerHTML = outputs;
        addPagerToTables('#main_expenses_tbl', 20);
    }).catch((error) => {
        console.log(error);
    })

}

// Employee payment 

document.querySelector("#btn-employee-payment-form").onclick = () => {
    let bindDataIntable = document.querySelector("#display-expenses-tbl1");
    let forms = new FormData(document.getElementById('employee-payment-form'));
    bindDataIntable.textContent = "Data loading...";


    fetch("/main/api/expenses/payment/", {
        method:"POST",
        credentials: "same-origin",
        body: forms,
    }).then(response => response.json())
    .then(result => {
        if(result.error) {
            console.log(result.error);
        }

        for(var data in result.datas1){
            document.getElementById("fsalary").value = result.datas1[data].salary
        }

        let outputs = `
        <table class="order-table table" style="width: 100%" id="main_expenses_tbl1">
        <thead>
            <tr>
                <th>Id</th>
                <th>Designation</th>
                <th>Amount</th>
                <th>Date</th>
            </tr>
        </thead>
        <tbody >`;

        for(let data in result.datas){
        
            outputs +=`<tr>`
            outputs += `<td>${result.datas[data].id}</td>`;
            outputs += `<td>${result.datas[data].description}</td>`;
            outputs += `<td>${result.datas[data].amount}</td>`;
            outputs += `<td>${result.datas[data].date}</td>`;
            outputs +=`</tr>`;
            
        }

        outputs +=`
                </tbody>
            </table>`;
        bindDataIntable.innerHTML = outputs;
        addPagerToTables('#main_expenses_tbl1', 20);
    }).catch((error) => {
        console.log(error);
    })

}

// Record other expenses 

document.querySelector("#btn-otherexpenses").onclick = () => {
    let bindDataIntable = document.querySelector("#display-expenses-tbl1");
    let forms = new FormData(document.getElementById('other-expenses-form'));
    bindDataIntable.textContent = "Data loading...";


    fetch("/main/api/expenses/payment/", {
        method:"POST",
        credentials: "same-origin",
        body: forms,
    }).then(response => response.json())
    .then(result => {
        if(result.error) {
            console.log(result.error);
        }

        let outputs = `
        <table class="order-table table" style="width: 100%" id="main_expenses_tbl1">
        <thead>
            <tr>
                <th>Id</th>
                <th>Designation</th>
                <th>Amount</th>
                <th>Date</th>
            </tr>
        </thead>
        <tbody >`;

        for(let data in result.datas){
        
            outputs +=`<tr>`
            outputs += `<td>${result.datas[data].id}</td>`;
            outputs += `<td>${result.datas[data].description}</td>`;
            outputs += `<td>${result.datas[data].amount}</td>`;
            outputs += `<td>${result.datas[data].date}</td>`;
            outputs +=`</tr>`;
        }

        outputs +=`
                </tbody>
            </table>`;
        bindDataIntable.innerHTML = outputs;
        addPagerToTables('#main_expenses_tbl1', 20);
        document.getElementById("payment-box").style.display = "block";
        document.getElementById("display-expenses-tbl").style.display = "none";
        document.getElementById("add-pop-other-expenses").style.display = "none";
    }).catch((error) => {
        console.log(error);
    })

}
//  Provision Session 
// Display physical product table 


document.querySelector("#btn-display-physicalproduct").onclick = () => {
    let bindDataIntable = document.querySelector("#display-physical-product");
    const forms = new FormData(document.getElementById("addphysicalproduct-hidden-form"));
    bindDataIntable.textContent = "Data loading...";

    fetch("/main/api/save_physical_product/", {
        method: "POST",
        credentials: "same-origin",
        body: forms,
    }).then(response => response.json())
    .then(result => {
        if(result.error) {
            alert(result.error)
            console.log(result.error);
        }

        let outputs = `
        <table class="order-table table" style="width: 100%" id="main_provision_tbl">
        <thead>
            <tr>
                <th>Id</th>
                <th>Product</th>
                <th>Description</th>
                <th>Unit price</th>
                <th>Tot price</th>
                <th>Currency</th>
                <th>Stock</th>
                <th>Record Date</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody >`;

        for(let data in result.datas){
            // 
            console.log(result.datas[data]);
            outputs +=`<tr>`;
            outputs += `<td>${result.datas[data].product_id}</td>`;
            outputs += `<td>${result.datas[data].product_name}</td>`;
            outputs += `<td>${result.datas[data].description}</td>`;
            outputs += `<td>${result.datas[data].unit_price}</td>`;
            outputs += `<td>${result.datas[data].tot_price}</td>`;
            outputs += `<td>${result.datas[data].currency_type}</td>`;
            outputs += `<td>${result.datas[data].quantity}</td>`;
            outputs += `<td>${result.datas[data].date}</td>`;
            outputs += `<td>
                        <center>
                            <a class="btn-edit"  id="btn-edit" name="${result.datas[data].product_id}">Update</a>
                        <center></td>`;
                        
            outputs +=`</tr>`;
        }

        outputs +=`
                </tbody>
            </table>`;
        bindDataIntable.innerHTML = outputs;
        addPagerToTables('#main_provision_tbl', 20);
    }).catch((error) => {
        console.log(error);
    });
}


// Add physical product 


document.querySelector("#btn-add-physical-product").onclick = () => {
    let bindDataIntable = document.querySelector("#display-physical-product");
    const forms = new FormData(document.getElementById("addphysicalproduct-form"));
    bindDataIntable.textContent = "Data loading...";
    
    fetch("/main/api/save_physical_product/", {
        method: "POST",
        credentials: "same-origin",
        body: forms,
    }).then(response => response.json())
    .then(result => {
        
        if(result.error) {
            alert(result.error)
            console.log(result.error);
        }

        let outputs = `
        <table class="order-table table" style="width: 100%" id="main_provision_tbl">
        <thead>
            <tr>
                <th>Id</th>
                <th>Product</th>
                <th>Description</th>
                <th>Unit price</th>
                <th>Tot price</th>
                <th>Currency</th>
                <th>Stock</th>
                <th>Record Date</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody >`;

        for(let data in result.datas){
            // 
            
            console.log(result.datas[data]);
            outputs +=`<tr>`
            outputs += `<td>${result.datas[data].product_id}</td>`;
            outputs += `<td>${result.datas[data].product_name}</td>`;
            outputs += `<td>${result.datas[data].description}</td>`;
            outputs += `<td>${result.datas[data].unit_price}</td>`;
            outputs += `<td>${result.datas[data].tot_price}</td>`;
            outputs += `<td>${result.datas[data].currency_type}</td>`;
            outputs += `<td>${result.datas[data].quantity}</td>`;
            outputs += `<td>${result.datas[data].date}</td>`;
            outputs += `<td><center>
                    <a class="btn-edit" name="${result.datas[data].product_id}">Update</a>
                <center></td>`;
            outputs +=`</tr>`;
            
        }

        outputs +=`
                </tbody>
            </table>`;
        bindDataIntable.innerHTML = outputs;
        addPagerToTables('#main_provision_tbl', 20);
    }).catch((error) => {
        console.log(error);
    });
}

// Update physical product "send request to db"

$(document).on('click', '.btn-edit', function() {
    $id = $(this).attr('name');
    document.getElementById('edit-pop-physical-product').style.display = "block";
    document.getElementById('edit-product').value = $id;
    
    let forms = new FormData(document.getElementById('edit-pop-physical-product-hidden'));

    fetch("/main/api/save_physical_product/", {
        method: "POST",
        credentials: "same-origin", 
        body: forms,
    }).then(response => response.json())
    .then(result => {
        if (result.error) {
            console.log(`${result.error}`);
        }
        else {
            for(let data in result.datas){
                document.getElementById("product_name_edt").value = result.datas[data].product_name;
                document.getElementById("product_designation_edt").value = result.datas[data].description;
                document.getElementById("unit_price_edt").value = result.datas[data].unit_price;
                document.getElementById("quantity_edt").value = result.datas[data].quantity;
                document.getElementById("tot_price_edt").value = result.datas[data].tot_price;
                document.getElementById("physical_product_edt").value = result.datas[data].product_id;
                document.getElementById("product_currency_edt").value = result.datas[data].currency_type;
                
            }
        }

    }).catch((error) => {
        console.error(error);
    })
});

// Update product data  

document.querySelector("#btn-edit-physical-product").onclick = () =>{
    let bindDataIntable = document.querySelector("#display-physical-product");
    const forms = new FormData(document.getElementById("editphysicalproduct-form"));
    bindDataIntable.textContent = "Data loading...";

    fetch("/main/api/save_physical_product/", {
        method:"POST",
        credentials: "same-origin",
        body: forms,
    }).then(response => response.json())
    .then(result => {
        if(result.error) {
            alert(result.error)
            console.log(result.error);
        }

        let outputs = `
        <table class="order-table table" style="width: 100%" id="main_provision_tbl">
        <thead>
            <tr>
                <th>Id</th>
                <th>Product</th>
                <th>Description</th>
                <th>Unit price</th>
                <th>Tot price</th>
                <th>Currency</th>
                <th>Stock</th>
                <th>Record Date</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody >`;

        for(let data in result.datas){
        
            outputs +=`<tr>`
            outputs += `<td>${result.datas[data].product_id}</td>`;
            outputs += `<td>${result.datas[data].product_name}</td>`;
            outputs += `<td>${result.datas[data].description}</td>`;
            outputs += `<td>${result.datas[data].unit_price}</td>`;
            outputs += `<td>${result.datas[data].tot_price}</td>`;
            outputs += `<td>${result.datas[data].currency_type}</td>`;
            outputs += `<td>${result.datas[data].quantity}</td>`;
            outputs += `<td>${result.datas[data].date}</td>`;
            outputs += `<td><center><a class="btn-edit" name="${result.datas[data].product_id}">Update</a><center></td>`;
            outputs +=`</tr>`;
            
        }

        outputs +=`
                </tbody>
            </table>`;
        bindDataIntable.innerHTML = outputs;
        addPagerToTables('#main_provision_tbl', 20);
    }).catch((error) => {
        console.log(error);
    })
}


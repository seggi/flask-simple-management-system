// Prevent default submition 
function defaultPrevented(){
    return false;
}

// Send product id found 
document.querySelector("#btn-getproductfound").onclick = () => {
    let bindDataIntable = document.querySelector("#display-purchaseitem1");
    let forms = new FormData(document.getElementById('getproductfound-form'));
    bindDataIntable.textContent = "Data loading...";

    fetch('/main/api/live_search/', {
        method: 'POST',
        credentials: 'same-origin',
        body: forms,
    }).then(response => response.json())
    .then(result => {
        
        if (result.error) {
            console.log(`${result.error}`);
        }
        else {
            for (var data in result.datas){
                document.getElementById("fproduct_name").value = result.datas[data].product_name;
                document.getElementById("fdescription").value = result.datas[data].description;
                document.getElementById("funit_price").value = result.datas[data].currency_type+' '+result.datas[data].unit_price;
                document.getElementById("fstock").value = result.datas[data].quantity;
            }

            let outputs = `
        <table class="order-table table" style="width: 100%" id="main_solditem_tbl">
        <thead>
            <tr>
                <th>Date</th>
                <th>Id</th>
                <th>Item</th>
                <th>Product</th>
                <th>Amount</th>
                <th>Quantity</th>
                <th>Client</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody >`;

        for(let data in result.datas1){

            outputs +=`<tr>`
            outputs += `<td>${result.datas1[data].date}</td>`;
            outputs += `<td>${result.datas1[data].solditemid}</td>`;
            outputs += `<td>${result.datas1[data].itemid}</td>`;
            outputs += `<td>${result.datas1[data].product_name}</td>`;
            outputs += `<td>${result.datas1[data].montant}</td>`;
            outputs += `<td>${result.datas1[data].sold_quantity}</td>`;
            outputs += `<td>${result.datas1[data].client}</td>`;
            outputs += `<td><center><a class="btn-edit" name="${result.datas1[data].id}">Invoice</a><center></td>`;
            outputs +=`</tr>`;
            
        }

        outputs +=`
                </tbody>
            </table>`;
        bindDataIntable.innerHTML = outputs;
        addPagerToTables('#main_solditem_tbl', 20);


        }
    }).catch((error) => {
        console.log(error);
    })
}

// Sell product form 

document.querySelector("#btn-sell-product-formitem").onclick = () => {
    let bindDataIntable = document.querySelector("#display-purchaseitem1");
    let forms = new FormData(document.getElementById('sell-product-form-item'));
    bindDataIntable.textContent = "Data loading...";

    fetch('/main/api/live_search/', {
        method: "POST",
        credentials: "same-origin",
        body: forms,
    }).then(response => response.json())
    .then(result => {

        if(result.error) {
            console.log(result.error);
        }

        for(var data in result.datas1){
            document.getElementById("fstock").value = result.datas1[data].quantity;
        }

        let outputs = `
        <table class="order-table table" style="width: 100%" id="main_solditem_tbl">
        <thead>
            <tr>
                <th>Date</th>
                <th>Id</th>
                <th>Item</th>
                <th>Product</th>
                <th>Amount</th>
                <th>Quantity</th>
                <th>Client</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody >`;

        for(let data in result.datas){

            outputs +=`<tr>`
            outputs += `<td>${result.datas[data].date}</td>`;
            outputs += `<td>${result.datas[data].solditemid}</td>`;
            outputs += `<td>${result.datas[data].itemid}</td>`;
            outputs += `<td>${result.datas[data].product_name}</td>`;
            outputs += `<td>${result.datas[data].montant}</td>`;
            outputs += `<td>${result.datas[data].sold_quantity}</td>`;
            outputs += `<td>${result.datas[data].client}</td>`;
            outputs += `<td><center><a class="btn-edit" name="${result.datas[data].id}">Invoice</a><center></td>`;
            outputs +=`</tr>`;
            
        }

        outputs +=`
                </tbody>
            </table>`;
        bindDataIntable.innerHTML = outputs;
        addPagerToTables('#main_solditem_tbl', 20);

    }).catch((error) => {
        console.log(error);
    })
}

// Display all selling activies

document.querySelector("#btn-get-all-sold-product").onclick = () => {
    document.getElementById("purchaseitem-box").style.display ="none";
    document.getElementById("display-purchaseitem").style.display = "block";

    let bindDataIntable = document.querySelector("#display-purchaseitem");
    let forms = new FormData(document.getElementById('get-sold-product-form'));
    bindDataIntable.textContent = "Data loading...";

    fetch('/main/api/live_search/', {
        method: "POST",
        credentials: "same-origin",
        body: forms,
    }).then(response => response.json())
    .then(result => {

        if(result.error) {
            console.log(result.error);
        }

        for(var data in result.datas1){
            document.getElementById("fstock").value = result.datas1[data].quantity;
        }

        let outputs = `
        <table class="order-table table" style="width: 100%" id="main_solditem_tbl">
        <thead>
            <tr>
                <th>Date</th>
                <th>Id</th>
                <th>Item</th>
                <th>Product</th>
                <th>Amount</th>
                <th>Quantity</th>
                <th>Client</th>
                
            </tr>
        </thead>
        <tbody >`;

        for(let data in result.datas){

            outputs +=`<tr>`
            outputs += `<td>${result.datas[data].date}</td>`;
            outputs += `<td>${result.datas[data].solditemid}</td>`;
            outputs += `<td>${result.datas[data].itemid}</td>`;
            outputs += `<td>${result.datas[data].product_name}</td>`;
            outputs += `<td>${result.datas[data].montant}</td>`;
            outputs += `<td>${result.datas[data].sold_quantity}</td>`;
            outputs += `<td>${result.datas[data].client}</td>`;
            // outputs += `<td><center><a class="btn-edit" name="${result.datas[data].id}">Invoice</a><center></td>`;
            outputs +=`</tr>`;
            
        }

        outputs +=`
                </tbody>
            </table>`;
        bindDataIntable.innerHTML = outputs;
        addPagerToTables('#main_solditem_tbl', 20);

    }).catch((error) => {
        console.log(error);
    })
}

// Display cash out 

const diplayCashOut = () => {
    // let forms = new FormData(document.getElementById("hidden-cashout-form"));
    let bindDataIntable = document.querySelector("#display-cashbook");
    bindDataIntable.textContent = "Data loading...";

    fetch("/main/api/cash_book/", {
        // method: "POST", 
        // credentials: "same-origin",
        // body: forms,
    }).then(response => response.json())
    .then(result => {
        if(result.error) {
            console.log(result.error);
        }
    
       else {
            for(let data in result.datas1){  
                document.getElementById("amountsolddebit").textContent =result.datas1[data].currency_type+''+result.datas1[data].debit;
                document.getElementById("amountsoldcredit").textContent = result.datas1[data].currency_type+''+result.datas1[data].credit;
                var totcash = result.datas1[data].debit - result.datas1[data].credit;
            
                document.getElementById("tot-cash").textContent = result.datas1[data].currency_type+' '+totcash;
            }   

            let outputs = `
            <table class="order-table table" style="width: 100%" id="main_cashbook_tbl">
            <thead>
                <tr>
                    <th>Id</th>
                    <th>Designation</th>
                    <th>Debit</th>
                    <th>Credit</th>
                    <th>Date</th>
                </tr>
            </thead>
            <tbody >`;

            for(let data in result.datas){
                outputs +=`<tr>`
                outputs += `<td>${result.datas[data].id}</td>`;
                outputs += `<td>${result.datas[data].description}</td>`;
                outputs += `<td>${result.datas[data].currency_type} ${result.datas[data].debit}</td>`;
                outputs += `<td>${result.datas[data].currency_type} ${result.datas[data].credit}</td>`;
                // utputs += `<td>${result.datas[data].credit}</td>`;
                outputs += `<td>${result.datas[data].date}</td>`;
                outputs +=`</tr>`;
            }

            outputs +=`
                    </tbody>
                </table>`;
            bindDataIntable.innerHTML = outputs;
            addPagerToTables('#main_cashbook_tbl', 20);
       }
    })
    .catch((error) => {
        console.log(error);
    })
}


// ============================= Print table ===================
// =============================================================

function printData()
{
   var divToPrint=document.getElementById("main_cashbook_tbl");

   var style = "<style>";
   style = style + "table {width: 100%; font: 17px Calibri;}";
   style = style + "table, th, td {border: solid 1px #DDD; border-collapse: collapse;";
   style = style + "padding: 2px 3px; text-align: center;}";
   style = style + "</style>";
   newWin= window.open("", "", 'height=700,width=700');
   newWin.document.write(style);
   newWin.document.write(divToPrint.innerHTML);
   newWin.print();
   newWin.close();
}

$('#getbutton').on('click',function(){
printData();
})
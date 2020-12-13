// Add product

function openAddPhysicalProductPop() {
    document.getElementById("add-pop-physical-product").style.display ="block";
}

function closeAddPhysicalProductPop(){
    document.getElementById("add-pop-physical-product").style.display ="none";
}

function closeEditPhysicalProductPop(){
    document.getElementById("edit-pop-physical-product").style.display ="none";
}

// Record worker

function closeRecordWorkerPop(){
    document.getElementById("add-pop-record-worker").style.display ="none";
}

function openRecordWorkerPop(){
    document.getElementById("add-pop-record-worker").style.display ="block";
}

// Update worker data 

function closeUpdateWorkerPop() {
    document.getElementById("add-pop-update-worker").style.display ="none";
}

// Remove worker pop screen

function closeRemoveWorkerPop() {
    document.getElementById("add-pop-remove-worker").style.display ="none";
}

// Purchase session screen

function openPurchasePop() {
    document.getElementById("purchaseitem-box").style.display ="block";
    document.getElementById("display-purchaseitem").style.display = "none";
}


// Expenses session screen 

function openPaymentPop() {
    document.getElementById("payment-box").style.display = "block";
    document.getElementById("display-expenses-tbl").style.display = "none";
}

function closeRecordExpensesPop(){
    document.getElementById("add-pop-other-expenses").style.display = "none";
}

function openRecordExpensesPop() {
    document.getElementById("add-pop-other-expenses").style.display = "block";
}

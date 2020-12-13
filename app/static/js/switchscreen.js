// diplayCashOut

function cashBook() {
    document.getElementById("session1").style.display = "block";
    document.getElementById("session2").style.display = "none";
    document.getElementById("session3").style.display = "none";
    document.getElementById("Purchase-session").style.display = "none";
    document.getElementById("session5").style.display = "none";
    diplayCashOut();
}


function Provision() {
    document.getElementById("session1").style.display = "none";
    document.getElementById("session2").style.display = "block";
    document.getElementById("session3").style.display = "none";
    document.getElementById("Purchase-session").style.display = "none";
    document.getElementById("session5").style.display = "none";
}

function Expenses() {
    document.getElementById("session1").style.display = "none";
    document.getElementById("session2").style.display = "none";
    document.getElementById("session3").style.display = "block";
    document.getElementById("Purchase-session").style.display = "none";
    document.getElementById("session5").style.display = "none";
}

function Sell() {
    document.getElementById("session1").style.display = "none";
    document.getElementById("session2").style.display = "none";
    document.getElementById("session3").style.display = "none";
    document.getElementById("Purchase-session").style.display = "block";
    document.getElementById("session5").style.display = "none";

}

function Employee() {
    document.getElementById("session1").style.display = "none";
    document.getElementById("session2").style.display = "none";
    document.getElementById("session3").style.display = "none";
    document.getElementById("Purchase-session").style.display = "none";
    document.getElementById("session5").style.display = "block";
}
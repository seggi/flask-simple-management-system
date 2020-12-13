// Search Employee 

const results1 = document.getElementById('results1');
const search_input1 =  document.getElementById('search1');
const employeesalary = document.getElementById('hdn-employeesalary');
const employeeid = document.getElementById('hidden-esearch-id');
const employeefullname =  document.getElementById('hdn-employeefullname');

const femployeename = document.getElementById('femployee_name');
const fsalary = document.getElementById('fsalary');
const currency_type_payment = document.getElementById('currency_type_payment')

let search_term1 = '';
let employeefound;

let items = { text: 'Jaja Lumoo' }

const fetchEmployee = async () => {
    employeefound = await fetch(
        '/main/api/expenses/payment/', 
    ).then(response => response.json());
};

const showEmployee = async () => {
    results1.innerHTML = '';
    await fetchEmployee();

    const ul = document.createElement('ul');
    ul.classList.add('item-data-found');

    employeefound.filter(employee => 
        employee.name.toLowerCase().includes(search_term1.toLowerCase()))
        .forEach(employee => {
            const li = document.createElement('li');
            li.classList.add('item-element');

            const employeename = document.createElement('h3');
            employeename.innerHTML = employee.name +' '+employee.lastname;

            const btncontent = document.createElement('a');
            btncontent.classList.add('item-found-details');
            btncontent.onclick = function(event) {
                search_input1.value = btncontent.innerText;
                employeeid.value = employee.id;
                fsalary.value = employee.currency_type+' '+employee.salary;
                femployeename.value = employee.name +' '+employee.lastname;
                employeesalary.value = employee.salary;
                employeefullname.value = employee.name +' '+employee.lastname;
                currency_type_payment.value = employee.currency_id;
                results1.style.display = "none";
            }
            btncontent.appendChild(employeename)
            li.appendChild(btncontent)
            ul.appendChild(li)
        });
    results1.appendChild(ul);
};

search_input1.addEventListener('input', e => {
    search_term1 = e.target.value;
    results1.style.display = "block";
    showEmployee();
})





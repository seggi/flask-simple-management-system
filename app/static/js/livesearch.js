// Search Purchase product

const results = document.getElementById('results');
const search_input =  document.getElementById('search');
const gethiddenid = document.getElementById('hidden-search-id');
const sellproductidhidden = document.getElementById('product-to-sell_id');
const sellproductcurrency = document.getElementById('currency_type')
const productvalue = document.getElementById('productvalue')

let search_term = '';
let itemsfound;



let data = {
    text: 'Ampoule blue',
}


const fetchItems = async () => {
    itemsfound = await fetch(
        '/main/api/live_search/',{
    }).then(response => response.json())
    .then(result => result);
    
};

const showItems = async () => {
    // clear the results
    results.innerHTML = '';
   
    // getting the data 
    await fetchItems();

    const ul = document.createElement('ul');
    ul.classList.add('item-data-found');
    
    itemsfound.filter(items => 
        items.product_name.toLowerCase().includes(search_term.toLowerCase())
    )
        .forEach(items => {
            // Create the struture 
            const li = document.createElement('li');
            li.classList.add('item-element');

            // Setting content data
            const product_name = document.createElement('h3');
            product_name.innerText = items.product_name;
            
            // product_name.classList.add('item-found-details');

             // Create button 
             const btncontent = document.createElement('a');
             btncontent.classList.add('item-found-details');
             btncontent.onclick = function(envent) {
                search_input.value = btncontent.innerText;
                gethiddenid.value = items.product_id;
                sellproductidhidden.value = items.product_id;
                sellproductcurrency.value = items.currency_id;
                productvalue.value = items.unit_price;
                results.style.display = "none";
                console.log(gethiddenid.value + search_input.value + sellproductcurrency.value)
             }

            btncontent.appendChild(product_name)

            li.appendChild(btncontent);
            ul.appendChild(li);
        });
      

    results.appendChild(ul);
      // hide live search items

};

search_input.addEventListener('input', e => {
    // saving the input value
    search_term = e.target.value;
    results.style.display = "block";
    // re-displaying items based on the new search_iterm
    showItems();
    
});




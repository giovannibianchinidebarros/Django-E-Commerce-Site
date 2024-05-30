// document.getElementById("navbarcart").setAttribute('data-bs-content', '<h4>This is your Cart</h4>');



const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]');
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl));


var value = "some_value";
document.cookie="key="+value;



if(localStorage.getItem('cart')==null){
    var cart = {};
}
else{
    cart = JSON.parse(localStorage.getItem('cart'));
}


$(document).on('click', '.addtocart', function(){
    // console.log('the add to card button was clicked!!');
    var item_id = this.id.toString();
    
    if(cart[item_id]!=undefined){
        cart[item_id] += 1;
    }
    else{
        cart[item_id] = 1;
    }
    // console.log(`item_id: ${item_id}   ---  qtd: ${cart[item_id]}` );
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById("navbarcart").innerHTML = `Cart(${Object.keys(cart).length})`;

    displayCart(cart);
   
})

function displayCart(cart){
    
    var cartString = "";
    cartString += "<h4>This is your Cart</h4>";
    
    for(let itemId in cart){
        cartString += `item: ${itemId}    qtd: ${cart[itemId]} </br>`;
    };
    cartString += '</br><a href="/checkout" class="btn btn-warning" id="checkout">Checkout</a>';
    
    document.getElementById("navbarcart").setAttribute('data-bs-content', cartString);
    var popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl));

}
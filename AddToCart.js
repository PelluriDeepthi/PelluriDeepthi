// Simulated user credentials
const validUsername = "user123";
const validPassword = "pass456";

document.getElementById("loginButton").addEventListener("click", function () {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username === validUsername && password === validPassword) {
        window.location.href = "AddToCartProducts.html";
    } else {
        alert("Invalid credentials. Please try again.");
    }
});



// Add to Cart functionality
document.getElementById("addToCart").addEventListener("click", function () {
    const selectedProduct = document.getElementById("categoryDropdown").value;
    const cartItemsList = document.getElementById("cartItems");
    const CartItemCount = document.getElementById("cartItemCount");

    const newItem = document.createElement("li");
    newItem.textContent = selectedProduct;
    newItem.classList.add("cart-item");

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Remove";
    deleteButton.classList.add("delete-button");
    deleteButton.addEventListener("click", function () {
        cartItemsList.removeChild(newItem);
        updateCartItemCount();
    });

    newItem.appendChild(deleteButton);
    cartItemsList.appendChild(newItem);
    updateCartItemCount();
});

// Clear Cart functionality
document.getElementById("clearCart").addEventListener("click", function () {
    const cartItemsList = document.getElementById("cartItems");
    cartItemsList.innerHTML = "";
    updateCartItemCount();
});

// Update cart item count
function updateCartItemCount() {
    const cartItemsList = document.getElementById("cartItems");
    const cartItemCount = document.getElementById("cartItemCount");
    const itemCount = cartItemsList.children.length;
    cartItemCount.textContent = `Items in cart: ${itemCount}`;
}
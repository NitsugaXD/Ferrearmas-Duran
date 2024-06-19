let token = '';

function register() {
    const username = document.getElementById('reg_username').value;
    const email = document.getElementById('reg_email').value;
    const password = document.getElementById('reg_password').value;

    fetch('/users/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, email, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.id) {
            window.location.href = '/login/';
        } else {
            document.getElementById('registerError').textContent = 'Registro fallido. Inténtalo de nuevo.';
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('/auth/api-token-auth/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.token) {
            token = data.token;
            window.location.href = '/products/';
        } else {
            document.getElementById('loginError').textContent = 'Login fallido. Inténtalo de nuevo.';
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function fetchProducts() {
    fetch('/products/', {
        headers: {
            'Authorization': `Token ${token}`
        }
    })
    .then(response => response.json())
    .then(products => {
        const productList = document.getElementById('productList');
        productList.innerHTML = '';
        products.forEach(product => {
            const productItem = document.createElement('div');
            productItem.textContent = `${product.name} - $${product.price} - Stock: ${product.stock}`;
            const addButton = document.createElement('button');
            addButton.textContent = 'Añadir al Carrito';
            addButton.onclick = () => addToCart(product.id);
            productItem.appendChild(addButton);
            productList.appendChild(productItem);
        });
    });
}

function addToCart(productId) {
    fetch('/cart/add/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`
        },
        body: JSON.stringify({ product_id: productId, quantity: 1 })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status) {
            fetchCart();
        } else {
            alert('Error al añadir al carrito: ' + data.error);
        }
    });
}

function fetchCart() {
    fetch('/cart/', {
        headers: {
            'Authorization': `Token ${token}`
        }
    })
    .then(response => response.json())
    .then(cart => {
        const cartItems = document.getElementById('cartItems');
        cartItems.innerHTML = '';
        cart.items.forEach(item => {
            const cartItem = document.createElement('div');
            cartItem.textContent = `${item.product.name} - Cantidad: ${item.quantity}`;
            cartItems.appendChild(cartItem);
        });
        document.getElementById('cart').style.display = 'block';
    });
}

function checkout() {
    fetch('/orders/checkout/', {
        method: 'POST',
        headers: {
            'Authorization': `Token ${token}`
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.status) {
            fetchOrders();
        } else {
            alert('Error durante el pago: ' + data.error);
        }
    });
}

function fetchOrders() {
    fetch('/orders/', {
        headers: {
            'Authorization': `Token ${token}`
        }
    })
    .then(response => response.json())
    .then(orders => {
        const orderList = document.getElementById('orderList');
        orderList.innerHTML = '';
        orders.forEach(order => {
            const orderItem = document.createElement('div');
            orderItem.textContent = `Orden #${order.id}`;
            order.products.forEach(product => {
                const productItem = document.createElement('div');
                productItem.textContent = `${product.name} - $${product.price}`;
                orderItem.appendChild(productItem);
            });
            orderList.appendChild(orderItem);
        });
        document.getElementById('orders').style.display = 'block';
    });
}

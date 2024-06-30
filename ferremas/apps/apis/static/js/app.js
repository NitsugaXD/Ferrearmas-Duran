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

document.addEventListener('DOMContentLoaded', function() {
    const productListDiv = document.getElementById('product-list');
    function fetchProducts() {
        fetch('/api/products/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                productListDiv.innerHTML = '<h2>Lista de Productos</h2>';
                data.forEach(product => {
                    const productDiv = document.createElement('div');
                    productDiv.innerHTML = `
                        <p>Código: ${product.codigo}</p>
                        <p>Marca: ${product.marca}</p>
                        <p>Nombre: ${product.nombre}</p>
                        <p>Precio: ${product.precio}</p>
                        <p>Stock: ${product.stock}</p>
                        <hr>
                    `;
                    productListDiv.appendChild(productDiv);
                });
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                productListDiv.innerText = 'Error al cargar la lista de productos';
            });
    }

    // Obtener y mostrar la lista de productos cuando se carga la página
    fetchProducts();
});


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

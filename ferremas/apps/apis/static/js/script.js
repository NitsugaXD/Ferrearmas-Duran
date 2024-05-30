// scripts.js

document.addEventListener('DOMContentLoaded', function() {
    // Función para obtener y mostrar la lista de productos
    function getProductList() {
        fetch('/api/productos/')
            .then(response => response.json())
            .then(data => {
                const productListDiv = document.getElementById('product-list');
                productListDiv.innerHTML = '<h2>Lista de Productos</h2>';
                data.forEach(product => {
                    const productDiv = document.createElement('div');
                    productDiv.innerHTML = `
                        <p>${product.nombre} - Precio: ${product.precio}</p>
                        <button onclick="addToCart(${product.codigo})">Agregar al carrito</button>
                    `;
                    productListDiv.appendChild(productDiv);
                });
            });
    }

    // Función para agregar un producto al carrito
    function addToCart(productCode) {
        fetch(`/api/carro/productos/?codigo=${productCode}&cantidad=1`, {
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => {
            alert(data.mensaje);
        });
    }

    // Obtener y mostrar la lista de productos cuando se carga la página
    getProductList();
});

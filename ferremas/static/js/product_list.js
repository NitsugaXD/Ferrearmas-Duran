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

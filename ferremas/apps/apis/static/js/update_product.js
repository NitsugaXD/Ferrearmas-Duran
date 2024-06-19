document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('update-product-form');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const formData = {
            codigo: form.codigo.value,  // Incluye el código en los datos
            marca: form.marca.value,
            nombre: form.nombre.value,
            precio: form.precio.value,
            stock: form.stock.value,
        };

        const codigo = form.codigo.value;

        fetch(`/api/products/${codigo}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')  // Obtén el token CSRF si es necesario
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.text())  // Leer la respuesta como texto
        .then(text => {
            console.log('Server response:', text);  // Imprimir la respuesta del servidor
            try {
                const data = JSON.parse(text);  // Intentar parsear la respuesta como JSON
                if (data.error) {
                    messageDiv.innerText = data.error;
                } else {
                    messageDiv.innerText = data.mensaje;
                    form.reset();
                }
            } catch (error) {
                console.error('Error parsing JSON:', error, 'Response text:', text);
                messageDiv.innerText = 'Error al procesar la respuesta del servidor';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            messageDiv.innerText = 'Error al actualizar el producto';
        });
    });

    // Función para obtener el token CSRF desde las cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});

# API de Ferremas

Esta API proporciona endpoints para interactuar con productos y carros de compras en la tienda de Ferremas.

## API de Consulta de Productos

Esta API permite consultar información detallada de los productos disponibles en Ferremas.

### Endpoints Disponibles

- **Obtener Lista de Productos**: `GET /api/productos/`
- **Obtener Detalles de un Producto por Código**: `GET /api/productos/<codigo>/`

### Parámetros de Consulta

- `<codigo>`: Código único del producto que se desea consultar.

### Ejemplo de Uso en Postman

#### Obtener Lista de Productos

1. Abre Postman.
2. Selecciona el método GET.
3. Ingresa la URL: `http://localhost:8000/api/productos/`.
4. Haz clic en "Send".

#### Obtener Detalles de un Producto por Código

1. Abre Postman.
2. Selecciona el método GET.
3. Ingresa la URL con el código del producto deseado, por ejemplo: `http://localhost:8000/api/productos/FER-12345/`.
4. Haz clic en "Send".

## API de Gestión de Productos

Esta API permite crear, editar y eliminar productos en Ferremas.

### Endpoints Disponibles

- **Crear un Producto**: `POST /api/productos/`
- **Editar un Producto**: `PUT /api/productos/<codigo>/`
- **Eliminar un Producto**: `DELETE /api/productos/<codigo>/`

### Parámetros de Solicitud

- `<codigo>`: Código único del producto que se desea editar o eliminar.

### Ejemplo de Uso en Postman

#### Crear un Producto

1. Abre Postman.
2. Selecciona el método POST.
3. Ingresa la URL: `http://localhost:8000/api/productos/`.
4. En la sección "Body", selecciona "raw" y "JSON".
5. Ingresa los detalles del producto que deseas crear en formato JSON.
6. Haz clic en "Send".

#### Editar un Producto

1. Abre Postman.
2. Selecciona el método PUT.
3. Ingresa la URL con el código del producto que deseas editar, por ejemplo: `http://localhost:8000/api/productos/FER-12345/`.
4. En la sección "Body", selecciona "raw" y "JSON".
5. Ingresa los nuevos detalles del producto en formato JSON.
6. Haz clic en "Send".

#### Eliminar un Producto

1. Abre Postman.
2. Selecciona el método DELETE.
3. Ingresa la URL con el código del producto que deseas eliminar, por ejemplo: `http://localhost:8000/api/productos/FER-12345/`.
4. Haz clic en "Send".

## API de Carro de Compras

Esta API permite agregar productos al carro de compras en Ferremas.

### Endpoints Disponibles

- **Crear un Carro de Compras**: `POST /api/carro/`

### Parámetros de Solicitud

- `productos`: Lista de IDs de productos que se desean agregar al carro.

### Ejemplo de Uso en Postman

#### Crear un Carro de Compras

1. Abre Postman.
2. Selecciona el método POST.
3. Ingresa la URL: `http://localhost:8000/api/carro/`.
4. En la sección "Body", selecciona "raw" y "JSON".
5. Ingresa el cuerpo de la solicitud con los IDs de los productos que deseas agregar al carro, por ejemplo:

```json
{
    "productos": [1, 2, 3]
}
```

6. Haz clic en "Send".

## Ejemplo de Productos

1. **Taladro Percutor Bosch**
```json
{
    "codigo": "FER-12345",
    "marca": "Bosch",
    "nombre": "Taladro Percutor Bosch",
    "precio": 89090.99,
    "stock": 10
}
```

2. **Set de Destornilladores Stanley (6 piezas)**
```json
{
    "codigo": "FER-67890",
    "marca": "Stanley",
    "nombre": "Set de Destornilladores Stanley (6 piezas)",
    "precio": 25999.99,
    "stock": 20
}
```

3. **Bolsa de Cemento CEMEX (50 kg)**
```json
{
    "codigo": "FER-24680",
    "marca": "CEMEX",
    "nombre": "Bolsa de Cemento CEMEX (50 kg)",
    "precio": 12499.99,
    "stock": 50
}
```

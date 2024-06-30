Entendido, aquí tienes un ejemplo de documentación para tu proyecto:

# Documentación de la API

## Introducción

Este documento describe cómo configurar el entorno, crear las tablas localmente y ejecutar las pruebas unitarias e integradas. También incluye una descripción de los endpoints disponibles en la API.

## Requisitos

- Python 3.x
- Django
- Django REST Framework
- pytest
- pytest-django

## Instalación

1. **Crea un entorno virtual:**

   ```bash
   python -m venv venv
   ```

2. **Activa el entorno virtual:**

   - En Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Aplica las migraciones:**

   ```bash
   python manage.py migrate
   ```

5. **Ejecuta el servidor de desarrollo:**

   ```bash
   python manage.py runserver
   ```

## Endpoints Disponibles:

### Resumen de Endpoints

- **Autenticación**
  - `POST /api/token/`: Obtener un token de autenticación.
  - `POST /api/token/refresh/`: Refrescar el token.

- **Usuarios**
  - `GET /api/users/`: Listar usuarios.
  - `POST /api/users/`: Crear un nuevo usuario.
  - `GET /api/users/<id>/`: Detalle de un usuario.
  - `PUT /api/users/<id>/`: Actualizar un usuario.
  - `DELETE /api/users/<id>/`: Eliminar un usuario.

- **Productos**
  - `GET /api/productos/`: Listar productos.
  - `POST /api/productos/`: Crear un nuevo producto.
  - `GET /api/productos/<id>/`: Detalle de un producto.
  - `PUT /api/productos/<id>/`: Actualizar un producto.
  - `DELETE /api/productos/<id>/`: Eliminar un producto.

- **Carrito**
  - `POST /api/carrito/agregar/`: Agregar productos al carrito.
  - `GET /api/carrito/`: Ver el contenido del carrito.
  - `DELETE /api/carrito/eliminar/<id>/`: Eliminar un producto del carrito.

- **Pedidos**
  - `POST /api/pedidos/`: Crear un nuevo pedido.
  - `GET /api/pedidos/`: Listar pedidos del usuario.
  - `GET /api/pedidos/<id>/`: Detalle de un pedido.

## Ejemplos Endpoints

### Autenticación

- **POST /api/token/**
  - **Entrada:**
    ```json
    {
      "username": "testuser",
      "password": "testpass"
    }
    ```
  - **Resultado esperado:**
    ```json
    {
      "access": "jwt_access_token",
      "refresh": "jwt_refresh_token"
    }
    ```

### Usuarios

- **POST /api/users/**
  - **Entrada:**
    ```json
    {
      "username": "newuser",
      "password": "newpassword",
      "email": "newuser@example.com"
    }
    ```
  - **Resultado esperado:**
    ```json
    {
      "id": 1,
      "username": "newuser",
      "email": "newuser@example.com"
    }
    ```

- **GET /api/users/1/**
  - **Resultado esperado:**
    ```json
    {
      "id": 1,
      "username": "newuser",
      "email": "newuser@example.com"
    }
    ```

### Productos

- **POST /api/productos/**
  - **Entrada:**
    ```json
    {
      "codigo": 123,
      "nombre": "Producto A",
      "precio": 100.0,
      "stock": 50
    }
    ```
  - **Resultado esperado:**
    ```json
    {
      "id": 1,
      "codigo": 123,
      "nombre": "Producto A",
      "precio": 100.0,
      "stock": 50
    }
    ```

- **GET /api/productos/1/**
  - **Resultado esperado:**
    ```json
    {
      "id": 1,
      "codigo": 123,
      "nombre": "Producto A",
      "precio": 100.0,
      "stock": 50
    }
    ```

### Carrito

- **POST /api/carrito/agregar/**
  - **Entrada:**
    ```json
    {
      "codigo": 123,
      "cantidad": 2
    }
    ```
  - **Resultado esperado:**
    ```json
    {
      "mensaje": "Producto 'Producto A' agregado correctamente al carro."
    }
    ```

- **GET /api/carrito/**
  - **Resultado esperado:**
    ```json
    {
      "productos": [
        {
          "codigo": 123,
          "nombre": "Producto A",
          "cantidad": 2,
          "precio": 100.0
        }
      ],
      "total": 200.0
    }
    ```

### Pedidos

- **POST /api/pedidos/**
  - **Entrada:**
    ```json
    {
      "direccion": "123 Calle Principal"
    }
    ```
  - **Resultado esperado:**
    ```json
    {
      "id": 1,
      "usuario": "testuser",
      "direccion": "123 Calle Principal",
      "estado": "pendiente",
      "total": 200.0
    }
    ```

- **GET /api/pedidos/1/**
  - **Resultado esperado:**
    ```json
    {
      "id": 1,
      "usuario": "testuser",
      "direccion": "123 Calle Principal",
      "estado": "pendiente",
      "productos": [
        {
          "codigo": 123,
          "nombre": "Producto A",
          "cantidad": 2,
          "precio": 100.0
        }
      ],
      "total": 200.0
    }
    ```

## Ejecución de Pruebas

Para ejecutar las pruebas unitarias e integradas:

```bash
pytest
```

### Pruebas

El proyecto incluye un total de **32 pruebas** divididas en unitarias e integradas:

- **16 Pruebas Unitarias**
  - Validan la lógica de negocio interna.
- **16 Pruebas de Integración**
  - Validan la interacción entre diferentes partes del sistema.

### Ejemplos de Pruebas

1. **Pruebas de Autenticación:**
   - Creación de usuarios.
   - Autenticación con credenciales válidas e inválidas.

2. **Pruebas de Productos:**
   - CRUD de productos.
   - Validaciones de stock y precios.

3. **Pruebas de Carrito:**
   - Agregar y eliminar productos.
   - Calcular el total del carrito.

4. **Pruebas de Pedidos:**
   - Creación de pedidos.
   - Listar pedidos del usuario.


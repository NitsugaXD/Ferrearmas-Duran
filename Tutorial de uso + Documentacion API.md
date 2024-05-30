
# Documentación de la API

## Introducción

Este documento es un paso a paso para levantar el entorno virutal, crear las tablas localmente, describe los endpoints disponibles en la API, los parámetros necesarios para cada uno, los verbos HTTP utilizados y ejemplos de las respuestas esperadas.

## Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes requisitos:

- Python

## Instalación

1. Crea un entorno virtual:
   ```bash
   python -m venv venv
   ```


2. Activa el entorno virtual:

   - En Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Aplica las migraciones:

   ```bash
   cd ferremas
   python manage.py makemigrations api
   python manage.py migrate
   ```

5. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## Endpoints Disponibles

### 1. Crear y Listar Productos

#### Crear Producto

- **Endpoint:** `/api/productos/`
- **Método HTTP:** `POST`, `GET`

**Solicitud:**

```http
POST /api/productos/
Content-Type: application/json
```

```json
{
    "codigo": 1,
    "marca": "Bosch",
    "nombre": "Taladro Percutor Bosch",
    "precio": 89090,
    "stock": 15
}
```

**Respuesta:**

```json
{
  "codigo": 1,
  "marca": "Bosch",
  "nombre": "Taladro Percutor Bosch",
  "precio": 89090,
  "stock": 15
}
```

#### Listar Productos

**Solicitud:**

```http
GET /api/productos/
```

**Respuesta:**

```json
[
    {
        "codigo": 1,
        "marca": "Bosch",
        "nombre": "Taladro Percutor Bosch",
        "precio": 89090,
        "stock": 15
    },
    
]
```

### 2. Detalle, Actualizar y Eliminar Producto

- **Endpoint:** `/api/productos/<str:codigo>/`
- **Método HTTP:** `GET`, `PUT`, `DELETE`

#### Detalle de Producto

**Solicitud:**

```http
GET /api/productos/1/
```

**Respuesta:**

```json
{
  "codigo": 1,
  "marca": "Bosch",
  "nombre": "Taladro Percutor Bosch",
  "precio": 89090,
  "stock": 15
}
```

#### Actualizar Producto

**Solicitud:**

```http
PUT /api/productos/1/
Content-Type: application/json
```

```json
{
    "codigo": 1,
    "marca": "Bosch",
    "nombre": "Taladro Percutor Bosch",
    "precio": 85000,
    "stock": 10
}
```

**Respuesta:**

```json
{
  "codigo": 1,
  "marca": "Bosch",
  "nombre": "Taladro Percutor Bosch",
  "precio": 85000,
  "stock": 10
}
```

#### Eliminar Producto

**Solicitud:**

```http
DELETE /api/productos/1/
```

**Respuesta:**

```http
# Ejecutar Listar Productos para comprobar cambios
```

### 3. Agregar Productos al Carro

- **Endpoint:** `/api/carro/productos/`
- **Método HTTP:** `POST`

#### Agregar Producto al Carro

**Solicitud:**

```http
POST /api/carro/productos/
Content-Type: application/json
```

```json
{
    "codigo": 1,
    "cantidad": 5
}
```

**Respuesta:**

```json
{
  "mensaje": "Producto 'Taladro Percutor Bosch' agregado correctamente al carro."
}
```

### 4. Detalle del Carro

- **Endpoint:** `/api/carro/detalle/`
- **Método HTTP:** `GET`

#### Obtener Detalle del Carro

**Solicitud:**

```http
GET /api/carro/detalle/
```

**Respuesta:**

```json
{
  "productos": [
    {
      "nombre": "Taladro Percutor Bosch",
      "precio": 89090,
      "cantidad": 5
    }
  ],
  "total": 445450
}
```

### 5. Eliminar Producto del Carro

- **Endpoint:** `/api/carro/productos/<int:producto_codigo>/`
- **Método HTTP:** `DELETE`

#### Eliminar Producto del Carro

**Solicitud:**

```http
DELETE /api/carro/productos/1/
```

**Respuesta:**

```json
{
  "mensaje": "Producto 'Taladro Percutor Bosch' eliminado correctamente del carro."
}
```

### 6. Pagar y Finalizar el Carro

- **Endpoint:** `/api/carro/finalizar/`
- **Método HTTP:** `POST`

#### Pagar y Finalizar el Carro

**Solicitud:**

```http
POST /api/carro/finalizar/
```

```json
{
  "metodo_pago": "tarjeta de crédito"
}
```
**Respuesta:**

```json
{
  "mensaje": "Carro pagado y pedido finalizado correctamente.",
  "total": 445450,
  "metodo_pago": "tarjeta de crédito",
  "productos": [
    {
      "nombre": "Taladro",
      "precio": 89090,
      "cantidad": 5
    }
  ]
}
```

### Resumen de Endpoints

| Endpoint                                      | Método HTTP | Descripción                 |
| --------------------------------------------- | ----------- | --------------------------- |
| `/api/productos/`                             | `GET`       | Listar productos            |
| `/api/productos/`                             | `POST`      | Crear producto              |
| `/api/productos/<str:codigo>/`                | `GET`       | Detalle de producto         |
| `/api/productos/<str:codigo>/`                | `PUT`       | Actualizar producto         |
| `/api/productos/<str:codigo>/`                | `DELETE`    | Eliminar producto           |
| `/api/carro/productos/`                       | `POST`      | Agregar producto al carro   |
| `/api/carro/detalle/`                         | `GET`       | Obtener detalle del carro   |
| `/api/carro/productos/<int:producto_codigo>/` | `DELETE`    | Eliminar producto del carro |
| `/api/carro/finalizar/`                       | `POST`      | Pagar y finalizar el carro  |

## Notas

- El ID del carro se asume como 1 en todos los casos.
- Los productos eliminados del carro no se pueden recuperar, y el stock se actualiza automáticamente cuando se paga y finaliza el pedido.
- El carro al pagar se elimina por completo y se creara uno nuevo siempre y cuando se agregen productos a este
# 🛍️ RESTful API for sample Product Management System

This is a RESTful API for managing products in an inventory system using **Flask**, **PostgreSQL**, and **SQLAlchemy**. It supports CRUD operations, with input validation and logging.
A RESTful API (Representational State Transfer) is an architectural style for designing networked applications. It uses standard HTTP methods (like GET, POST, PUT, DELETE) to perform operations on resources (usually represented as JSON objects).
---

## 🚀 Setup Instructions

1. **Clone/Extract the Project**

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure PostgreSQL**
   - Create a database named `products`
   - Update credentials in `app/config.py` if needed

4. **Initialize Database**
   ```bash
   python
   >>> from app import db, create_app
   >>> app = create_app()
   >>> with app.app_context():
   ...     db.create_all()
   ```

5. **Run the Server**
   ```bash
   python run.py
   ```

---

## 📬 API Endpoints

### 🔹 POST `/products`
Create a new product.

**Request Body (JSON):**
```json
{
  "name": "MacBook Pro",
  "quantity": 10,
  "price": 1299.99
}
```

✅ **Success Response (201):**
```json
{
  "id": 1,
  "name": "MacBook Pro",
  "quantity": 10,
  "price": 1299.99
}
```

❌ **Error Response (400):**
```json
{
  "error": "Request must be JSON"
}
```

---

### 🔹 GET `/products`
Get all products.

✅ **Success Response (200):**
```json
[
  {
    "id": 1,
    "name": "MacBook Pro",
    "quantity": 10,
    "price": 1299.99
  }
]
```

---

### 🔹 GET `/products/<id>`
Get a product by ID.

✅ **Success (200):**
```json
{
  "id": 1,
  "name": "MacBook Pro",
  "quantity": 10,
  "price": 1299.99
}
```

❌ **Not Found (404):**
```json
{
  "error": "Product not found"
}
```

---

### 🔹 PUT `/products/<id>`
Update a product.

**Request Body (Partial Allowed):**
```json
{
  "price": 1399.99
}
```

✅ **Success (200):**
```json
{
  "id": 1,
  "name": "MacBook Pro",
  "quantity": 10,
  "price": 1399.99
}
```

---

### 🔹 DELETE `/products/<id>`
Delete a product.

✅ **Success (204):** No content

❌ **Not Found (404):**
```json
{
  "error": "Product not found"
}
```

---

## ⚠️ Error Handling

| Error Type             | Code | Message                            |
|------------------------|------|------------------------------------|
| Missing JSON Body      | 400  | `"Request must be JSON"`           |
| Validation Errors      | 400  | Custom field-level validation      |
| Not Found (Product)    | 404  | `"Product not found"`              |
| Server/Internal Error  | 500  | `"Error <description>"`            |

All errors are logged using the built-in `logging` module.

---

## 📦 Tech Stack

- Python + Flask
- PostgreSQL
- SQLAlchemy + Marshmallow
- REST API Design
- Logging and Exception Handling

---

## 📧 Contact

Feel free to reach out if you have any questions or improvements!

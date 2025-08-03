# E-Commerce REST API

A Django REST Framework (DRF) based API for e-commerce product and user management.

## Features Implemented

### User Authentication
- JWT-based authentication (login/refresh)
- User registration endpoint
- Custom user model with:
  - Email/password authentication
  - Date of birth field
  - Profile photo upload capability

### Product Management
- CRUD operations for products:
  - Create new products
  - List all products
  - Retrieve single product details
  - Update existing products
  - Delete products
- Product categories with relationships
- Stock management

### API Endpoints

#### Authentication

| Endpoint                   | Method | Description               |
|----------------------------|--------|---------------------------|
| `/api/auth/register/`      | POST   | Register new user         |
| `/api/auth/login/`         | POST   | Obtain JWT tokens         |
| `/api/auth/token/refresh/` | POST   | Refresh JWT token         |

### Products API Endpoints

| Endpoint               | Method | Description           |
|------------------------|--------|-----------------------|
| `/api/products/`       | GET    | List all products     |
| `/api/products/`       | POST   | Create new product    |
| `/api/products/<id>/`  | GET    | Get product details   |
| `/api/products/<id>/`  | PUT    | Update product        |
| `/api/products/<id>/`  | DELETE | Delete product        |


## Technical Stack
- **Backend**: Django 4.2 + Django REST Framework
- **Database**: SQLite (development), PostgreSQL ready
- **Authentication**: JWT (JSON Web Tokens)
- **File Storage**: Local filesystem (ready for AWS S3 integration)

## Setup Instructions

### Prerequisites
- Python 3.10+
- pip

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ecommerce-api.git
   cd ecommerce-api
   ```

2. **Create and activate virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run migrations:**
```bash
python manage.py migrate
```

5. **Create superuser:**
```bash
python manage.py createsuperuser
```

6. **Run development server:**
```bash
python manage.py runserver
```

### Testing the API
Use tools like Postman or cURL to test endpoints:

**User Registration**
```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com", "password":"mypassword"}'
  ```

**Product Creation (Authenticated)**
```bash
curl -X POST http://127.0.0.1:8000/api/products/ \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name":"Product Name", "price":19.99, "stock":100}'
  ```
# E-Commerce-Backend-ProDev-BE

🛍️ E-Commerce Backend – ProDev BE
📘 Overview

The ProDev BE (E-Commerce Backend) project is designed to simulate a real-world backend environment supporting a modern e-commerce application. It focuses on API development, database optimization, and secure authentication, forming the backbone for the ProDev FE Frontend Catalog
.

This backend handles product management, user authentication, filtering, sorting, and pagination, enabling scalable integration with any e-commerce frontend (web, mobile, or PWA).

🌍 Real-World Application

This case study mirrors real enterprise backend development. By completing it, participants will:

Design and optimize relational database schemas

Build and document RESTful APIs

Implement JWT-based authentication

Optimize performance through query indexing and efficient data access

🎯 Project Goals

CRUD APIs:
Build APIs for managing products, categories, and users (with authentication).

Filtering, Sorting, Pagination:
Implement backend logic for efficient product browsing and discovery.

Database Optimization:
Design a relational schema with proper indexing for high-performance queries.

API Documentation:
Provide clean, interactive API documentation (Swagger/OpenAPI or Postman).

🧰 Technologies Used
Technology	Purpose
Django	High-level Python web framework for backend logic
Django REST Framework (DRF)	API creation and serialization
PostgreSQL	Relational database with robust query support
JWT (JSON Web Token)	Secure user authentication
Swagger / drf-yasg	Interactive API documentation
Gunicorn + Nginx (optional)	Production-grade deployment setup
⚙️ Key Features
1. CRUD Operations

Create, Read, Update, Delete for Products and Categories

Manage User registration, login, and profile updates with JWT-based authentication

2. API Features

Filtering products by category or search keyword

Sorting by price (ascending/descending)

Pagination for large product datasets

3. API Documentation

Auto-generated Swagger UI available at /api/docs/

Optionally publish Postman collection for external testing

🧱 Database Schema (Simplified)

Tables:

User → stores user credentials and profile info

Category → product categories

Product → product details (title, description, price, stock, image, etc.)

ERD Example:

User (id, username, email, password)
Category (id, name, slug)
Product (id, title, description, price, stock, category_id, created_at)

🚀 Getting Started
1. Clone the Repository
git clone https://github.com/Sam-Adk/prodev-be.git
cd prodev-be

2. Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file in the root directory:

SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_NAME=prodevdb
DATABASE_USER=postgres
DATABASE_PASSWORD=yourpassword
DATABASE_HOST=localhost
DATABASE_PORT=5432

5. Apply Migrations
python manage.py makemigrations
python manage.py migrate

6. Run Development Server
python manage.py runserver


Backend will be live at:
👉 http://127.0.0.1:8000/

🔑 API Endpoints
🔐 Authentication
Method	Endpoint	Description
POST	/api/auth/register/	Register a new user
POST	/api/auth/login/	Login and get JWT token
GET	/api/auth/profile/	Retrieve user profile
🛒 Products
Method	Endpoint	Description
GET	/api/products/	List all products (supports filtering, sorting, pagination)
POST	/api/products/	Add new product
GET	/api/products/:id/	Retrieve single product
PUT	/api/products/:id/	Update product
DELETE	/api/products/:id/	Delete product

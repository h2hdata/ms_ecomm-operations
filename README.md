# ms_ecomm-operations
This repository consists of POC created for microservices domain. Problem is to manage operations for a typical ecommerce business.

To enhance the complexity and capability of the FastAPI codebase using SQLAlchemy ORM version 2.0, you can incorporate several advanced features. Here’s an improved version of the codebase with more sophisticated features such as dependency injection for database sessions, pagination, and error handling.
Enhanced Project Structure
myapp/
├── main.py
├── models.py
├── schemas.py
├── crud.py
├── database.py
├── dependencies.py
├── config.py
└── __init__.py

**Improvements Explained**
Dependency Injection:
Using dependency injection for the database session ensures that each endpoint gets a fresh session. This is handled in dependencies.py with the get_db function.
Configuration Management:
Using pydantic.BaseSettings in config.py allows for centralized management of configuration settings, making it easy to switch between different environments.
Error Handling:
Implemented HTTPException in main.py to handle errors gracefully.
Pagination:
The read_items endpoint supports pagination via query parameters skip and limit.

Environment Variables:
The .env file allows easy management of environment variables and is parsed by Pydantic settings.
Dependencies
To use these features, ensure you have the necessary dependencies:
pip install fastapi sqlalchemy sqlalchemy[asyncio] aiosqlite pydantic python-dotenv

**Calling Fastapi app:**
cd Documents
uvicorn ecom3.main:app --reload

Endpoints:
Endpoint 1: Create Items with name and description 
Description: Creates a new user with a POST request to /items/.

curl -X POST "http://localhost:8000/items/" -H "Content-Type: application/json" -d "{\"name\":\"Harry Potter\", \"description\": \"non-fictional and interesting story\"}"
Endpoint 2: Read Items
Description: Retrieves a list of items with a GET request to /items/.

curl -X GET "http://localhost:8000/items/"

-to retrieve first 10 
curl -X GET "http://localhost:8000/items/?skip=0&limit=10"
-to retrieve next ten items
curl -X GET "http://localhost:8000/items/?skip=10&limit=10"

Endpoint 3: Update Item
Endpoint: Update an existing item's information by item ID using a PUT request to /items/{item_id}. we can update name and description

curl -X PUT "http://localhost:8000/items/1" -H "Content-Type: application/json" -d "{\"name\": \"Harry Potter\",\"description\": \"mindblowing story\"}"

Endpoint 4: Delete Item
Endpoint: Delete an existing user by ID using a DELETE request to /items/{item_id}.

curl -X DELETE "http://localhost:8000/items/1"

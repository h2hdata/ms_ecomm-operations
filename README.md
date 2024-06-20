# ms_ecomm-operations
This repository consists of POC created for microservices domain. Problem is to manage operations for a typical ecommerce business.<br><br><br>

To enhance the complexity and capability of the FastAPI codebase using SQLAlchemy ORM version 2.0, you can incorporate several advanced features. Here’s an improved version of the codebase with more sophisticated features such as dependency injection for database sessions, pagination, and error handling.<br><br>
Enhanced Project Structure<br>
myapp/<br>
├── main.py <br>
├── models.py<br>
├── schemas.py<br>
├── crud.py<br>
├── database.py<br>
├── dependencies.py<br>
├── config.py<br>
└── __init__.py<br><br><br>

**Improvements Explained**<br>
Dependency Injection:<br>
Using dependency injection for the database session ensures that each endpoint gets a fresh session. This is handled in dependencies.py with the get_db function.<br>
Configuration Management:<br>
Using pydantic.BaseSettings in config.py allows for centralized management of configuration settings, making it easy to switch between different environments.
Error Handling:<br>
Implemented HTTPException in main.py to handle errors gracefully.<br><br>
Pagination:<br>
The read_items endpoint supports pagination via query parameters skip and limit.<br><br><br>

Environment Variables:<br>
The .env file allows easy management of environment variables and is parsed by Pydantic settings.<br><br>
Dependencies<br>
To use these features, ensure you have the necessary dependencies:<br>
pip install fastapi sqlalchemy sqlalchemy[asyncio] aiosqlite pydantic python-dotenv<br><br>
<br><br><br><br>
**Calling Fastapi app:**<br>
cd Documents<br>
uvicorn ecom3.main:app --reload<br><br>

Endpoints:<br>
Endpoint 1: Create Items with name and description <br>
Description: Creates a new user with a POST request to /items/.<br>

curl -X POST "http://localhost:8000/items/" -H "Content-Type: application/json" -d "{\"name\":\"Harry Potter\", \"description\": \"non-fictional and interesting story\"}"<br><br>
Endpoint 2: Read Items<br>
Description: Retrieves a list of items with a GET request to /items/.<br>

curl -X GET "http://localhost:8000/items/"<br>

-to retrieve first 10 <br>
curl -X GET "http://localhost:8000/items/?skip=0&limit=10"<br>
-to retrieve next ten items<br>
curl -X GET "http://localhost:8000/items/?skip=10&limit=10"<br><br>

Endpoint 3: Update Item<br>
Endpoint: Update an existing item's information by item ID using a PUT request to /items/{item_id}. we can update name and description<br>

curl -X PUT "http://localhost:8000/items/1" -H "Content-Type: application/json" -d "{\"name\": \"Harry Potter\",\"description\": \"mindblowing story\"}"<br>

Endpoint 4: Delete Item<br>
Endpoint: Delete an existing user by ID using a DELETE request to /items/{item_id}.<br>

curl -X DELETE "http://localhost:8000/items/1"<br>

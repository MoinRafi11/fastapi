
# 76 - FastAPI Introduction

## 1. What Is FastAPI?

FastAPI is a modern, high-performance Python web framework used to build APIs and backend applications.

It is designed to make API development fast, simple, and efficient. FastAPI uses Python type hints to validate data, generate API documentation, and provide editor support.

FastAPI is commonly used to build REST APIs, microservices, and backend services that communicate with frontend applications or other systems.

### Key Features

- High performance.
- Built-in request data validation.
- Automatic interactive API documentation.
- Support for asynchronous programming using `async` and `await`.
- Python type hints for defining data structures.
- Automatic generation of OpenAPI schemas.
- Dependency injection for reusable application logic.
- Support for authentication and authorization integrations.

## 2. Why Use FastAPI?

FastAPI simplifies the development of APIs by providing many features out of the box.

Without a framework, developers would need to implement request handling, input validation, routing, and documentation separately.

FastAPI provides these capabilities through a straightforward Python interface.

### Advantages

- Easy to learn if you know Python.
- Automatically validates incoming request data.
- Generates interactive API documentation.
- Supports synchronous and asynchronous endpoints.
- Integrates with databases and external services.
- Suitable for small applications and larger service-based architectures.

### Common Use Cases

- REST API development.
- Backend services for React applications.
- Microservices.
- Machine learning model APIs.
- Cloud application backends.
- Automation services.
- Internal APIs used by DevOps tools.

## 3. FastAPI vs Flask vs Django

Python offers several frameworks for web development. Their purposes overlap, but they have different strengths.

| Feature | FastAPI | Flask | Django |
|---|---|---|---|
| Main purpose | API development | General-purpose web applications and APIs | Full-featured web applications |
| Type validation | Built-in integration with Pydantic | Requires additional libraries or custom logic | Available through forms, serializers, and other tools |
| Automatic API documentation | Built-in OpenAPI documentation | Requires extensions or additional tools | Usually requires additional tools |
| Asynchronous support | Supported | Supported in modern versions, with limitations depending on extensions | Supported in modern versions |
| Built-in ORM | No | No | Yes |
| Learning curve | Relatively easy | Relatively easy | More features to learn |
| Common use | APIs and microservices | Lightweight applications | Full-stack web applications |

**Note:** FastAPI, Flask, and Django can all be used to build APIs. The best choice depends on the application's requirements.

## 4. Installing FastAPI

FastAPI requires Python and an ASGI server to run web applications.

Uvicorn is a commonly used ASGI server for FastAPI.

### Step 1: Check Python Installation

```bash
python --version
```

On some Linux systems, use:

```bash
python3 --version
```

### Step 2: Create a Project Directory

```bash
mkdir fastapi-project
cd fastapi-project
```

### Step 3: Create a Virtual Environment

On Windows:

```powershell
python -m venv venv
```

On Linux:

```bash
python3 -m venv venv
```

### Step 4: Activate the Virtual Environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```cmd
venv\Scripts\activate.bat
```

Linux:

```bash
source venv/bin/activate
```

### Step 5: Install FastAPI and Uvicorn

```bash
pip install "fastapi[standard]"
```

This installation includes FastAPI's standard optional dependencies, including the `fastapi` command-line tooling and Uvicorn.

Alternatively, install the core packages explicitly:

```bash
pip install fastapi uvicorn
```

## 5. Creating Your First FastAPI Application

Create a file named `main.py`.

Add the following code:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}


@app.get("/about")
def about():
    return {"message": "This is my first FastAPI application."}
```

### Understanding the Code

**Import FastAPI**

```python
from fastapi import FastAPI
```

Imports the FastAPI class used to create the application.

**Create the Application**

```python
app = FastAPI()
```

Creates the FastAPI application instance.

**Define a Route**

```python
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}
```

- `@app.get("/")` registers a GET endpoint at the root path.
- `home()` is the Python function executed when the endpoint is requested.
- The returned Python dictionary is serialized into a JSON response.

**Define Another Endpoint**

```python
@app.get("/about")
def about():
    return {"message": "This is my first FastAPI application."}
```

Registers a GET endpoint at `/about`.

## 6. Running the FastAPI Application

Run the following command from the directory containing `main.py`:

```bash
fastapi dev main.py
```

This starts the development server with automatic reload support.

Alternatively, run:

```bash
uvicorn main:app --reload
```

### Understanding the Uvicorn Command

```bash
uvicorn main:app --reload
```

- `uvicorn`: Starts the ASGI server.
- `main`: Refers to the `main.py` Python module.
- `app`: Refers to the FastAPI application instance inside that module.
- `--reload`: Restarts the development server when code changes are detected.

The server typically starts at:

```text
http://127.0.0.1:8000
```

Use this address to access the application locally.

**Important:** `--reload` is intended for development, not production deployment.

## 7. Testing the API

Once the application is running, open a browser or use an API client.

### Root Endpoint

URL:

```text
http://127.0.0.1:8000/
```

Response:

```json
{
  "message": "Welcome to FastAPI!"
}
```

### About Endpoint

URL:

```text
http://127.0.0.1:8000/about
```

Response:

```json
{
  "message": "This is my first FastAPI application."
}
```

You can also test endpoints using `curl`:

```bash
curl http://127.0.0.1:8000/
```

Example response:

```json
{"message":"Welcome to FastAPI!"}
```

## 8. Automatic API Documentation

One of FastAPI's most useful features is automatic API documentation.

When the application is running, open the following URLs in a browser.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

Swagger UI provides an interactive interface where you can inspect endpoints, enter parameters, submit requests, and view responses.

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

ReDoc presents the API documentation in a different layout.

FastAPI generates these documentation pages from the application's routes, request models, response types, and OpenAPI schema.

## 9. Understanding API Routes and HTTP Methods

FastAPI supports common HTTP methods through route decorators.

| Decorator | HTTP Method | Typical Purpose |
|---|---|---|
| `@app.get()` | GET | Retrieve information |
| `@app.post()` | POST | Create a resource or initiate an operation |
| `@app.put()` | PUT | Replace a resource |
| `@app.patch()` | PATCH | Partially update a resource |
| `@app.delete()` | DELETE | Delete a resource |

Example:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
def get_users():
    return {"message": "Retrieve users"}


@app.post("/users")
def create_user():
    return {"message": "Create user"}


@app.put("/users/1")
def update_user():
    return {"message": "Replace user"}


@app.patch("/users/1")
def partial_update_user():
    return {"message": "Partially update user"}


@app.delete("/users/1")
def delete_user():
    return {"message": "Delete user"}
```

These examples demonstrate route registration. They do not implement actual database operations.

## 10. Path Parameters

Path parameters allow clients to pass values through the URL.

Example:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "message": "User retrieved successfully"
    }
```

Request:

```text
http://127.0.0.1:8000/users/10
```

Response:

```json
{
  "user_id": 10,
  "message": "User retrieved successfully"
}
```

In this example:

- `{user_id}` is a path parameter.
- `user_id: int` declares that the parameter should be an integer.
- FastAPI converts valid input and validates its type.
- Invalid values, such as `/users/abc`, produce a validation error response.

## 11. Query Parameters

Query parameters are values passed after a question mark in the URL.

Example:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/products")
def get_products(category: str = "all", limit: int = 10):
    return {
        "category": category,
        "limit": limit
    }
```

Request:

```text
http://127.0.0.1:8000/products?category=electronics&limit=5
```

Response:

```json
{
  "category": "electronics",
  "limit": 5
}
```

In this example:

- `category` is a query parameter with a default value of `"all"`.
- `limit` is a query parameter with a default value of `10`.
- The client can override these defaults by providing query parameters.

Query parameters are commonly used for filtering, sorting, pagination, and search operations.

## 12. Request Body and Pydantic Models

A request body carries data sent by a client, commonly when creating or updating a resource.

FastAPI integrates with Pydantic to validate structured request data.

Example:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    email: str


@app.post("/users")
def create_user(user: User):
    return {
        "message": "User received successfully",
        "user": user
    }
```

Example request body:

```json
{
  "name": "Moin",
  "age": 22,
  "email": "moin@example.com"
}
```

FastAPI validates the incoming data against the `User` model.

If required fields are missing or values cannot be validated against the declared types, FastAPI returns a validation error response.

**Note:** The example returns the received data but does not save it to a database.

## 13. Synchronous vs Asynchronous Endpoints

FastAPI supports both synchronous and asynchronous path operation functions.

### Synchronous Endpoint

```python
@app.get("/sync")
def synchronous_endpoint():
    return {"message": "Synchronous response"}
```

A normal `def` endpoint is suitable for ordinary synchronous logic.

FastAPI runs synchronous path operation functions in a thread pool, helping prevent blocking code from directly blocking the main event loop.

### Asynchronous Endpoint

```python
@app.get("/async")
async def asynchronous_endpoint():
    return {"message": "Asynchronous response"}
```

An `async def` endpoint is useful when working with asynchronous libraries and operations that support `await`.

For example, an asynchronous HTTP client can be used to make non-blocking network requests.

**Important:** Using `async def` does not automatically make blocking operations non-blocking. Synchronous blocking code inside an asynchronous endpoint can still block the event loop.

## 14. FastAPI in a DevOps Environment

FastAPI can be used to create backend services that integrate with infrastructure automation and CI/CD workflows.

Examples include:

- Creating APIs to trigger approved automation jobs.
- Exposing deployment status to dashboards.
- Retrieving health information from services.
- Integrating internal tools with CI/CD pipelines.
- Building lightweight microservices.
- Providing API endpoints for monitoring integrations.

### Example: Health Check Endpoint

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
```

Run the application:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Test the endpoint locally:

```bash
curl http://127.0.0.1:8000/health
```

Expected response:

```json
{
  "status": "healthy"
}
```

The endpoint returns a simple status message. It does not independently verify database availability, external dependencies, or the overall health of the application.

### Containerization

A FastAPI application can be packaged into a Docker image and deployed as a container.

A typical workflow is:

1. Develop the FastAPI application.
2. Install dependencies.
3. Create a Docker image.
4. Test the container locally.
5. Push the image to a container registry.
6. Deploy it to a server or container platform.
7. Monitor application health and logs.

When deploying a container, the application must listen on an interface and port that are accessible through the container's network configuration.

## 15. Common FastAPI Commands

| Command | Purpose |
|---|---|
| `pip install "fastapi[standard]"` | Install FastAPI and standard optional dependencies |
| `fastapi dev main.py` | Start the development server |
| `uvicorn main:app --reload` | Start Uvicorn with automatic reload |
| `uvicorn main:app --host 0.0.0.0 --port 8000` | Listen on all container interfaces on port 8000 |
| `pip freeze` | Display installed Python packages |
| `pip freeze > requirements.txt` | Save installed package versions to a requirements file |
| `pip install -r requirements.txt` | Install packages listed in a requirements file |

## 16. Common Issues and Troubleshooting

### ModuleNotFoundError

**Possible cause:** FastAPI is not installed in the active Python environment.

Check the installation:

```bash
python -m pip show fastapi
```

Install the required packages if necessary:

```bash
python -m pip install "fastapi[standard]"
```

### Command Not Found: uvicorn

**Possible cause:** Uvicorn is not installed in the active environment or the environment is not activated.

Try:

```bash
python -m pip install uvicorn
python -m uvicorn main:app --reload
```

### Address Already in Use

**Possible cause:** Another process is already listening on port 8000.

Choose another port:

```bash
uvicorn main:app --reload --port 8001
```

### Application Cannot Be Accessed from Another Machine

**Possible cause:** The application is listening only on the loopback interface, or network rules are blocking access.

For a development or appropriately secured test environment, run:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Also verify firewall rules, network connectivity, and any container port mappings.

Binding to `0.0.0.0` makes the service listen on all available IPv4 interfaces. It does not by itself make the application publicly accessible.

### 404 Not Found

**Possible cause:** The requested route is not registered at that path.

Check the endpoint URL and inspect the available routes at:

```text
http://127.0.0.1:8000/docs
```

### 422 Unprocessable Content

**Possible cause:** The request does not satisfy the endpoint's expected parameters or request body schema.

Check the required fields, data types, path parameters, query parameters, and JSON structure.

## 17. Best Practices

- Use a virtual environment for each Python project.
- Keep dependencies documented in a requirements file or another dependency-management configuration.
- Use Pydantic models to validate structured request data.
- Organize larger applications into separate modules and routers.
- Handle exceptions and return appropriate HTTP status codes.
- Store secrets in environment variables or a suitable secret-management system.
- Never expose sensitive information in API responses or logs.
- Use authentication and authorization for protected endpoints.
- Add tests for important routes and application behavior.
- Use `--reload` only for development.
- Configure HTTPS, process management, logging, and monitoring appropriately for production.
- Avoid exposing administrative or automation endpoints without strong access controls.

## 18. Summary

FastAPI is a modern Python framework for building APIs and backend services.

Key concepts covered in this introduction:

- Installing FastAPI and Uvicorn.
- Creating a basic application.
- Running the development server.
- Testing API endpoints.
- Using automatic Swagger UI and ReDoc documentation.
- Working with HTTP methods, path parameters, and query parameters.
- Validating request bodies with Pydantic.
- Understanding synchronous and asynchronous endpoints.
- Using FastAPI in DevOps and containerized environments.

FastAPI provides a convenient foundation for developing Python-based APIs that can be tested locally, integrated with other services, and deployed through CI/CD workflows.

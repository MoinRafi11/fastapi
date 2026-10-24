
# 77 - FastAPI Hello World

## 1. Introduction

FastAPI is a Python framework used to build APIs and backend applications. In this guide, we will create a simple Hello World API, run it locally, and test it using a browser, Swagger UI, and `curl`.

By the end of this guide, you will know how to:

- Set up a FastAPI project.
- Create your first API endpoint.
- Run the FastAPI development server.
- Return JSON responses.
- Test API endpoints.
- Understand basic FastAPI project structure.

## 2. Prerequisites

Before starting, make sure you have:

- Python installed on your system.
- VS Code or another code editor.
- Basic knowledge of Python.
- Basic understanding of HTTP requests and responses.

Check your Python installation:

```bash
python --version
```

On Linux, you may need:

```bash
python3 --version
```

## 3. Create the Project Directory

Create a directory for the project and navigate into it.

```bash
mkdir fastapi-hello-world
cd fastapi-hello-world
```

Open the directory in VS Code:

```bash
code .
```

Your project will contain a Python application file and a virtual environment.

## 4. Create a Virtual Environment

A virtual environment keeps project dependencies separate from other Python projects.

### Windows

```powershell
python -m venv venv
```

Activate it using PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If you use Command Prompt:

```cmd
venv\Scripts\activate.bat
```

### Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

After activation, your terminal usually displays the environment name, such as `(venv)`.

## 5. Install FastAPI

Install FastAPI and its standard optional dependencies:

```bash
python -m pip install "fastapi[standard]"
```

This provides FastAPI and the standard tooling needed to run the application locally.

Verify the installation:

```bash
python -m pip show fastapi
```

## 6. Create the Hello World Application

Create a file named `main.py` in the project directory.

Add the following code:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}
```

### Understanding the Code

**Import FastAPI**

```python
from fastapi import FastAPI
```

Imports the `FastAPI` class from the framework.

**Create the Application**

```python
app = FastAPI()
```

Creates the application instance that the server will run.

**Define the Endpoint**

```python
@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}
```

- `@app.get("/")` registers a GET endpoint at the root URL.
- `hello_world()` is the function executed when the endpoint is requested.
- The returned dictionary is automatically converted into a JSON response.

## 7. Run the FastAPI Application

Make sure your terminal is in the project directory and your virtual environment is activated.

Run:

```bash
fastapi dev main.py
```

FastAPI starts the development server, typically at:

```text
http://127.0.0.1:8000
```

Alternatively, you can start the application using Uvicorn:

```bash
uvicorn main:app --reload
```

### Understanding the Uvicorn Command

- `uvicorn` starts the ASGI server.
- `main` refers to the `main.py` module.
- `app` refers to the FastAPI instance inside `main.py`.
- `--reload` automatically restarts the server when code changes are detected.

Use `--reload` during development, not as a production deployment setting.

## 8. Test the API in a Browser

Open the following URL:

```text
http://127.0.0.1:8000/
```

Expected response:

```json
{
  "message": "Hello, World!"
}
```

Congratulations! Your first FastAPI endpoint is running.

The response is JSON rather than a traditional HTML webpage because the endpoint returns a Python dictionary.

## 9. Test the API Using Swagger UI

FastAPI automatically generates interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

Follow these steps:

1. Locate the `GET /` endpoint.
2. Expand the endpoint.
3. Click **Try it out**.
4. Click **Execute**.
5. Inspect the response body and HTTP status code.

You should see the message:

```json
{
  "message": "Hello, World!"
}
```

A successful request normally returns the HTTP status code `200 OK`.

## 10. Test the API Using curl

You can also send an HTTP request from your terminal.

```bash
curl http://127.0.0.1:8000/
```

Expected output:

```json
{"message":"Hello, World!"}
```

To display the HTTP response headers along with the response body, use:

```bash
curl -i http://127.0.0.1:8000/
```

The response should include a status line similar to:

```text
HTTP/1.1 200 OK
content-type: application/json
```

The exact HTTP version and other headers may vary.

## 11. Add Another Endpoint

Let's add a second endpoint to the same application.

Update `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}


@app.get("/about")
def about():
    return {"message": "Welcome to my FastAPI application!"}
```

Save the file.

If you started the server with `--reload`, it should detect the change automatically.

Open:

```text
http://127.0.0.1:8000/about
```

Expected response:

```json
{
  "message": "Welcome to my FastAPI application!"
}
```

You now have two GET endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Returns the Hello World message |
| GET | `/about` | Returns information about the application |

## 12. Project Structure

Your project directory should look like this:

```text
fastapi-hello-world/
├── venv/
└── main.py
```

The `venv/` directory contains the isolated Python environment and installed dependencies.

The `main.py` file contains the FastAPI application and its endpoints.

**Note:** The virtual environment should generally not be committed to Git. Add it to `.gitignore` if you are tracking the project with Git.

Example `.gitignore`:

```gitignore
venv/
__pycache__/
*.py[cod]
.env
```

## 13. Common Errors and Solutions

### Error: `ModuleNotFoundError: No module named 'fastapi'`

**Cause:** FastAPI is not installed in the active Python environment.

**Solution:**

```bash
python -m pip install "fastapi[standard]"
```

Make sure the correct virtual environment is activated.

### Error: `fastapi` Command Not Found

**Cause:** The command-line tool may not be available in the active environment.

**Solution:**

```bash
python -m pip install "fastapi[standard]"
python -m uvicorn main:app --reload
```

### Error: Address Already in Use

**Cause:** Another process is already using port `8000`.

**Solution:** Start the application on another port.

```bash
uvicorn main:app --reload --port 8001
```

Then open:

```text
http://127.0.0.1:8001/
```

### Error: 404 Not Found

**Cause:** The requested endpoint does not exist or the URL is incorrect.

**Solution:** Check the URL and inspect the available endpoints at:

```text
http://127.0.0.1:8000/docs
```

### Error: Cannot Access the API from Another Machine

**Cause:** The application may be listening only on the loopback interface.

For a suitable development or testing environment, run:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Also verify firewall rules, network connectivity, and any container port mappings.

Binding to `0.0.0.0` allows the server to listen on all available IPv4 interfaces, but it does not automatically make the API accessible over the internet.

## 14. Stop the Application

To stop the development server, return to the terminal where it is running and press:

```text
CTRL + C
```

Deactivate the virtual environment when you finish working:

```bash
deactivate
```

## 15. Summary

In this guide, we created and tested a basic FastAPI application.

We learned how to:

- Create a project directory.
- Set up a Python virtual environment.
- Install FastAPI.
- Create a `main.py` application.
- Define GET endpoints.
- Run the development server.
- Test endpoints using a browser, Swagger UI, and `curl`.
- Troubleshoot common errors.

The Hello World application provides a simple starting point for developing more advanced APIs using FastAPI.

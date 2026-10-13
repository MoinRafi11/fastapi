from fastapi import FastAPI
from fastapi.responses import FileResponse

#Create an Application Instance
app = FastAPI()

#App decorator for HTTP GET request at ROOT URL "/"
@app.get("/")
def read_root():
    return {"message": "Hello-World"}

@app.get("/new-home")
def read_root():
    return FileResponse("index.html")

@app.get("/users")
def read_root():
    return {"message": "This is user page"}

@app.get("/contact")
def read_root():
    return FileResponse("contact.html")
    

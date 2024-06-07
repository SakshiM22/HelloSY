from fastapi import Union
from fastapi import FastAPI
app = FastAPI()

@app.get("Home")
def read_root():
    return {"Hello": "World"}


@app.get("/About")
def about():
    return{"msg":"About us"}

@app.get("Contact-Us")

@app.get("/login")
def login(username: str, password: str):
    if username =="steel" and password == "abcd1234":
        return {"data": "This is a login page"}
    else:
        return {"data": Login failed incorrect username or password}


@app.post("/login")
def login_post(request:Request):
    print(request.headers)
    print(request.body)




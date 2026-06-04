from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hola_mundo():
    return {"message": "Hola David"}

@app.get("/")
def root():
    return {"message": "Bienvenido a mi API"}
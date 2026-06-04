from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hola_mundo():
    return {"message": "Hola David"}

@app.get("/")
def root():
    return {"message": "Bienvenido a mi API"}

@app.get("/suma")
def sumar(a:int, b:int):
    return {"resultado": f"{a} + {b} = {a+b}"}


@app.get("/resta")
def restar(a:int, b:int):
    return {"resultado": f"{a} - {b} = {a-b}"}


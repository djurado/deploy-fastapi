from fastapi import FastAPI
from config import settings
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

@app.get("/clave_secreta")
def obtener_clave():
    return {"clave": f"{settings.clave_secreta.get_secret_value()}"}

@app.get("/titulo_api")
def obtener_titulo():
    return {"titulo": f"{settings.title_api}"}


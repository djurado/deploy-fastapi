from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_hello_status_code():
    response = client.get('/hello')
    assert response.status_code == 200

def test_sumar_numeros_positivos():
    a = 1
    b = 2
    response = client.get(f'/suma?a={a}&b={b}')
    assert response.json() == {"resultado": f"{a} + {b} = {a+b}"}

# def suma(a:int, b:int):
#     resultado = a + b
#     return resultado

# def test_sumar_dos_numeros_positivos():
#     a = 4
#     b = 6
#     resultado = a+b
#     assert resultado == 10


# def test_sumar_dos_numeros_con_nulo():
#     a = 0
#     b = 6
#     resultado = a+b
#     assert resultado == None

    
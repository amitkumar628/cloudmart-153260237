from fastapi import FastAPI
from .database import get_products, get_cart

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/products")
def products():
    return get_products()

@app.get("/cart")
def cart():
    return get_cart()

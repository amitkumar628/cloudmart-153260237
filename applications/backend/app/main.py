from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import products_container, cart_container, orders_container
from .models import Product, CartItem, Order

app = FastAPI()

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

# ---------------- PRODUCTS ----------------
@app.get("/products")
def get_products():
    items = list(products_container.read_all_items())
    return items

@app.get("/categories")
def get_categories():
    items = list(products_container.read_all_items())
    categories = sorted(list({p["category"] for p in items}))
    return {"categories": categories}

# ---------------- CART ----------------
@app.get("/cart")
def get_cart():
    items = list(cart_container.read_all_items())
    return items

@app.post("/cart")
def add_to_cart(item: CartItem):
    cart_container.upsert_item(item.dict())
    return {"message": "Added to cart"}

@app.delete("/cart/{item_id}")
def remove_cart_item(item_id: str):
    cart_container.delete_item(item_id, partition_key=item_id)
    return {"message": "Removed"}

# ---------------- ORDERS ----------------
@app.post("/orders")
def create_order(order: Order):
    orders_container.upsert_item(order.dict())
    return {"message": "Order placed", "order_id": order.id}

@app.get("/orders")
def get_orders():
    items = list(orders_container.read_all_items())
    return items

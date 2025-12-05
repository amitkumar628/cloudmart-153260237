from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import get_client

app = FastAPI()

# ---------------------------------------------------
# ENABLE CORS — REQUIRED FOR FRONTEND (127.0.0.1:5500)
# ---------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # allow requests from your local frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------
# HEALTH CHECK
# ---------------------------------------------------
@app.get("/health")
def health_check():
    return {"status": "ok"}

# ---------------------------------------------------
# GET PRODUCTS
# ---------------------------------------------------
@app.get("/products")
def get_products():
    client = get_client()
    database = client.get_database_client("cloudmartdb")
    container = database.get_container_client("products")

    items = list(container.read_all_items())
    return items

# ---------------------------------------------------
# GET CART
# ---------------------------------------------------
@app.get("/cart")
def get_cart():
    client = get_client()
    database = client.get_database_client("cloudmartdb")
    container = database.get_container_client("cart")

    items = list(container.read_all_items())
    return items

# ---------------------------------------------------
# ADD TO CART  (THIS IS REQUIRED FOR FRONTEND BUTTON)
# ---------------------------------------------------
@app.post("/cart/{product_id}")
def add_to_cart(product_id: str):
    client = get_client()
    database = client.get_database_client("cloudmartdb")
    container = database.get_container_client("cart")

    item = {
        "id": product_id,
        "productId": product_id
    }

    container.create_item(item)
    return {"message": "added", "productId": product_id}

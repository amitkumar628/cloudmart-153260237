from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from azure.cosmos import CosmosClient
import os
import uuid

app = FastAPI()

# -----------------------------
# Cosmos DB Credentials
# -----------------------------
COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT")
COSMOS_KEY = os.getenv("COSMOS_KEY")

if not COSMOS_ENDPOINT or not COSMOS_KEY:
    raise Exception("Cosmos DB credentials not found. Set COSMOS_ENDPOINT and COSMOS_KEY.")

client = CosmosClient(COSMOS_ENDPOINT, credential=COSMOS_KEY)
database = client.get_database_client("cloudmart")

products = database.get_container_client("products")
cart = database.get_container_client("cart")
orders = database.get_container_client("orders")


# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
def health_check():
    try:
        list(products.read_all_items(max_item_count=1))
        return {"status": "healthy", "db_status": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "db_status": str(e)}


# -----------------------------
# Products Endpoints
# -----------------------------
@app.get("/api/v1/products")
def get_products(category: str = None):
    query = "SELECT * FROM c"
    items = list(products.query_items(query=query, enable_cross_partition_query=True))

    if category:
        items = [p for p in items if p.get("category") == category]

    return items


# -----------------------------
# Cart Endpoints
# -----------------------------
@app.get("/api/v1/cart")
def get_cart(user_id: str = "demo-user"):
    query = f"SELECT * FROM c WHERE c.user_id = '{user_id}'"
    items = list(cart.query_items(query=query, enable_cross_partition_query=True))
    return items


@app.post("/api/v1/cart")
def add_to_cart(item: dict, user_id: str = "demo-user"):
    item["id"] = str(uuid.uuid4())
    item["user_id"] = user_id

    cart.create_item(item)
    return {"message": "Item added to cart", "item": item}


# -----------------------------
# Orders Endpoints
# -----------------------------
@app.post("/api/v1/orders")
def place_order(order: dict, user_id: str = "demo-user"):
    order["id"] = str(uuid.uuid4())
    order["user_id"] = user_id

    orders.create_item(order)
    return {"message": "Order placed successfully", "order": order}


@app.get("/api/v1/orders")
def get_orders(user_id: str = "demo-user"):
    query = f"SELECT * FROM c WHERE c.user_id = '{user_id}'"
    items = list(orders.query_items(query=query, enable_cross_partition_query=True))
    return items

import os
from azure.cosmos import CosmosClient, PartitionKey

COSMOS_URL = os.getenv("COSMOS_URL")
COSMOS_KEY = os.getenv("COSMOS_KEY")
DATABASE_NAME = "cloudmartdb"

client = CosmosClient(COSMOS_URL, credential=COSMOS_KEY)
database = client.create_database_if_not_exists(id=DATABASE_NAME)

# Products container
products_container = database.create_container_if_not_exists(
    id="products",
    partition_key=PartitionKey(path="/category"),
)

# Cart container
cart_container = database.create_container_if_not_exists(
    id="cart",
    partition_key=PartitionKey(path="/id"),
)

# Orders container
orders_container = database.create_container_if_not_exists(
    id="orders",
    partition_key=PartitionKey(path="/id"),
)

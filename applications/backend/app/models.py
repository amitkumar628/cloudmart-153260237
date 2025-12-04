from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    id: str
    name: str
    category: str
    price: float
    image: Optional[str] = None

class CartItem(BaseModel):
    id: str
    product_id: str
    quantity: int

class Order(BaseModel):
    id: str
    items: List[CartItem]
    total: float

from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float

class CartItem(BaseModel):
    id: int
    name: str
    qty: int

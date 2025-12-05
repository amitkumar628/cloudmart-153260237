# Placeholder mock database until real Cosmos added.

def get_products():
    return [
        {"id": 1, "name": "Laptop", "price": 1200},
        {"id": 2, "name": "Phone", "price": 800}
    ]

def get_cart():
    return {
        "items": [
            {"id": 1, "name": "Laptop", "qty": 1}
        ],
        "total": 1200
    }

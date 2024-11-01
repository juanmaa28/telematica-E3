from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo de datos para los productos
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    in_stock: bool

# Base de datos simulada
products_db = []

# Endpoint para obtener todos los productos
@app.get("/products/", response_model=List[Product])
async def get_products():
    return products_db

# Endpoint para obtener un producto por ID
@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    for product in products_db:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

# Endpoint para crear un nuevo producto
@app.post("/products/", response_model=Product)
async def create_product(product: Product):
    products_db.append(product)
    return product

# Endpoint para actualizar un producto
@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, updated_product: Product):
    for idx, product in enumerate(products_db):
        if product.id == product_id:
            products_db[idx] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")

# Endpoint para eliminar un producto
@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    for idx, product in enumerate(products_db):
        if product.id == product_id:
            del products_db[idx]
            return {"message": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")

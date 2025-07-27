from demo.database.core import SqlProductRepository
from demo.product.core import ProductService
from fastapi import FastAPI

repo = SqlProductRepository()
svc = ProductService(repo)

app = FastAPI()

from collections.abc import AsyncGenerator
from decimal import Decimal
from typing import Protocol
from uuid import UUID

from pydantic import BaseModel


class Product(BaseModel):
    id: UUID
    name: str
    price: Decimal
    quantity: int


class ProductRepository(Protocol):
    async def get_all_products_in_stock(self) -> AsyncGenerator[Product]: ...
    async def get_by_id(self, product_id: UUID) -> Product | None: ...


class ProductService:
    def __init__(self, repository: ProductRepository) -> None:
        self._repo = repository

    async def get_listings(self) -> AsyncGenerator[Product]:
        async for product in await self._repo.get_all_products_in_stock():
            yield product

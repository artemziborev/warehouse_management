from dataclasses import dataclass, field
from typing import List

from domain.entities.product import Product
from domain.exceptions import WarehouseCellFullException


@dataclass
class WarehouseCell:
    id: int | None
    code: str
    capacity: int
    products: List[Product] = field(default_factory=list)

    def add_product(self, product: Product):
        if len(self.products) >= self.capacity:
            raise WarehouseCellFullException(self.id)
        self.products.append(product)

    def remove_product(self, product_id: int):
        self.products = [p for p in self.products if p.id != product_id]

    def count_products(self) -> int:
        return len(self.products)

    def is_full(self) -> bool:
        return len(self.products) >= self.capacity

    def __repr__(self):
        return f"<WarehouseCell(id={self.id}, code={self.code}, capacity={self.capacity}, products={len(self.products)})>"

from dataclasses import dataclass, field
from typing import List

from domain.entities.product import Product


@dataclass
class Order:
    id: int | None
    products: List[Product] = field(default_factory=list)

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product_id: int):
        self.products = [p for p in self.products if p.id != product_id]

    def total_price(self) -> float:
        return sum(p.price.value for p in self.products)

    def total_quantity(self) -> int:
        return sum(p.quantity.value for p in self.products)

    def is_empty(self) -> bool:
        return len(self.products) == 0

    def __repr__(self):
        return f"<Order(id={self.id}, total_price={self.total_price()}, total_quantity={self.total_quantity()})>"

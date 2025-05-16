from dataclasses import dataclass

from domain.entities.value_objects import Price, Quantity


@dataclass
class Product:
    id: int | None
    name: str
    description: str
    unit: str
    price: Price
    quantity: Quantity

    def change_quantity(self, new_quantity: int):
        self.quantity = Quantity(new_quantity)

    def change_price(self, new_price: float):
        self.price = Price(new_price)

    def is_available(self) -> bool:
        return self.quantity.value > 0

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, price={self.price.value}, quantity={self.quantity.value})>"

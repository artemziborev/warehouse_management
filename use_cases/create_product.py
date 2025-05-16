from domain.entities.product import Product
from domain.entities.value_objects import Price, Quantity
from domain.unit_of_work import UnitOfWork


class CreateProductUseCase:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def execute(
        self, name: str, description: str, unit: str, price: float, quantity: int
    ) -> Product:
        product = Product(
            id=None,
            name=name,
            description=description,
            unit=unit,
            price=Price(price),
            quantity=Quantity(quantity),
        )

        with self.uow:
            self.uow.products.add(product)
            self.uow.commit()

        return product

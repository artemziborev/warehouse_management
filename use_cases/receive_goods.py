from domain.exceptions import EntityNotFoundException
from domain.unit_of_work import UnitOfWork


class ReceiveGoodsUseCase:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def execute(self, product_id: int, additional_quantity: int):
        with self.uow:
            product = self.uow.products.get(product_id)
            if not product:
                raise EntityNotFoundException("Product", product_id)

            new_quantity = product.quantity.value + additional_quantity
            product.change_quantity(new_quantity)

            self.uow.products.add(product)
            self.uow.commit()

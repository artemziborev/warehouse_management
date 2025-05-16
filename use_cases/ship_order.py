from domain.exceptions import EntityNotFoundException, InsufficientStockException
from domain.unit_of_work import UnitOfWork


class ShipOrderUseCase:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def execute(self, order_id: int):
        with self.uow:
            order = self.uow.orders.get(order_id)
            if not order:
                raise EntityNotFoundException("Order", order_id)

            for product in order.products:
                if product.quantity.value <= 0:
                    raise InsufficientStockException(product.id, product.quantity.value)

                product.change_quantity(product.quantity.value - 1)
                self.uow.products.add(product)

            self.uow.orders.remove(order_id)

            self.uow.commit()

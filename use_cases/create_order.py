from domain.entities.order import Order
from domain.exceptions import EntityNotFoundException
from domain.unit_of_work import UnitOfWork


class CreateOrderUseCase:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def execute(self, product_ids: list[int]) -> Order:
        with self.uow:
            products = []
            for product_id in product_ids:
                product = self.uow.products.get(product_id)
                if not product:
                    raise EntityNotFoundException("Product", product_id)
                products.append(product)

            order = Order(id=None, products=products)
            self.uow.orders.add(order)
            self.uow.commit()

        return order

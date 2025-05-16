from domain.unit_of_work import UnitOfWork


class InventoryManagementUseCase:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def execute(self):
        with self.uow:
            products = self.uow.products.list()
            self.uow.commit()
            return products

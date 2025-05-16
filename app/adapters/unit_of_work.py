from sqlalchemy.orm import Session

from app.adapters.repositories.order_repository import SqlAlchemyOrderRepository
from app.adapters.repositories.product_repository import SqlAlchemyProductRepository
from app.adapters.repositories.warehouse_cell_repository import (
    SqlAlchemyWarehouseCellRepository,
)
from domain.repositories.interfaces.order_repository import OrderRepository
from domain.repositories.interfaces.product_repository import ProductRepository
from domain.repositories.interfaces.warehouse_cell_repository import (
    WarehouseCellRepository,
)
from domain.unit_of_work import UnitOfWork


class SqlAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session: Session):
        self._session = session
        self._products = SqlAlchemyProductRepository(self._session)
        self._orders = SqlAlchemyOrderRepository(self._session)
        self._warehouse_cells = SqlAlchemyWarehouseCellRepository(self._session)

    @property
    def products(self) -> ProductRepository:
        return self._products

    @property
    def orders(self) -> OrderRepository:
        return self._orders

    @property
    def warehouse_cells(self) -> WarehouseCellRepository:
        return self._warehouse_cells

    def commit(self):
        self._session.commit()

    def rollback(self):
        self._session.rollback()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.rollback()
        else:
            self.commit()

from abc import ABC, abstractmethod

from domain.repositories.interfaces.order_repository import OrderRepository
from domain.repositories.interfaces.product_repository import ProductRepository
from domain.repositories.interfaces.warehouse_cell_repository import (
    WarehouseCellRepository,
)


class UnitOfWork(ABC):
    @property
    @abstractmethod
    def products(self) -> ProductRepository:
        pass

    @property
    @abstractmethod
    def orders(self) -> OrderRepository:
        pass

    @property
    @abstractmethod
    def warehouse_cells(self) -> WarehouseCellRepository:
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        pass

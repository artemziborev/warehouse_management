from typing import List, Optional

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from domain.entities.warehouse_cell import WarehouseCell
from domain.repositories.interfaces.warehouse_cell_repository import (
    WarehouseCellRepository,
)
from framework_drivers.orm.warehouse_cell_orm import WarehouseCellORM


class SqlAlchemyWarehouseCellRepository(WarehouseCellRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, cell: WarehouseCell) -> None:
        cell_orm = WarehouseCellORM(code=cell.code, capacity=cell.capacity)
        self.session.add(cell_orm)
        self.session.flush()
        cell.id = cell_orm.id

    def get(self, cell_id: int) -> Optional[WarehouseCell]:
        try:
            cell_orm = self.session.query(WarehouseCellORM).filter_by(id=cell_id).one()
            return WarehouseCell(
                id=cell_orm.id, code=cell_orm.code, capacity=cell_orm.capacity
            )
        except NoResultFound:
            return None

    def list(self) -> List[WarehouseCell]:
        return [
            WarehouseCell(id=c.id, code=c.code, capacity=c.capacity)
            for c in self.session.query(WarehouseCellORM).all()
        ]

    def remove(self, cell_id: int) -> None:
        self.session.query(WarehouseCellORM).filter_by(id=cell_id).delete()
        self.session.flush()

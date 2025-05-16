from app.adapters.repositories.warehouse_cell_repository import (
    SqlAlchemyWarehouseCellRepository,
)
from domain.entities.warehouse_cell import WarehouseCell


def test_add_and_get_cell(session):
    cell_repo = SqlAlchemyWarehouseCellRepository(session)

    cell = WarehouseCell(id=None, code="A1", capacity=10)
    cell_repo.add(cell)

    retrieved = cell_repo.get(cell.id)
    assert retrieved is not None
    assert retrieved.code == "A1"
    assert retrieved.capacity == 10


def test_list_cells(session):
    cell_repo = SqlAlchemyWarehouseCellRepository(session)

    cell1 = WarehouseCell(id=None, code="A1", capacity=10)
    cell2 = WarehouseCell(id=None, code="B1", capacity=20)
    cell_repo.add(cell1)
    cell_repo.add(cell2)

    cells = cell_repo.list()
    assert len(cells) == 2
    assert cells[0].code == "A1"
    assert cells[1].code == "B1"


def test_remove_cell(session):
    cell_repo = SqlAlchemyWarehouseCellRepository(session)

    cell = WarehouseCell(id=None, code="A1", capacity=10)
    cell_repo.add(cell)

    cell_repo.remove(cell.id)

    assert cell_repo.get(cell.id) is None

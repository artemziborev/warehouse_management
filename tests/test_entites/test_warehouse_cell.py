import pytest

from domain.entities.product import Product
from domain.entities.value_objects import Price, Quantity
from domain.entities.warehouse_cell import WarehouseCell
from domain.exceptions import WarehouseCellFullException


def test_create_warehouse_cell():
    cell = WarehouseCell(id=None, code="A1", capacity=10)
    assert cell.id is None
    assert cell.code == "A1"
    assert cell.capacity == 10
    assert len(cell.products) == 0


def test_add_product_to_cell():
    cell = WarehouseCell(id=None, code="A1", capacity=2)
    product = Product(
        id=1,
        name="Laptop",
        description="High performance laptop",
        unit="pcs",
        price=Price(1500.0),
        quantity=Quantity(10),
    )

    cell.add_product(product)

    assert len(cell.products) == 1
    assert cell.products[0].name == "Laptop"


def test_add_product_to_full_cell():
    cell = WarehouseCell(id=None, code="A1", capacity=1)
    product1 = Product(
        id=1,
        name="Laptop",
        description="High performance laptop",
        unit="pcs",
        price=Price(1500.0),
        quantity=Quantity(10),
    )
    product2 = Product(
        id=2,
        name="Phone",
        description="Smartphone",
        unit="pcs",
        price=Price(500.0),
        quantity=Quantity(5),
    )

    cell.add_product(product1)

    with pytest.raises(WarehouseCellFullException):
        cell.add_product(product2)


def test_remove_product_from_cell():
    cell = WarehouseCell(id=None, code="A1", capacity=2)
    product1 = Product(
        id=1,
        name="Laptop",
        description="High performance laptop",
        unit="pcs",
        price=Price(1500.0),
        quantity=Quantity(10),
    )
    product2 = Product(
        id=2,
        name="Phone",
        description="Smartphone",
        unit="pcs",
        price=Price(500.0),
        quantity=Quantity(5),
    )

    cell.add_product(product1)
    cell.add_product(product2)

    cell.remove_product(product1.id)

    assert len(cell.products) == 1
    assert cell.products[0].name == "Phone"


def test_count_products():
    cell = WarehouseCell(id=None, code="A1", capacity=5)
    product1 = Product(
        id=1,
        name="Laptop",
        description="High performance laptop",
        unit="pcs",
        price=Price(1500.0),
        quantity=Quantity(10),
    )
    product2 = Product(
        id=2,
        name="Phone",
        description="Smartphone",
        unit="pcs",
        price=Price(500.0),
        quantity=Quantity(5),
    )

    cell.add_product(product1)
    cell.add_product(product2)

    assert cell.count_products() == 2


def test_is_full():
    cell = WarehouseCell(id=None, code="A1", capacity=1)
    product = Product(
        id=1,
        name="Laptop",
        description="High performance laptop",
        unit="pcs",
        price=Price(1500.0),
        quantity=Quantity(10),
    )

    cell.add_product(product)

    assert cell.is_full()

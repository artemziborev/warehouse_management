from domain.entities.product import Product
from domain.entities.value_objects import Price, Quantity
from use_cases.inventory_management import InventoryManagementUseCase


def test_inventory_management(uow):
    product1 = Product(
        id=None,
        name="Laptop",
        description="High performance laptop",
        unit="pcs",
        price=Price(1500.0),
        quantity=Quantity(10),
    )
    product2 = Product(
        id=None,
        name="Phone",
        description="Smartphone",
        unit="pcs",
        price=Price(500.0),
        quantity=Quantity(5),
    )

    with uow:
        uow.products.add(product1)
        uow.products.add(product2)
        uow.commit()

    use_case = InventoryManagementUseCase(uow)
    products = use_case.execute()

    assert len(products) == 2
    assert products[0].name == "Laptop"
    assert products[1].name == "Phone"


def test_empty_inventory(uow):
    use_case = InventoryManagementUseCase(uow)
    products = use_case.execute()
    assert len(products) == 0

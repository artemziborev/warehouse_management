import pytest

from domain.entities.order import Order
from domain.entities.product import Product
from domain.entities.value_objects import Price, Quantity
from domain.exceptions import EntityNotFoundException, InsufficientStockException
from use_cases.ship_order import ShipOrderUseCase


def test_ship_order(uow):
    product = Product(
        id=None,
        name="Laptop",
        description="High performance laptop",
        unit="pcs",
        price=Price(1500.0),
        quantity=Quantity(10),
    )
    with uow:
        uow.products.add(product)
        order = Order(id=None, products=[product])
        uow.orders.add(order)
        uow.commit()

    use_case = ShipOrderUseCase(uow)
    use_case.execute(order.id)

    with uow:
        assert uow.orders.get(order.id) is None
        updated_product = uow.products.get(product.id)
        assert updated_product.quantity.value == 9


def test_ship_order_with_nonexistent_order(uow):
    use_case = ShipOrderUseCase(uow)

    with pytest.raises(EntityNotFoundException, match="Order with ID 999 not found"):
        use_case.execute(999)


def test_ship_order_with_insufficient_stock(uow):
    product = Product(
        id=None,
        name="Laptop",
        description="High performance laptop",
        unit="pcs",
        price=Price(1500.0),
        quantity=Quantity(0),
    )
    with uow:
        uow.products.add(product)
        order = Order(id=None, products=[product])
        uow.orders.add(order)
        uow.commit()

    use_case = ShipOrderUseCase(uow)
    with pytest.raises(
        InsufficientStockException, match="Product with ID .+ has only 0 items in stock"
    ):
        use_case.execute(order.id)

from app.adapters.repositories.order_repository import SqlAlchemyOrderRepository
from app.adapters.repositories.product_repository import SqlAlchemyProductRepository
from domain.entities.order import Order
from domain.entities.product import Product
from domain.entities.value_objects import Price, Quantity


def test_add_and_get_order(session):
    product_repo = SqlAlchemyProductRepository(session)
    order_repo = SqlAlchemyOrderRepository(session)

    product = Product(
        id=None,
        name="Laptop",
        description="High performance laptop",
        unit="pcs",
        price=Price(1500.0),
        quantity=Quantity(10),
    )
    product_repo.add(product)

    order = Order(id=None, products=[product])
    order_repo.add(order)

    retrieved = order_repo.get(order.id)
    assert retrieved is not None
    assert len(retrieved.products) == 1
    assert retrieved.products[0].name == "Laptop"


def test_list_orders(session):
    product_repo = SqlAlchemyProductRepository(session)
    order_repo = SqlAlchemyOrderRepository(session)

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
    product_repo.add(product1)
    product_repo.add(product2)

    order1 = Order(id=None, products=[product1])
    order2 = Order(id=None, products=[product2])
    order_repo.add(order1)
    order_repo.add(order2)

    orders = order_repo.list()
    assert len(orders) == 2
    assert len(orders[0].products) == 1
    assert len(orders[1].products) == 1
    assert orders[0].products[0].name == "Laptop"
    assert orders[1].products[0].name == "Phone"


def test_remove_order(session):
    product_repo = SqlAlchemyProductRepository(session)
    order_repo = SqlAlchemyOrderRepository(session)

    product = Product(
        id=None,
        name="Laptop",
        description="High performance laptop",
        unit="pcs",
        price=Price(1500.0),
        quantity=Quantity(10),
    )
    product_repo.add(product)

    order = Order(id=None, products=[product])
    order_repo.add(order)

    order_repo.remove(order.id)

    assert order_repo.get(order.id) is None

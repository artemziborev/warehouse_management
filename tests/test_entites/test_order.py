from domain.entities.order import Order
from domain.entities.product import Product
from domain.entities.value_objects import Price, Quantity


def test_create_order():
    order = Order(id=None)
    assert order.id is None
    assert order.is_empty()


def test_add_product_to_order():
    order = Order(id=None)
    product = Product(
        id=1,
        name="Laptop",
        description="High performance laptop",
        unit="pcs",
        price=Price(1500.0),
        quantity=Quantity(10),
    )
    order.add_product(product)
    assert len(order.products) == 1
    assert order.products[0].name == "Laptop"


def test_remove_product_from_order():
    order = Order(id=None)
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

    order.add_product(product1)
    order.add_product(product2)

    order.remove_product(product1.id)

    assert len(order.products) == 1
    assert order.products[0].name == "Phone"


def test_total_price():
    order = Order(id=None)
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

    order.add_product(product1)
    order.add_product(product2)

    assert order.total_price() == 2000.0


def test_total_quantity():
    order = Order(id=None)
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

    order.add_product(product1)
    order.add_product(product2)

    assert order.total_quantity() == 15


def test_order_is_empty():
    order = Order(id=None)
    assert order.is_empty()


def test_order_is_not_empty():
    order = Order(id=None)
    product = Product(
        id=1,
        name="Laptop",
        description="High performance laptop",
        unit="pcs",
        price=Price(1500.0),
        quantity=Quantity(10),
    )
    order.add_product(product)
    assert not order.is_empty()

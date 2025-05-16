from domain.entities.product import Product
from domain.entities.value_objects import Price, Quantity


def test_create_product():
    product = Product(
        id=None,
        name="Laptop",
        description="High performance laptop",
        unit="pcs",
        price=Price(1500.0),
        quantity=Quantity(10),
    )
    assert product.name == "Laptop"
    assert product.description == "High performance laptop"
    assert product.unit == "pcs"
    assert product.price.value == 1500.0
    assert product.quantity.value == 10


def test_change_price():
    product = Product(
        id=None,
        name="Laptop",
        description="High performance laptop",
        unit="pcs",
        price=Price(1500.0),
        quantity=Quantity(10),
    )
    product.change_price(2000.0)
    assert product.price.value == 2000.0


def test_change_quantity():
    product = Product(
        id=None,
        name="Laptop",
        description="High performance laptop",
        unit="pcs",
        price=Price(1500.0),
        quantity=Quantity(10),
    )
    product.change_quantity(20)
    assert product.quantity.value == 20


def test_product_is_available():
    product = Product(
        id=None,
        name="Laptop",
        description="High performance laptop",
        unit="pcs",
        price=Price(1500.0),
        quantity=Quantity(10),
    )
    assert product.is_available()


def test_product_is_not_available():
    product = Product(
        id=None,
        name="Laptop",
        description="High performance laptop",
        unit="pcs",
        price=Price(1500.0),
        quantity=Quantity(0),
    )
    assert not product.is_available()

from app.adapters.repositories.product_repository import SqlAlchemyProductRepository
from domain.entities.product import Product
from domain.entities.value_objects import Price, Quantity


def test_add_and_get_product(session):
    repo = SqlAlchemyProductRepository(session)

    # Добавляем продукт
    product = Product(
        id=None,
        name="Laptop",
        description="High performance laptop",
        unit="pcs",
        price=Price(1500.0),
        quantity=Quantity(10),
    )
    repo.add(product)

    # Проверяем получение продукта
    retrieved = repo.get(product.id)
    assert retrieved is not None
    assert retrieved.name == "Laptop"
    assert retrieved.price.value == 1500.0
    assert retrieved.quantity.value == 10


def test_list_products(session):
    repo = SqlAlchemyProductRepository(session)

    # Добавляем несколько продуктов
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
    repo.add(product1)
    repo.add(product2)

    # Проверяем список продуктов
    products = repo.list()
    assert len(products) == 2
    assert products[0].name == "Laptop"
    assert products[1].name == "Phone"


def test_remove_product(session):
    repo = SqlAlchemyProductRepository(session)

    # Добавляем продукт
    product = Product(
        id=None,
        name="Laptop",
        description="High performance laptop",
        unit="pcs",
        price=Price(1500.0),
        quantity=Quantity(10),
    )
    repo.add(product)

    # Удаляем продукт
    repo.remove(product.id)

    # Проверяем, что продукт удален
    assert repo.get(product.id) is None

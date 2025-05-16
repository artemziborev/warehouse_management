import pytest

from domain.entities.product import Product
from domain.entities.value_objects import Price, Quantity
from domain.exceptions import EntityNotFoundException
from use_cases.create_order import CreateOrderUseCase


def test_create_order(uow):
    # Добавляем продукт для теста
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
        uow.commit()

    # Создаем заказ
    use_case = CreateOrderUseCase(uow)
    order = use_case.execute([product.id])

    # Проверяем, что заказ создан
    assert order.id is not None
    assert len(order.products) == 1
    assert order.products[0].name == "Laptop"


def test_create_order_with_nonexistent_product(uow):
    use_case = CreateOrderUseCase(uow)

    # Проверяем, что создается исключение для несуществующего продукта
    with pytest.raises(EntityNotFoundException, match="Product with ID 999 not found"):
        use_case.execute([999])


def test_create_order_with_multiple_products(uow):
    # Добавляем несколько продуктов для теста
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

    # Создаем заказ с несколькими продуктами
    use_case = CreateOrderUseCase(uow)
    order = use_case.execute([product1.id, product2.id])

    # Проверяем, что заказ создан
    assert order.id is not None
    assert len(order.products) == 2
    assert order.products[0].name == "Laptop"
    assert order.products[1].name == "Phone"

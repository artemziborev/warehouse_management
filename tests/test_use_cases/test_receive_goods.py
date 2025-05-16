import pytest

from domain.entities.product import Product
from domain.entities.value_objects import Price, Quantity
from domain.exceptions import EntityNotFoundException
from use_cases.receive_goods import ReceiveGoodsUseCase


def test_receive_goods(uow):
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

    # Принимаем товар
    use_case = ReceiveGoodsUseCase(uow)
    use_case.execute(product.id, 5)

    # Проверяем, что количество обновилось
    with uow:
        updated_product = uow.products.get(product.id)
        assert updated_product.quantity.value == 15


def test_receive_goods_for_nonexistent_product(uow):
    use_case = ReceiveGoodsUseCase(uow)

    # Проверяем, что создается исключение для несуществующего продукта
    with pytest.raises(EntityNotFoundException, match="Product with ID 999 not found"):
        use_case.execute(999, 5)


def test_receive_goods_with_negative_quantity(uow):
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

    # Проверяем, что создается исключение для отрицательного количества
    use_case = ReceiveGoodsUseCase(uow)
    with pytest.raises(ValueError, match="Quantity must be non-negative"):
        use_case.execute(product.id, -5)

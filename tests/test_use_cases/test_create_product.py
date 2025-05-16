import pytest

from use_cases.create_product import CreateProductUseCase


def test_create_product(uow):
    use_case = CreateProductUseCase(uow)

    product = use_case.execute(
        name="Laptop",
        description="High performance laptop",
        unit="pcs",
        price=1500.0,
        quantity=10,
    )

    assert product.id is not None
    assert product.name == "Laptop"
    assert product.price.value == 1500.0
    assert product.quantity.value == 10


def test_create_product_with_invalid_price(uow):
    use_case = CreateProductUseCase(uow)

    with pytest.raises(ValueError, match="Price must be positive"):
        use_case.execute(
            name="Laptop",
            description="High performance laptop",
            unit="pcs",
            price=-1500.0,
            quantity=10,
        )


def test_create_product_with_invalid_quantity(uow):
    use_case = CreateProductUseCase(uow)

    with pytest.raises(ValueError, match="Quantity must be non-negative"):
        use_case.execute(
            name="Laptop",
            description="High performance laptop",
            unit="pcs",
            price=1500.0,
            quantity=-10,
        )

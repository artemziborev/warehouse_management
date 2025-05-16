from typing import List, Optional

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from domain.entities.product import Product
from domain.entities.value_objects import Price, Quantity
from domain.repositories.interfaces.product_repository import ProductRepository
from framework_drivers.orm.product_orm import ProductORM


class SqlAlchemyProductRepository(ProductRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, product: Product) -> None:
        product_orm = ProductORM(
            name=product.name,
            description=product.description,
            unit=product.unit,
            price=product.price.value,
            quantity=product.quantity.value,
        )
        self.session.add(product_orm)
        self.session.flush()
        product.id = product_orm.id

    def get(self, product_id: int) -> Optional[Product]:
        try:
            product_orm = self.session.query(ProductORM).filter_by(id=product_id).one()
            return Product(
                id=product_orm.id,
                name=product_orm.name,
                description=product_orm.description,
                unit=product_orm.unit,
                price=Price(product_orm.price),
                quantity=Quantity(product_orm.quantity),
            )
        except NoResultFound:
            return None

    def list(self) -> List[Product]:
        return [
            Product(
                id=p.id,
                name=p.name,
                description=p.description,
                unit=p.unit,
                price=Price(p.price),
                quantity=Quantity(p.quantity),
            )
            for p in self.session.query(ProductORM).all()
        ]

    def remove(self, product_id: int) -> None:
        self.session.query(ProductORM).filter_by(id=product_id).delete()
        self.session.flush()

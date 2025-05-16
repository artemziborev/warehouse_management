from typing import List, Optional

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from domain.entities.order import Order
from domain.entities.product import Product
from domain.entities.value_objects import Price, Quantity
from domain.repositories.interfaces.order_repository import OrderRepository
from framework_drivers.orm.order_orm import OrderORM
from framework_drivers.orm.product_orm import ProductORM


class SqlAlchemyOrderRepository(OrderRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, order: Order) -> None:
        order_orm = OrderORM()
        order_orm.products = [
            self.session.query(ProductORM).filter_by(id=p.id).one()
            for p in order.products
        ]
        self.session.add(order_orm)
        self.session.flush()
        order.id = order_orm.id

    def get(self, order_id: int) -> Optional[Order]:
        try:
            order_orm = self.session.query(OrderORM).filter_by(id=order_id).one()
            products = [
                Product(
                    id=p.id,
                    name=p.name,
                    description=p.description,
                    unit=p.unit,
                    price=Price(p.price),
                    quantity=Quantity(p.quantity),
                )
                for p in order_orm.products
            ]
            return Order(id=order_orm.id, products=products)
        except NoResultFound:
            return None

    def list(self) -> List[Order]:
        return [
            Order(
                id=o.id,
                products=[
                    Product(
                        id=p.id,
                        name=p.name,
                        description=p.description,
                        unit=p.unit,
                        price=Price(p.price),
                        quantity=Quantity(p.quantity),
                    )
                    for p in o.products
                ],
            )
            for o in self.session.query(OrderORM).all()
        ]

    def remove(self, order_id: int) -> None:
        self.session.query(OrderORM).filter_by(id=order_id).delete()
        self.session.flush()

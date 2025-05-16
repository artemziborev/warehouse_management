from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship

from framework_drivers.orm.base import Base

order_product_association = Table(
    "order_product_association",
    Base.metadata,
    Column("order_id", ForeignKey("orders.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "product_id", ForeignKey("products.id", ondelete="CASCADE"), primary_key=True
    ),
)


class OrderORM(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    products = relationship(
        "ProductORM",
        secondary=order_product_association,
        backref="orders",
        cascade="all, delete",
    )

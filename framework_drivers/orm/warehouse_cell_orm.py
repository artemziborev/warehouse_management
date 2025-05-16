from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from framework_drivers.orm.base import Base

cell_product_association = Table(
    "cell_product_association",
    Base.metadata,
    Column(
        "cell_id",
        ForeignKey("warehouse_cells.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "product_id", ForeignKey("products.id", ondelete="CASCADE"), primary_key=True
    ),
)


class WarehouseCellORM(Base):
    __tablename__ = "warehouse_cells"

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, nullable=False, unique=True)
    capacity = Column(Integer, nullable=False)
    products = relationship(
        "ProductORM",
        secondary=cell_product_association,
        backref="cells",
        cascade="all, delete",
    )

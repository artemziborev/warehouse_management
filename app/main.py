from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.adapters.unit_of_work import SqlAlchemyUnitOfWork
from framework_drivers.orm.base import Base
from use_cases.create_order import CreateOrderUseCase
from use_cases.create_product import CreateProductUseCase
from use_cases.inventory_management import InventoryManagementUseCase
from use_cases.receive_goods import ReceiveGoodsUseCase
from use_cases.ship_order import ShipOrderUseCase


def setup_database():
    engine = create_engine("sqlite:///warehouse.db")
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)


def main():
    # Setup database
    Session = setup_database()

    try:
        with Session() as session:
            with SqlAlchemyUnitOfWork(session) as uow:
                # Use Cases
                create_product_use_case = CreateProductUseCase(uow)
                create_order_use_case = CreateOrderUseCase(uow)
                receive_goods_use_case = ReceiveGoodsUseCase(uow)
                ship_order_use_case = ShipOrderUseCase(uow)
                inventory_management_use_case = InventoryManagementUseCase(uow)

                # Create a new product
                product = create_product_use_case.execute(
                    name="Laptop",
                    description="High performance laptop",
                    unit="pcs",
                    price=1500.0,
                    quantity=10,
                )
                print(f"Product created: {product}")

                # Receive additional stock
                receive_goods_use_case.execute(
                    product_id=product.id, additional_quantity=5
                )
                print(f"Stock received for product {product.id}")

                # Create a new order
                order = create_order_use_case.execute([product.id])
                print(f"Order created: {order}")

                # Ship the order
                ship_order_use_case.execute(order.id)
                print(f"Order shipped: {order.id}")

                # Print current inventory
                inventory = inventory_management_use_case.execute()
                print("\nCurrent Inventory:")
                for item in inventory:
                    print(f"Product: {item.name}, Quantity: {item.quantity.value}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

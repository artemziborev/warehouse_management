class EntityNotFoundException(Exception):
    def __init__(self, entity_name: str, entity_id: int):
        super().__init__(f"{entity_name} with ID {entity_id} not found")


class InsufficientStockException(Exception):
    def __init__(self, product_id: int, available: int):
        super().__init__(
            f"Product with ID {product_id} has only {available} items in stock"
        )


class WarehouseCellFullException(Exception):
    def __init__(self, cell_id: int):
        super().__init__(f"Warehouse cell with ID {cell_id} is full")

from datetime import datetime


class ProductPrice:
    def __init__(self, product_id, price) -> None:
        self.product_id = product_id
        self.price = price
        self.created_at = datetime.now()

class Product:
    def __init__(self, name, price, available, store, link='') -> None:
        self.name = name
        self.price = price
        self.link = link
        self.available = available
        self.store = store

    def __str__(self) -> str:
        return f'{self.name}, {self.price}, {self.store}, {"Disponível" if self.available else "Indisponível"}'

    def to_object(self):
        return {
            'available': self.available,
            'name': self.name,
            'price': self.price,
            'store': self.store,
            'link': self.link
        }

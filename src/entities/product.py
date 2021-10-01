class Product:
    def __init__(self, name, price, available, store) -> None:
        self.name = name
        self.price = price
        self.available = available
        self.store = store

    def __str__(self) -> str:
        return f'{self.name}, {self.price}, {self.store}, {"Disponível" if self.available else "Indisponível"}'

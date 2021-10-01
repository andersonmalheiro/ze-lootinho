from typing import Any, Sequence
from urllib.request import urlopen

from bs4 import BeautifulSoup
from bs4.element import ResultSet

from src.entities.product import Product
from src.utils.kabum.get_product_data import get_product_data


def nvidia():
    url = "https://www.kabum.com.br/hardware/placa-de-video-vga/nvidia?page_number=1&page_size=100&facet_filters=eyJrYWJ1bV9wcm9kdWN0IjpbInRydWUiXX0=&sort=price"
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')

    products: Sequence[Product] = []

    product_cards: ResultSet[Any] = bs.find_all(
        'div', {'class': 'productCard'})

    for card in product_cards:
        product = get_product_data(card)
        products.append(product)

    return products

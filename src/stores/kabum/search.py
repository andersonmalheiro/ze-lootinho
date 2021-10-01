from typing import Sequence
from urllib.request import urlopen

from bs4 import BeautifulSoup

from src.entities.product import Product
from src.utils.kabum.get_product_data import get_product_data


def search(product_name) -> Sequence[Product]:
    products: Sequence[Product] = []

    separator = '+'
    formated_name = separator.join(product_name.split(' '))

    url = f'https://www.kabum.com.br/busca?query={formated_name}&page_number=1&page_size=40&facet_filters=&sort=price'

    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')

    product_cards = bs.find_all('div', {'class': 'productCard'})

    for card in product_cards:
        product = get_product_data(card)
        products.append(product)

    return products

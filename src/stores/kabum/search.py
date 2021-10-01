from typing import Sequence
from urllib.request import urlopen
from bs4 import BeautifulSoup
from src.entities.product import Product


def search(product_name) -> Sequence[Product]:
    products: Sequence[Product] = []

    separator = '+'
    formated_name = separator.join(product_name.split(' '))

    url = f'https://www.kabum.com.br/busca?query={formated_name}&page_number=1&page_size=40&facet_filters=&sort=price'

    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')

    print("searching products...")
    product_cards = bs.find_all('div', {'class': 'productCard'})

    for card in product_cards:
        name = card.find('h2', {'class': 'nameCard'}).text

        price: str = card.find('span', {'class': 'priceCard'}).text.replace(".", "").replace(
            ",", ".").replace("R$", "").strip()

        formated_price = 0

        try:
            formated_price = float(price)
        except:
            pass

        unavailable = card.find('div', {'class': 'unavailableFooterCard'})

        products.append(Product(name=name.lower(), price=formated_price,
                                available=not bool(unavailable), store="Kabum"))

    print("products obtained.")
    return products

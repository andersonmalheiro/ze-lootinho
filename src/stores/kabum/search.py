from urllib.request import urlopen
from bs4 import BeautifulSoup
from src.entities.product import Product


def search(product_name):
    separator = '+'
    formated_name = separator.join(product_name.split(' '))
    url = f'https://www.kabum.com.br/busca?query={formated_name}&page_number=1&page_size=20&facet_filters=&sort=price'
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')

    products = []

    product_cards = bs.find_all('div', {'class': 'productCard'})

    for card in product_cards:
        name = card.find('h2', {'class': 'nameCard'}).text
        price = card.find('span', {'class': 'priceCard'}).text
        unavailable = card.find('div', {'class': 'unavailableFooterCard'})

        product = Product(name=name, price=price,
                          available=not bool(unavailable), store="Kabum")

        products.append(product)

    return products

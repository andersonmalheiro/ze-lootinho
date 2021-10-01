from urllib.request import urlopen
from bs4 import BeautifulSoup
from src.entities.product import Product


def nvidia_serie_16_search():
    url = "https://www.kabum.com.br/hardware/placa-de-video-vga/nvidia/geforce-gtx-serie-16?page_number=1&page_size=20&facet_filters=&sort=price"
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

from urllib.request import urlopen
from bs4 import BeautifulSoup
from src.entities.product import Product


def nvidia():
    url = "https://www.terabyteshop.com.br/hardware/placas-de-video/nvidia-geforce"
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')

    products = []

    product_cards = bs.find_all('div', {'class': 'pbox'})

    for card in product_cards:
        name = card.find('a', {'class': 'prod-name'}).text
        price = card.find('div', {'class': 'prod-new-price'}).text
        unavailable = card.find('div', {'class': 'tbt_esgotado'})

        product = Product(name=name, price=price,
                          available=not bool(unavailable), store="Terabyte")

        products.append(product)

    return products

from typing import Any

from src.entities.product import Product


def get_product_data(card: Any) -> Product:
    base_url = 'https://www.kabum.com.br'

    name = card.find('h2', {'class': 'nameCard'}).text

    link = card.find('a')['href']

    price: str = card.find('span', {'class': 'priceCard'}).text.replace(".", "").replace(
        ",", ".").replace("R$", "").strip()

    formated_price = 0

    try:
        formated_price = float(price)
    except:
        pass

    unavailable = card.find('div', {'class': 'unavailableFooterCard'})

    return Product(name=name.lower(), price=formated_price,
                   available=not bool(unavailable), store="Kabum", link=f'{base_url}{link}')

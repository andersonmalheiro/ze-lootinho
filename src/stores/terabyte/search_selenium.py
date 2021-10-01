import os
import sys
from time import sleep, time
from typing import Sequence

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from src.entities.product import Product


def create_driver_instance(headless=False) -> WebDriver:
    options = Options()
    options.add_argument(f"user-data-dir={os.getcwd()}/user-data")

    if headless:
        options.headless = True

    driver_path = f'{os.getcwd()}/src/drivers/chromedriver'
    driver = webdriver.Chrome(executable_path=driver_path, options=options)

    return driver


def get_error_screenshot(driver: WebDriver):
    img_path = f'{os.getcwd()}/screenshots/{str(time())}.png'
    print(img_path)
    saved = driver.save_screenshot(img_path)

    if not saved:
        print("Error when making screenshot")


def terabyte_nvidia():
    driver = create_driver_instance()
    products: Sequence[Product] = []

    driver.get(
        "https://www.terabyteshop.com.br/hardware/placas-de-video/nvidia-geforce")

    sleep(10)
    # FIXME: find solution to "Under attack mode"

    # driver.add_cookie(
    #     {'name': 'PHPSESSID', 'value': 'vooppg784g5poidicsdpouue52'})
    # driver.add_cookie({'name': '_tnd', 'value': '1627503122960'})
    # driver.add_cookie({'name': '_tnwc', 'value': 's=m|m=i|a=null|d=null'})
    # driver.add_cookie(
    #     {'name': '_tnt', 'value': 'AYq63gfm5SmIeEPxihvz0Uy3ulCtMp2s'})
    # driver.add_cookie(
    #     {'name': 'cf_clearance', 'value': 'Dled.TAOzdyyD.lmaNDxC8QJ.Tzoawu1U0Ht_F_g.iM-1633010370-0-150'})
    # driver.add_cookie({'name': '__cf_bm', 'value': 'QSaSYu5jX6dGxyfTWNQ0lYr_NqEA0y.fUqHZ8sYsJ0A-1633025082-0-AeWbuW3yNMXkci1yaHTnZYHuy0YO3+68c2F/SEWPMxzJGvOlFW4K87WIymB00oBWBDcMhpIsBCL4ccv4J5GXXP8RhKC83TwS9aCQHDX/9gzZ'})

    driver.implicitly_wait(10)

    print("Finding items...")

    try:
        driver.find_element_by_id('prodarea')

        html = driver.page_source
        bs = BeautifulSoup(html, 'html.parser')

        product_cards = bs.find_all('div', {'class': 'pbox'})

        for card in product_cards:
            name = ''
            price = ''
            unavailable = False

            try:
                name: str = card.find('a', {'class': 'prod-name'}).text
                price_txt: str = card.find(
                    'div', {'class': 'prod-new-price'}).text
                price_parts = price_txt.split(' ')
                price = f"{price_parts[0]} {price_parts[1]}"

                unavailable = card.find('div', {'class': 'tbt_esgotado'})

                products.append(Product(name=name, price=price,
                                        available=not bool(unavailable), store="Terabyte"))

            except:
                pass

    except:
        get_error_screenshot(driver)
        print("Unexpected error:", sys.exc_info()[0])
        pass

    print("Finishing...")

    sleep(5)
    driver.close()

    return products

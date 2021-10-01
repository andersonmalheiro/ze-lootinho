from typing import Sequence
from src.entities.product import Product
from json import dumps


def res_to_json(results: Sequence[Product]):
    return dumps([item.to_object() for item in results])

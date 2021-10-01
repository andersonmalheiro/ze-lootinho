from typing import Sequence

from src.entities.product import Product
from src.products.gpus import gpu_list
from src.stores.kabum.nvidia_gpus import nvidia
from src.stores.kabum.search import search


def get_gpus():
    results: Sequence[Product] = []

    print("searching...")
    search_res = nvidia()

    print("filtering products...")
    for p in gpu_list:
        filtered = list(
            filter(lambda item: item.name.find(p) != -1 and item.available, search_res))

        results.extend(filtered)

    print('sorting by price...')
    ordered_by_price = sorted(results, key=lambda item: item.price)

    print('generating JSON...')
    return list(map(lambda item: item.to_object(), ordered_by_price))

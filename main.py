from typing import Sequence

from src.entities.product import Product
from src.products.gpus import gpu_list
from src.products.cpus import cpus_list
from src.stores.kabum.search import search
from src.utils.results_to_json import res_to_json


def main():
    results: Sequence[Product] = []

    for p in gpu_list:
        search_res = search(p)

        print("filtering products...")
        filtered = list(
            filter(lambda item: item.name.find(p) != -1 and item.available, search_res))

        results.extend(filtered)

    print("ordering by best prices...")
    ordered_by_price = sorted(results, key=lambda item: item.price)

    print("generating JSON...")
    print(res_to_json(ordered_by_price))

    print("\ndone.")


if __name__ == '__main__':
    main()

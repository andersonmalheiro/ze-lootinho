from src.stores.kabum.nvidia_serie_16 import nvidia_serie_16_search
from src.stores.kabum.search import search
from src.stores.terabyte.nvidia import nvidia
from src.stores.terabyte.search_selenium import terabyte_nvidia


def main():
    # kabum_serie_16 = nvidia_serie_16_search()
    terabyte_results = terabyte_nvidia()

    for p in terabyte_results:
        print(p)


if __name__ == '__main__':
    main()

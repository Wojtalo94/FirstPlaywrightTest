# W testach importujemy klase:
from pages.search import SearchPage


def test_bing_search(set_up) -> None:
    page = set_up
    # zaimportowana funkcja z parametrem page (bo taka też jest przyjmowana w funkcji specjalnej __init__ w tej klasie)
    search_page = SearchPage(page)
    # wywołujemy otwieranie strony w danej klasie
    search_page.navigate()
    # wywoułujemy wyszukanie, czyli akcje na tej stronie
    search_page.search("search query")
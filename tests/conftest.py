import pytest
from playwright.sync_api import Playwright

# ten plik będzie globalnym conftestem dla całego projektu, wszystkich testów, umieszczamy go w folderze z testami, aby python miał dostęp do niego dla testów
# fixtures - dokumentacja: https://docs.pytest.org/en/7.2.x/explanation/fixtures.html#what-fixtures-are/, fixtures służą to testów oprogramowania, zapewniają taką spójność, niezawodność, dają takie same wyniki, czyli są to generanie takie ustawienia które pozwolą nam np. mieć porządek w serwisach, w jakiś warunkach, środowisku testowym. Te elementy ustawień fixtures będą sie znajdować w pliku conftest.py. Ten plik python będzie automatycznie skanował i szukał tego pliku i będzie z niego korzystał. GENERALNIE w pythonie fixtures są znane w bibliotece pytestu i fixtures to specjalny rodzaj funkcji która umożliwia tworzenie ustalonego środowiska do testów, czyli są wykorzystywane do USTAWIEŃ ŚRODOWISKA TESTÓW. Mogą być też używane do przygotowania danych wejściowych, symulacji baz danych, konfiguracji API, czy nawet mockowania obiektów (czyli takich fałszywych obiektów).

# utwórzmy metodę set_up do przechowywania ustawień przeglądarki, mogą też one dotyczyć pewnego zakresu (scope), jeśli ustawimy na "session", to będzie fixtures na daną sesję w przeglądarce (czyli jeśli uruchomimy przeglądarke w trybie incognito i uruchomimy ją drugi raz, to będzie to nowa sesja w danej przeglądarce i np. hasła nie będą zapamiętane w obrębie tego fixtures i będziemy cały czas zaczynać od nowa i będzie trzeba np. akceptować te termsy, privet polisy itd.). Możemy i tak ustawmy na poziomie funkcji czyli "function", możemy też utworzyć na poziomie przeglądarki a więc "browser"
# wywołajmy fixtures z pytestu dla metody set_up
@pytest.fixture(scope="function")
def set_up(playwright: Playwright):
    # slow_mo spowalnia wykonywanie akcji, aby lepiej widzieć, wartość podana w milisekundach, 1500msec=1.5sec, przydatne do debugowania, ale defaultowo musi być wyłączone, bo będą testy trwały ZBYT DŁUGO
    # headless=False sprawia że otwiera nam się przeglądarka, można by to wywalć, tak jak slow_mo i używać tego podczas uruchamia testów z terminala wpisując: 'pytest --headed --slowmo=1500 --device="iPhone 14 --full-page-screenshot"'
    browser = playwright.chromium.launch(headless=False, slow_mo=1500)
    page = browser.new_page()
    page.goto("https://www.google.com/")
    page.set_default_timeout(15000)

    # słowo kluczowe yield, to taki specyficzny return i zwróćmy sobie tutaj page 
    yield page
    # zakończmy tą sesję
    page.close()

# Automated Tests - Playwright od jaktestowac.pl

Playwright jest narzędzie (a raczej zbiór bibliotek) które pozwala na pisanie testów automatycznych stron internetowych. Playwright pozwala testować działanie oraz zachowanie stron internetowych na różnych przeglądarkach.

Warto również odnotować:

- jest rozwijany od początku 2020 przez Microsoft,
- w 2021 pojawił się w wersji stable,
- pozwala obecnie testować przeglądarki (silniki) takie jak Chromium, Firefox oraz WebKit,
- Playwright wspiera emulacje urządzeń mobilnych,
- oferuje wsparcie dla wielu domen, stron oraz tabów w testach,
- na Docker Hub dostępny jest oficjalny Docker Image, z którego można korzystać przy puszczaniu testów na CI,
- jest dostępny dla systemów Windows, Linux i Mac OS,
- Playwright jest Open Source i w pełni darmowy,
- Playwright zawiera koncept Auto-waiting, który ma za zadanie zmniejszyć potrzebę stosowania funkcji do czekania na elementy na stronie.

Ograniczenia:

- brak wsparcia dla IE 11 i starszych wersji Edge (aczkolwiek nowy Edge na Chromium jest wspierany) ,
- brak wsparcia dla rzeczywistych urządzeń mobilnych (obecnie jedynie możliwość emulacji).

Na początku venv:
C:\Python38-10-64\python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip

1. Instalujemy playwright
   pip install pytest-playwright (pewnie rozwiązując problemy/braki)
2. Instalujemy wszystkie przeglądarki które wspiera playwright czyli Chromium, Firefox, Webkid
   playwright install

Dodatkowe rzeczy:

- playwright codegen - generowanie kodu, otwiera się okno przeglądarki za pomocą które możemy klikać oraz drugie okno z playwright inspector, gdzie cały kod będzie generowany, wystarczy wpisać "playwright codegen"
- pytest - aby uruchomić wszystkie testy, wystarczy wpisać pytest w terminal

Linki warte uwagi:

- https://github.com/microsoft/playwright – oficjalne repozytorium na GitHub,
- https://playwright.dev/python/docs/intro/ – oficjalna dokumentacja,
- https://playwright.dev/python/docs/test-runners/ – Pytest plugin.
- https://the-internet.herokuapp.com - strona do ćwiczeń testów automatycznych
- https://www.youtube.com/watch?v=y8zY14HHiPI&list=PLP5_A7hnY1Tggph0F0cRqf5iyyZuIBXYC oraz https://www.youtube.com/watch?v=VZ5LU8vHT0s&list=PLhW3qG5bs-L8WcAa9cfXaqGe0-Cq85y4X - lekcje z playwright dużo bardziej rozwinięte
- BRAKUJE tutaj linku z testami automatycznymi dla python+playwright

Teoria:

- POM (Page Object Model) - polega na tym że będziemy oddzielać UI (User Interface) od testów. Czyli będziemy chcieli żeby testy używające klas Page Object Model do interakcji z UI czyli interfejsem użytkownika były wypracowane w osobnej klasie, żeby kod był czystszy, czytelniejszy, łatwiejszy w naprawie i aby ten kod można było używać wiele razy, w różnych testach z jednej klasy. Mamy ją też ujętą w dokumentacji: https://playwright.dev/python/docs/pom/

- pytest - zapewnia parametryzację testów, czy danych wejściowych, dobrze integruje się z innymi narzędziami, bibliotekami pythona, dokumentacja pytest: https://docs.pytest.org/en/7.2.x/explanation/goodpractices.html/
- pytest --template=html1/index.html --report=report.html - to jest komenda do uruchamiania w htmlu raportu z testów, aby mieć go dostępnego trzeba zainstalować go 'pip install pytest-reporter-html1'. W głównym repozytorium projektu utworzy się report.html z raportem testów. Aby utworzyć raport np. dla smoke testów to robimy to w ten sposób: "pytest -m smoke --template=html1/index.html --report=smoke_test_report.html", nie wiem czy parametr -m musi być, może tak może nie

- fixtures - dokumentacja: https://docs.pytest.org/en/7.2.x/explanation/fixtures.html#what-fixtures-are/, fixtures służą to testów oprogramowania, zapewniają taką spójność, niezawodność, dają takie same wyniki, czyli są to generanie takie ustawienia które pozwolą nam np. mieć porządek w serwisach, w jakiś warunkach, środowisku testowym. Te elementy ustawień fixtures będą sie znajdować w pliku conftest.py. Ten plik python będzie automatycznie skanował i szukał tego pliku i będzie z niego korzystał. GENERALNIE w pythonie fixtures są znane w bibliotece pytestu i fixtures to specjalny rodzaj funkcji która umożliwia tworzenie ustalonego środowiska do testów, czyli są wykorzystywane do USTAWIEŃ ŚRODOWISKA TESTÓW. Mogą być też używane do przygotowania danych wejściowych, symulacji baz danych, konfiguracji API, czy nawet mockowania obiektów (czyli takich fałszywych obiektów).

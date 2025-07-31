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
C:\Python310-32\python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip

1) Instalujemy playwright
pip install pytest-playwright (pewnie rozwiązując problemy/braki)
2) Instalujemy wszystkie przeglądarki które wspiera playwright czyli Chromium, Firefox, Webkid
playwright install

Dodatkowe rzeczy:
- playwright codegen - generowanie kodu, otwiera się okno przeglądarki za pomocą które możemy klikać oraz drugie okno z playwright inspector, gdzie cały kod będzie generowany
- aby uruchomić testy, wystarczy wpisać pytest



Linki warte uwagi:
https://github.com/microsoft/playwright – oficjalne repozytorium na GitHub,
https://playwright.dev/python/docs/intro/ – oficjalna dokumentacja,
https://playwright.dev/python/docs/test-runners/ – Pytest plugin.













import pytest
from playwright.sync_api import expect

# marker pytestu to taka adnotacja pytestu przed testem, który możemy zdefiniować
# adnotacja @pytest.mark.skip(reason="strona nie jest gotowa") test jest pomijany
# natomiast test z markerem xfail: @pytest.mark.xfail(reason="strona nie jest dostępna"), oznaczamy testy gdy np. nie wszystkie resoursy na weba zostały wrzucone przez devów, albo jest jakiś bug i czekamy żeby został naprawiony
@pytest.mark.smoke
# jako parametr użyjmy naszej funkcji set_up
def test_link_playwright_documentation(set_up) -> None:
    # teraz musimy naszego page'a załadować z set_up'u z conftestu, nawet go nie trzeba importować, bo python go od razu wykrywa
    page = set_up
    # niżej czekamy aż strona się załaduje, to może rozwiązać dużo problemów. Domyślnie czeka 30 sekund, my zmniejszmy na 10 sekund
    page.wait_for_load_state(timeout=10000)
    page.get_by_role("button", name="Accept all").click()
    page.get_by_label("Search", exact=True).click()
    page.goto("https://www.google.com/search?q=playwright")
    # jeśli chcemy wyszukać po textcie ale jest ich kilka takich samych i chcemy pobrać np. tylko pierwszy, to robimy to za pomocą funkcji? nth czyli po indexie, bo to działa jak tablica: page.get_by_text("Accept").nth(0), albo możemy użyć first: get_by_text("Accept").first
    # jeśli chcemy użyć CSS, to musimy zrobić na elemencie copy->Selector i powinniśmy dostaniemy np. "ApjFQb" więc robimy: page.locator("#ApjFQb").click(), możemy to znaleźć też w dokumentacji Playwright
    page.get_by_text("Playwright: Fast and reliable end-to-end testing for modern").click()
    # poniższy element musimy podświetlić, aby nam się lista rozwijana pojawiła, nie kliknąć, a właśnie wyświetlić i od tego jest metoda hover. Możemy za pomocą generatora kliknąć w ten element aby dostać jego path.
    page.get_by_text("Node.jsNode.jsPythonJava.NET").hover()
    # dopiero teraz automat kliknie w pythona na liście
    page.get_by_label("Main", exact=True).get_by_role("link", name="Python").click()
    page.get_by_role("link", name="Docs").click()
    # expect jako parametr oczekuje albo page, albo locator albo APIResponse, expect jest playwrightowym assertem, ma on w sobie nie tylko waita, ale także odpytuje wiele razy w ciągu paru sekund o ten elementy który oczekujemy
    (expect(page.get_by_role("link",
                             name="Write tests using web first assertions, page fixtures and locators")).to_be_visible())
    # natomiast tutaj sam expect nie jest dobry, bo nie będzie logów, lepiej dać:
    try:
        (expect(page.get_by_role("link",
                             name="Write tests using web first assertions, page fixtures and locators")).to_be_visible())
    except AssertionError as e:
        self._logger.error(f"Wrong link: {e}. Actual link: {page.url}")
        raise

    
    # aby assert pythonowy zadziałał, trzeba zrobić waita na stronie, aż się ona załaduje, tutaj przychodzi nam z pomocą poniższy kod, który czeka aż strona się załaduje, nie trzeba używać parametrów:
    #page.wait_for_load_state
    # możemy też jako waita użyć wait_for_selector:
    #page.wait_for_selector("text=Write tests using web first assertions, page fixtures and locators"), co warto używać jeśli chcemy użyć assert zamiast expect
    # assert pythonowy pyta tylko raz i nie ma w sobie waita, ale czy przez to nie jest bardziej "prawdomówny" od playwrighta? chyba raczej nie? natomiast expect jest bardziej stabilny, to na pewno, pasowały by natomiast żeby zwracał więcej informacji, logów, że text oczekiwany jest taki a aktualnie jest taki
    #assert page.is_visible("text=Write tests using web first assertions, page fixtures and locators")
    # lista assercji jest też dostępna w dokumentacji playwright
    print('TC is finished')

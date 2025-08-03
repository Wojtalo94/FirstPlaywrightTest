# w pytest testy domyślnie są uruchamiane w trybie headless, więc przeglądarki nie widać, możemy to zmienić min. używając terminala do odpalenia testów "(venv) pytest test_xxxxx.py --headed"

# tworzymy funkcję testu pod pytest, nazwa funkcji powinna być szczegółowa, aby wiadomo było co testuje
# w pyteście dla playwrighta jako pierszy parametr funkcja testu przyjmuje obiekt page i z tego obiektu page będziemy mogli korzystać dalej w teście
# ten obiekt page jest on stroną która jest inicjalizowana przez pytest i jest wstrzykiwana do naszej funkcji testowej i to nam zastępuje inicjalizację przeglądarki, context'u i stowrzenie obiektu strony
# nie musimy też dodawać zamknięcie context'u i przeglądarki gdyż o te elementy dba sam już pytest
def test_antoogle_search(page):
    test_phrase = 'Test'
    page.goto("https://antoogle.testoneo.com/?")
    page.get_by_role("textbox", name="Recipient's username").click()
    page.get_by_role("textbox", name="Recipient's username").fill(test_phrase)
    page.get_by_role("button", name="Search!").click()
    # szukamy nalepiej w konsoli przeglądarki w zakładce Elements elementu który chcemy zweryfikować i pierwszy element ma id="item0"
    # użyjmy funkcji inner_text, pierwszy jego parametrem jest selector (czyli '#item0')
    text1 = page.inner_text('#item0')
    assert text1 == test_phrase, f"Expected value: '{test_phrase}', actual value '{text1}'"


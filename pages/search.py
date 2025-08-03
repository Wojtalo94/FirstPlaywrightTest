# lokatory i selectory wyciągamy do osobnych plików, klas, żeby móc ich używać w innych testach
# lokatory wypisujemy w klasie zaraz pod funkcją specjalną: 
class SearchPage:
    def __init__(self, page):
        self.page = page
        self.search_input = page.locator('[aria-label="Enter search"]')
        self.search_main_input = page.locator('[aria-label="Enter main search"]')


    def navigate(self):
        self.page.goto("https://bing.com")


    # a następnie te lokatory czy selectory używamy w funkcjach w niżej czyli:
    def search(self, text):
        self.search_input.fill(text)
        self.search_input.press("Enter")
import logging


class MainPage:
    def __init__(self, page):
        self.page = page
        self._logger = logging.getLogger("MainPage")


    def open_main_page(self, main_url: str) -> None:
        self._logger.info(f"Open the '{main_url}' main page")
        self.page.goto(main_url)
        self.page.wait_for_load_state(timeout=15000)

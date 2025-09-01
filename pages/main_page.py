import logging


class MainPage:
    def __init__(self, page):
        self.page = page
        self._logger = logging.getLogger("MainPage")


    def sign_in_to_main_page(self, account_data: Dict[str, str], main_url: str) -> None:
        self._logger.info("Logging into dynpack")
        username = account_data.get("username")
        password = account_data.get("password")
        self._logger.info("Checking credentials")
        if not username or not password:
            self._logger.error("Account_data missing 'username' or 'password'")
            raise ValueError("Account_data missing 'username' or 'password'")
        self._username_field.fill(username)
        self._password_field.fill(password)
        self._log_in_button.click()
        self._logger.info("Login submitted, waiting for load main dynpack page.")
        self.page.wait_for_load_state(timeout=15000)

        self._logger.info("Checking the URL address")
        try:
            expect(self.page).to_have_url(main_url)
        except AssertionError as e:
            self._logger.error(f"Incorrect URL: {e}. URL should be: {main_url}")
            raise

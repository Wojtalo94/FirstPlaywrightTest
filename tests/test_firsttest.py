from pages.main_page import mainPage
from typing import Dict


def test_boards(set_up, main_url: str, account_data: Dict[str,str]) -> None:
    page = set_up
    main_page = MainPage(page)

    main_page.open_main_page(main_url)
    main_page.sign_in(account_data, main_url)

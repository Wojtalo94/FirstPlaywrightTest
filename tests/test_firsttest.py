from pages.main_page import mainPage
from typing import Dict


def test_boards(set_up, capture_bad_responses) -> None:
    page = set_up
    main_page = MainPage(page)

    # steps in test

from pages.main_page import mainPage
from pages.x_page import XxxListPage
import pytest


@pytest.mark.ui
@pytest.mark.smoke
def test_checking_form_for_x(set_up, capture_bad_responses, account_data) -> None:
    page = set_up
    main_page = MainPage(page)
    x_page = XxxListPage(page)

    main_page.open_tab_on_main_page("X tab")
    x_page.select_z(3)
    x_page.select_y("Succeeded")
    x_page.select_w(account_data)
    x_page.mark_z()
    x_page.click_add_value_button()
    x_page.clear_filters_in_n_form()
    x_page.check_form_with_default_values()

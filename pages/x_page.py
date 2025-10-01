import time
import logging
from typing import Dict
from playwright.sync_api import expect
from helpers.helpers import date_months_back, date_months_forward


class XxxListPage:
    def __init__(self, page):
        self.page = page
        self._logger = logging.getLogger("XxxListPage")
        # 'x' field
        self._x_field = page.locator("input[name='x_field']")
        # 'Y' field
        self._y_field = page.locator("div.dk-multiselect", has=page.get_by_text("y_field", exact=True)).locator("input:visible")
        # 'Z' checkbox
        self._z_checkbox = page.locator("input[name='z_field']")
        # 'W' field
        self._w_field = page.locator('input[name="w_field"]')
        self._remove_w_value = page.locator("button#btn-remove").nth(0)
        # buttons
        self._clear_button = page.get_by_role("button", name="Clear filters", exact=True)
        self._add_value_button = page.locator("button#btn-add_value_button").nth(1)
        # multi drop down list
        self._multi_dropdown_list = page.locator("div.select__menu-list div.select__option")
        # 'Details' title
        self._details_title = page.locator('input[name="details_title"]')
        # table locators
        self._rows = page.locator("table tbody tr")
        self._x_in_table = self._rows.locator("td").nth(1)
        self._y_in_table = self._rows.locator("td").nth(2)
        self._z_in_table = self._rows.locator("td").nth(3)


    # ------------------------------------ internal helper utilities ------------------------------------
    def _wait_for_z_page(self,timeout: int = 5000) -> None:
        expect(self._details_title).to_be_visible(timeout=timeout)
        time.sleep(0.25)


    # ------------------------------------ actions ------------------------------------
    def select_x(self, months_back: int) -> None:
        start_date = date_months_back(months_back)
        self._logger.info(f"X was selected from: '{start_date}'.")
        self._x_field.fill(start_date)


    def select_y(self, y: str) -> None:
        self._logger.info(f"Y: '{y}' was selected.")
        self._y_field.click()
        self._multi_dropdown_list.filter(has=self.page.get_by_text(y, exact=True)).click()


    def select_w(self, account_data: Dict[str, str]) -> None:
        self._logger.info("W: was selected.")
        self._w_field.click()
        username = account_data.get("username")
        self._multi_dropdown_list.filter(has=self.page.get_by_text(username, exact=True)).click()


    def mark_z(self) -> None:
        self._logger.info("'Z' marked.")
        self._z_checkbox.check()


    def get_x(self, row_index: int):
        value = self._x_field.nth(row_index).inner_text()
        self._logger.info(f"Field 'X' has the value '{value}'.")
        return value


    def get_y(self, row_index: int):
        value = self._y_field.nth(row_index).inner_text()
        self._logger.info(f"Field 'Y' has the value '{value}'.")
        return value


    def click_add_value_button(self, row_index: int) -> None:
        self._logger.info(f"The view button in row '{row_index}' was clicked.")
        self._add_value_button.nth(row_index).click()
        self._wait_for_z_page()


    # ------------------------------------ removals ------------------------------------
    def clear_filters_in_N_form(self) -> None:
        self._logger.info("Form cleared using the Clear filters button")
        self.page.locator(".loader-wrapper").wait_for(state="hidden", timeout=10000)
        expect(self._clear_filters_button).to_be_visible(timeout=5000)
        time.sleep(0.25)
        self._clear_button.click()

    # ------------------------------------ assertions ------------------------------------
    def check_form_with_default_values(self) -> None:
        self._logger.info("The 'Flights' form has default values.")
        fields_with_input_value = [
            (self._x_field, "", "X"),
            (self._y_field, "", "Y"),
            (self._z_field, "", "Z"),
            (self._w_field, "", "W"),
        ]

        for locator, expected, name in fields_with_input_value:
            current_value = locator.input_value()
            try:
                self._logger.info(f"Field {name} has the value '{current_value}'.")
                expect(locator).to_have_value(expected)
            except AssertionError as e:
                self._logger.error(f"AssertionError: {e}. {name} is not empty: '{current_value}'. It should be '{expected}'.")
                raise

        fields_with_span_value = [
            (self._M_field, "All", "M"),
            (self._N_field, "All", "N"),
            (self._B_field, "All", "B"),
            (self._V_field, "All", "V"),
       ]

        for locator, expected, name in fields_with_span_value:
            current_value = locator.inner_text()
            try:
                self._logger.info(f"Field {name} has the value '{current_value}'.")
                expect(locator).to_have_text(expected)
            except AssertionError as e:
                self._logger.error(f"AssertionError: {e}. {name} is not empty: '{current_value}'. It should be '{expected}'.")
                raise

        checkboxes = [
            (self._z_checkbox, "Z"),
            (self._c_checkbox, "C"),
        ]

        for locator, name in checkboxes:
            try:
                self._logger.info(f"Field {name} should be unchecked.")
                expect(locator).not_to_be_checked(timeout=3000)
            except AssertionError as e:
                self._logger.error(f"AssertionError: {e}. {name} is checked. It should be unchecked.")
                raise

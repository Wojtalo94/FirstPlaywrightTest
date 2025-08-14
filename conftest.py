import pytest
import logging
from typing import Dict
from playwright.sync_api import Playwright
from config.config_loader import load_account, load_test_config, load_url_value


logging.basicConfig(filename="logs/logs_web.log",
                    filemode='a',
                    format='%(asctime)s.%(msecs)03d [%(levelname)s][%(name)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def pytest_runtest_setup(item):
    logger.info(f"==========| Start test: {item.name} |==========")


@pytest.fixture(scope="function")
def set_up(playwright: Playwright): 
    config = load_test_config()
    headless = config.get('headless', True)
    slow_mo = config.get('slow_mo', 0)
    browser = playwright.chromium.launch(headless=headless, slow_mo=slow_mo, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.set_default_timeout(15000)

    yield page

    page.close()
    browser.close()


@pytest.fixture(name="main_url", scope="session")
def fixture_main_url() -> str:
    return load_url_value("main_url")


@pytest.fixture(name="sign_out_url", scope="session")
def fixture_sign_out_url() -> str:
    return load_url_value("sign_out_url")


@pytest.fixture(name="account_data", scope="session")
def fixture_account_data() -> Dict[str, str]:
    """Returns a dict: {'username': ..., 'password': ...}"""
    username, password = load_account()
    return {"username": username, "password": password}

import pytest
import logging
from typing import Dict
from playwright.sync_api import Playwright
from helpers.bad_responses import BadResponses
from config.config_loader import load_account, load_test_config, load_url_value


logging.basicConfig(filename="logs/logs_web.log",
                    filemode='a',
                    format='%(asctime)s.%(msecs)03d [%(levelname)s][%(name)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


logging.basicConfig(filename="logs/logs_web.log",
                    filemode='a',
                    format='%(asctime)s.%(msecs)03d [%(levelname)s][%(name)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def pytest_runtest_setup(item):
    logger.info(f"====================| Start test: {item.name} |====================")


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


@pytest.fixture(scope="module")
def module_page(request, playwright: Playwright, sign_out_url):
    """
    Creates browser + context + page once per module (test file).
    Sets the module flag _is_logged_in = False
    """
    config = load_test_config()
    headless = config.get('headless', True)
    slow_mo = config.get('slow_mo', 0)

    browser = playwright.chromium.launch(headless=headless, slow_mo=slow_mo, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.set_default_timeout(15000)

    # flag indicating whether you are already logged in to this module
    setattr(request.module, "_is_logged_in", False)

    yield page

    page.close()
    context.close()
    browser.close()


@pytest.fixture(scope="function", name="set_up")
def set_up(request, module_page):
    """
    Fixture used in tests — returns page (re-uses module_page).
    Does not reset the session, so subsequent tests in the module see the logged-in user
    (provided that the first login has already taken place).
    """
    page = module_page

    yield page


@pytest.fixture(autouse=True)
def login_once_per_module(request, set_up, account_data, main_url):
    """
    Autouse fixture — logs in only once per module (on the first test),
    then sets request.module._is_logged_in = True and skips logging in.
    Thanks to this:
      - when running the entire file: the first test will log in, the next ones will not
      - when running a single test: it will be treated as ‘first’ and will be logged in
    """
    module = request.module
    if not getattr(module, "_is_logged_in", False):

        page = set_up
        sso = SSOPage(page)
        dynpack = DynpackPage(page)
        dynpack.open_main_page(main_url)
        sso.sign_in_to_dynpack(account_data, main_url)
        # we indicate that we are already logged in to the module
        setattr(module, "_is_logged_in", True)

    yield


@pytest.fixture(autouse=True)
def ensure_return_to_main(set_up, main_url, request):
    """Guarantee that after each test we try to open main page so next tests start clean.
    This fixture does NOT assert anything about network responses — it only performs
    the navigation back to main page in teardown. It logs but does not raise on errors
    to avoid masking the original test failure.
    """
    yield

    page = set_up
    try:
        dynpack = DynpackPage(page)
        dynpack.open_main_page(main_url)
    except Exception:
        logger.exception("Failed to open main page during post-test cleanup for %s", request.node.name)


@pytest.fixture(scope="function")
def capture_bad_responses(set_up, request):
    """Create BadResponses BEFORE the test runs so it collects during the test.
    Yields the BadResponses instance so the test can inspect it during execution.
    After the test finishes the fixture will call assert_no_bad_responses() which will
    raise AssertionError if any bad responses were collected (thus failing the test).
    """
    page = set_up
    bad = BadResponses(page)

    yield bad

    bad.assert_no_bad_responses()

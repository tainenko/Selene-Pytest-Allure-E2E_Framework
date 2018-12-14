from common_imports import *
from selene.helpers import env
from selene import config
from selene.browsers import BrowserName

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

browser_instance = env('selene_browser_name') or config.BrowserName.CHROME
base_url = "https://www.etmall.com.tw"


@pytest.fixture(scope="session", autouse=True)
def setup_browser():
    options = Options()
    prefs = {'profile.default_content_setting_values': {'notifications': 2}}#關閉chrome顯示通知
    options.add_experimental_option('prefs', prefs)
    options.add_argument('--window-size=1280,1024')
    driver = webdriver.Chrome(chrome_options=options)
    browser.set_driver(driver)

    config.browser_name = BrowserName.CHROME
    config.start_maximized = True
    #config.hold_browser_open = True
    config.base_url = "https://www.etmall.com.tw"
    config.app_host = ''

    '''
    # turn off selene auto-screenshots
    from selene import helpers
    helpers.take_screenshot = lambda *x: "See attachments"
    yield None
    '''

@pytest.fixture(scope="session", autouse=True)
def allure_config():
    # setup allure environment
    allure.environment(report="Web Automation Report", browser=browser_instance, hostname=base_url)


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def screenshot_on_failure(request):
    yield None
    attach = browser.driver().get_screenshot_as_png()
    if request.node.rep_setup.failed:
        allure.attach(request.function.__name__, attach, allure.attach_type.PNG)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            allure.attach(request.function.__name__, attach, allure.attach_type.PNG)


@pytest.fixture()
def reset_driver_state():
    browser.visit(base_url)

    yield None
    browser.driver().delete_all_cookies()

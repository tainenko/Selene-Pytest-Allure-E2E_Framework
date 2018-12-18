from common_imports import *
from selene.helpers import env
from selene import config
from selene.browsers import BrowserName

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

browser_instance = env('SELENE_BROWSER_NAME') or config.BrowserName.CHROME
base_url =env('SELENE_BASE_URL') or "https://www.etmall.com.tw"


def pytest_addoption(parser):
    parser.addoption("--platform",action="store",default="chrome",
                     help="option:chrome, firefox and  edge")
    parser.addoption("--stage",action="store",default="lab",
                     help="option:lab,mgt,stg,prd,g1,g2")
'''
@pytest.fixture
def platform(request):
    return request.config.getoption("--platform")
'''

def setup_platform(platform):
    return print(platform)

@pytest.fixture(scope="session", autouse=True)
def setup_browser():
    config.browser_name = BrowserName.CHROME
    #config.start_maximized = True
    #config.hold_browser_open = True
    config.base_url = base_url
    config.app_host = ''

    # turn off selene auto-screenshots
    from selene import helpers
    helpers.take_screenshot = lambda *x: "See attachments"
    yield None

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


@pytest.fixture(scope="function",autouse=True)
def screenshot_on_failure(request):
    yield None
    attach = browser.driver().get_screenshot_as_png()
    if request.node.rep_setup.failed:
        allure.attach(request.function.__name__, attach, allure.attach_type.PNG)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            allure.attach(request.function.__name__, attach, allure.attach_type.PNG)


@pytest.fixture(scope='session',autouse=True)
def reset_driver_state(variables):
    options = Options()
    prefs = {'profile.default_content_setting_values': {'notifications': 2}}  # 關閉chrome顯示通知
    options.add_experimental_option('prefs', prefs)
    options.add_argument('--window-size=1280,1024')
    driver = webdriver.Chrome(chrome_options=options)
    browser.set_driver(driver)
    browser.open_url(base_url)
    data=variables
    yield None
    browser.driver().delete_all_cookies()
    browser.driver().close()

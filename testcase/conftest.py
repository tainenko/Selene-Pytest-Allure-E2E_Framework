from common import *
from selene.helpers import env
from selene import config
from selene.browsers import BrowserName
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display



def pytest_addoption(parser):
    parser.addoption("--platform",action="store",default="CHROME",
                     help="option:chrome and firefox.")

@pytest.fixture
def platform(request):
    return request.config.getoption("--platform")

def set_browser_options(platform):
    if platform =='CHROME':
        config.browser_name = BrowserName.CHROME
        options = Options()
        prefs = {'profile.default_content_setting_values': {'notifications': 2}}  # 關閉chrome顯示通知
        options.add_experimental_option('prefs', prefs)
        options.add_argument(--start - maximized) #設定瀏覽器大小
        #options.add_argument('--window-size=1920,10280')
        driver = webdriver.Chrome(chrome_options=options)
        browser.set_driver(driver)
    elif platform =='FIREFOX':
        config.browser_name= BrowserName.FIREFOX
    else:
        print("Sorry, the browser is not supported yet.")
    #elif platform =='EDGE':
    #    config.browser_name=BrowserName.EDGE

@pytest.fixture(scope="session",autouse=True)
def setup_display():
    # Set screen resolution to 1920x1280
    display = Display(visible=0, size=(1920, 1280))
    display.start()
    
@pytest.fixture(scope="module", autouse=True)
def setup_browser():
    config.browser_name = BrowserName.CHROME
    options = Options()
    prefs = {'profile.default_content_setting_values': {'notifications': 2}}  # 關閉chrome顯示通知
    options.add_experimental_option('prefs', prefs)
    options.add_argument("--start-maximized") # 設定瀏覽器大小
    #options.add_argument('--window-size=1920,1280')
    driver = webdriver.Chrome(chrome_options=options)
    browser.set_driver(driver)
    config.base_url=env('SELENE_BASE_URL')
    config.apphost=""

    from selene import helpers # 關閉selene測試失敗時自動截圖功能
    helpers.take_screenshot = lambda *x: "See attachments"
    yield None
    browser.driver().delete_all_cookies() #teardown: reset the state of driver
    browser.driver().quit()

@pytest.fixture(scope="session", autouse=True)
def allure_config():
    # setup allure environment
    allure.environment(report="Web Automation Report--"+env('Web_ENV'),
                       browser=env('SELENE_BROWSER_NAME'),
                       hostname=env('SELENE_BASE_URL'))

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
from selene.api import *
import allure ,pytest
from selene.helpers import env
from selene import config
from selene.browsers import BrowserName
from selenium import webdriver
from selenium.webdriver.chrome.options import Optio/ns
import platform

#from pyvirtualdisplay import Display

def pytest_addoption(parser):
    parser.addoption("--browsertype",action="store",default="CHROME",
                     help="option:chrome and firefox.")
'''
@pytest.fixture
def browsertype(request):
    return request.config.getoption("--browsertype")

def set_browser_options(browsertype):
    if browsertype =='CHROME':
        config.browser_name = BrowserName.CHROME
        options = Options()
        prefs = {'profile.default_content_setting_values': {'notifications': 2}}  # 關閉chrome顯示通知
        options.add_experimental_option('prefs', prefs)
        #options.add_argument(--start - maximized) #設定瀏覽器大小
        options.add_argument('--window-size=1920,1280')
        driver = webdriver.Chrome(chrome_options=options)
        browser.set_driver(driver)
    elif browsertype =='FIREFOX':
        config.browser_name= BrowserName.FIREFOX
    else:
        print("Sorry, the browser is not supported yet.")
    #elif platform =='EDGE':
    #    config.browser_name=BrowserName.EDGE
'''
#@pytest.fixture(scope="session",autouse=True)
#def setup_display():
#    # Set screen resolution to 1920x1280
#    display = Display(visible=0, size=(1920, 1280))
#    display.start()

@pytest.fixture(scope="module", autouse=True)
def setup_browser():
    config.browser_name = env('SELENE_BROWSER_NAME') or BrowserName.CHROME
    options = Options()
    prefs = {'profile.default_content_setting_values': {'notifications': 2}}  # 關閉chrome顯示通知
    options.add_experimental_option('prefs', prefs)
    #options.add_argument("--start-maximized") # 設定瀏覽器大小
    options.add_argument('--window-size=1920,1280')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--headless')
    if platform.system() =="Linux": #判斷以Linux執行時新增相關chrome-option參數
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=options)
    browser.set_driver(driver)
    #set up base_url
    config.base_url=env('SELENE_BASE_URL')
    config.apphost=""

    from selene import helpers # 關閉selene測試失敗時自動截圖功能
    helpers.take_screenshot = lambda *x: "See attachments"
    yield None
    #browser.driver().delete_all_cookies() #teardown: reset the state of driver
    browser.driver().quit()

@pytest.fixture(scope="session", autouse=True)
def allure_config():
    # setup allure environment
    allure.environment(report=env('Web_ENV')+"Web Automation",
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
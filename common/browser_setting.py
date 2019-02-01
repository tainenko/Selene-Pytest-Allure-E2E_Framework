from selene import config
from selene.browsers import BrowserName
from selene.helpers import env
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class BrowserSetting:

    def setChrome(self):
        config.browser_name = BrowserName.CHROME
        options = webdriver.chrome.options.Options()
        prefs = {'profile.default_content_setting_values': {'notifications': 2}}  # 關閉chrome顯示通知
        options.add_experimental_option('prefs', prefs)
        # options.add_argument("--start-maximized") # 設定瀏覽器大小
        options.add_argument('--window-size=1920,1280')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--headless')
        if platform.system() == "Linux":  # 判斷以Linux執行時新增相關chrome-option參數
            options.add_argument('--disable-gpu')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install() ,chrome_options=options)
        return browser.set_driver(driver)

    def setFirefox(self):
        config.browser_name = BrowserName.FIREFOX
        options = webdriver.firefox.options.Options()
        firefox_capabilites = DesiredCapabilities.FIREFOX
        prefs = {'profile.default_content_setting_values': {'notifications': 2}}  # 關閉chrome顯示通知
        options.add_experimental_option('prefs', prefs)
        options.add_argument('--headless')
        options.add_argument('--window-size=1920,1280')
        firefox_capabilites['marionette'] = True
        firefox_capabilites['accetpInsecureCers'] = True
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),capabilities=firefox_capabilites,firefox_options=options)
        return browser.set_driver(driver)

    def setIE(self):
        return 0

    def setEdge(self):
        return 0


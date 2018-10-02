from selene.support.conditions import be
from selene.support.conditions import have
from selene import browser

from src.pages.login_page import LoginPage

def test_user_can_not_login_with_empty_verifySN(setup):
    (LoginPage()
     .open_login_page()
     .login_with_invalid_verifySN("eitctest001@gmail.com","abc12345","")
     .than()
     .validationErr
     .should(have.exct_text("驗證碼輸入錯誤。")))

def test_user_can_login_and_logout(setup):
    login=LoginPage()
    main_page=login.login_as("eitctest001@gmail.com","abc12345").than_at_main_page()
    main_page.logontext.should(be.visible)
    main_page.log_out()
    main_page.loginBtn.sould(be.clickable)

def teardown_module():
    browser.close()


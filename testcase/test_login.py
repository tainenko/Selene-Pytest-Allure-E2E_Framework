# -*- coding: utf-8 -*-
from common_imports import *

from src.pages.login_page import LoginPage


@allure.feature('會員登入功能')  # feature定义功能
@allure.story('登入驗証碼NULL')
def test_user_can_not_login_with_empty_verifySN():
    with allure.step("輸入帳號密碼"):  # 将一个测试用例分成几个步骤，将步骤打印到测试报告中，步骤2
        allure.attach('帳號', 'eitctest001')  # attach可以打印一些附加信息
        allure.attach('密碼', 'abc12345')
    (LoginPage()
    .open_login_page()
    .login_with_invalid_verifySN("eitctest001@gmail.com","abc12345","")
    .than()
    .validationErr
    .should(have.exact_text("必須填寫驗證碼")))

def test_user_can_login_and_logout():
    login=LoginPage()
    main_page=login.login_as("eitctest001@gmail.com","abc12345").than_at_main_page()
    main_page.logontext.should(be.visible)
    main_page.log_out()
    main_page.loginBtn.sould(be.clickable)

def teardown_module():
    browser.close()


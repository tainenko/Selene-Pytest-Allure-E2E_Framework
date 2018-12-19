# -*- coding: utf-8 -*-
from common_imports import *
from src.pages.login_page import LoginPage


@allure.feature('會員登入功能')  # feature定义功能
@pytest.mark.incremental
class TestMemberLogin(object):
    @allure.story('登入驗証碼NULL')
    def test_user_can_not_login_with_empty_verifySN(self,variables):
        user=variables['user']
        password=variables['password']
        with allure.step("輸入帳號密碼"):  # 将一个测试用例分成几个步骤，将步骤打印到测试报告中，步骤2
            allure.attach('帳號', 'eitctest001')  # attach可以打印一些附加信息
            allure.attach('密碼', 'abc12345')
        (LoginPage()
         .open_login_page()
         .login_with_invalid_verifySN(user, password, "")
         .than()
         .validationErr
         .should(have.exact_text("必須填寫驗證碼")))

    @allure.story('登入驗証碼失敗')
    def test_user_login_fail(self,variables):
        user=variables['user']
        password=variables['password']
        with allure.step('開啟登入頁'):pass
        login = LoginPage().open_login_page()
        with allure.step("輸入帳號、密碼，點擊登入Btn"):
            allure.attach('帳號', user)
            allure.attach('密碼', password)
        main_page = login.login_as(user, "abc").than_at_main_page()
        with allure.step("首頁的登入text必須visible，「xxx 您好」"):pass
        main_page.logontext.should(be.visible)
        with allure.step("關閉CrazyAD"):pass
        main_page.close_crazy_banner()
        with allure.step("點擊登出Btn"):pass
        main_page.logoutbtn.should(be.clickable)
        main_page.log_out()
        with allure.step("成功登出，登入Btn可點擊"):pass
        main_page.loginbtn.should(be.clickable)

    @allure.story('會員登入與登出功能')
    def test_user_can_login_and_logout(self,variables):
        user=variables['user']
        password=variables['password']
        with allure.step('開啟登入頁'):pass
        login = LoginPage().open_login_page()
        with allure.step("輸入帳號、密碼，點擊登入Btn"):
            allure.attach('帳號', user)
            allure.attach('密碼', password)
        main_page = login.login_as(user, password).than_at_main_page()
        with allure.step("首頁的登入text必須visible，「xxx 您好」"):pass
        main_page.logontext.should(be.visible)
        with allure.step("關閉CrazyAD"):pass
        main_page.close_crazy_banner()
        with allure.step("點擊登出Btn"):pass
        main_page.logoutbtn.should(be.clickable)
        main_page.log_out()
        with allure.step("成功登出，登入Btn可點擊"):pass
        main_page.loginbtn.should(be.clickable)




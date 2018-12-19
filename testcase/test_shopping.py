# -*- coding: utf-8 -*-
from common import *

from src.pages.main_page import MainPage
from src.pages.login_page import LoginPage
from src.pages.proddetail_page import ProductDetailPage
from src.pages.cartstep1_page import CartStep1Page



@allure.feature('結帳功能')
@pytest.mark.incremental
class TestMemberLogin(object):

    @allure.story('會員登入')
    def test_user_can_login_and_logout(self):
        with allure.step('開啟登入頁'): pass
        login = LoginPage().open_login_page()
        with allure.step("輸入帳號、密碼，點擊登入Btn"):
            allure.attach('帳號', 'eitctest001')
            allure.attach('密碼', 'abc12345')
        main_page = login.login_as("eitctest001@gmail.com", "abc12345").than_at_main_page()
        with allure.step("首頁的登入text必須visible，「xxx 您好」"): pass
        main_page.logontext.should(be.visible)


    @allure.story('加入購物車')
    def test_add_product_to_cart(self,variables):
        proddetail=ProductDetailPage()
        proddetail.open_proddetail_page(variables["product"])
        proddetail.click_go_to_checkout()
        proddetail.than()
        cartstep1 = proddetail.go_to_cart_step1_page()
        cartstep1.deliveryTab.should(be.clickable)


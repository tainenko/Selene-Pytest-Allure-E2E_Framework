# -*- coding: utf-8 -*-
from common import *
from src.pages.main_page import MainPage
from src.pages.login_page import LoginPage
from src.pages.proddetail_page import ProductDetailPage

@allure.feature('結帳功能')
@pytest.mark.incremental
class TestShoppingProcess(object):

    @pytest.fixture(scope="module", autouse=True)
    def setup(self):
        while (True):
            try:
                with allure.step('開啟登入頁'):
                    pass
                login = LoginPage().open_login_page()
                with allure.step("輸入帳號、密碼，點擊登入Btn"):
                    allure.attach('帳號', 'eitctest001')
                    allure.attach('密碼', 'abc12345')
                main_page = login.login_as("eitctest001@gmail.com", "abc12345").than_at_main_page()
                with allure.step("首頁的登入text必須visible，「xxx 您好」"):pass
                main_page.logontext.should(be.visible)
                break
            except NoSuchElement as e:
                print(e, ", try again!")

    @allure.story('一般商品結帳')
    def test_checkout_normal_product(self,variables):
        proddetail=ProductDetailPage()
        proddetail.open_proddetail_page(variables["product"])
        proddetail.click_go_to_checkout()
        proddetail.than()
        cartstep1 = proddetail.go_to_cart_step1_page()
        cartstep1.deliveryTab.should(be.clickable)
        cartstep2=cartstep1.click_checkout_button()
        cartstep3=cartstep2.click_ATM_tab().click_checkout_button()
        cartstep3.text.should(be.visible)

    @allure.story('24快配商品結帳')
    def test_checkout_fast_delivery_product_to(self,variables):
        proddetail=ProductDetailPage()
        proddetail.open_proddetail_page(variables["fastproduct"])
        proddetail.click_go_to_checkout()
        proddetail.than()
        cartstep1 = proddetail.go_to_cart_step1_page()
        cartstep1.checkoutbtn.should(be.clickable)
        cartstep2=cartstep1.click_checkout_button()
        cartstep3=cartstep2.click_COD_tab().click_checkout_button()
        cartstep3.text24.should(be.visible)


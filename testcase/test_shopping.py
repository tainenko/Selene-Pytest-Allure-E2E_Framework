# -*- coding: utf-8 -*-
from common import *
from src.pages.main_page import MainPage
from src.pages.login_page import LoginPage
from src.pages.proddetail_page import ProductDetailPage

@allure.feature('結帳功能')
@pytest.mark.incremental
class TestShoppingProcess(object):

    @pytest.fixture(scope="module", autouse=True)
    def setup(self,variables):
        while (True):
            try:
                with allure.step('前置作業-會員登入'):pass
                login = LoginPage().open_login_page()
                main_page = login.login_as(variables['user'], variables['password']).than_at_main_page()
                main_page.logontext.should(be.visible)
                break
            except NoSuchElement as e:
                print(e, ", try again!")

    @allure.story('一般商品結帳')
    def test_checkout_normal_product(self,variables):
        with allure.step('開啟一般宅配商品-商品細節頁'):pass
        proddetail=ProductDetailPage()
        proddetail.open_proddetail_page(variables["product"])
        with allure.step('點擊立即購買，切換到購物車Step1'): pass
        proddetail.click_go_to_checkout()
        proddetail.than()
        cartstep1 = proddetail.go_to_cart_step1_page()
        with allure.step('購物車Step1，點擊我要結帳'): pass
        cartstep1.deliveryTab.should(be.clickable)
        with allure.step('購物車Step2，選擇ATM付款，點擊確認結帳'): pass
        cartstep2=cartstep1.click_checkout_button()
        cartstep3=cartstep2.click_ATM_tab().click_checkout_button()
        with allure.step('購物車Step3，會出現ATM付款資訊'): pass
        cartstep3.text.should(be.visible)

    @allure.story('24快配商品結帳')
    def test_checkout_fast_delivery_product(self,variables):
        with allure.step('開啟24快配商品-商品細節頁'): pass
        proddetail=ProductDetailPage()
        proddetail.open_proddetail_page(variables["fastproduct"])
        with allure.step('點擊立即購買，切換到購物車Step1'): pass
        proddetail.click_go_to_checkout()
        proddetail.than()
        cartstep1 = proddetail.go_to_cart_step1_page()
        with allure.step('購物車Step1，點擊我要結帳'): pass
        cartstep1.checkoutbtn.should(be.clickable)
        with allure.step('購物車Step2，選擇ATM付款，點擊確認結帳'): pass
        cartstep2=cartstep1.click_checkout_button()
        cartstep3=cartstep2.click_COD_tab().click_checkout_button()
        with allure.step('購物車Step3，會出現感謝付款文案'): pass
        cartstep3.text24.should(be.visible)


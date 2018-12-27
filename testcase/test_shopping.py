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
            except:
                continue

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
        cartstep1.product_img.should(be.visible)
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
        cartstep1.product_img.should(be.visible)
        with allure.step('購物車Step2，選擇ATM付款，點擊確認結帳'): pass
        cartstep2=cartstep1.click_checkout_button()
        cartstep3=cartstep2.click_COD_tab().click_checkout_button()
        with allure.step('購物車Step3，會出現感謝付款文案'): pass
        cartstep3.text24.should(be.visible)

    @allure.story('超取商品結帳')
    def test_checkout_store_pick_up_product(self, variables):
        with allure.step('開啟超取商品-商品細節頁'): pass
        proddetail = ProductDetailPage()
        proddetail.open_proddetail_page(variables["storepickup"])
        with allure.step('點擊立即購買，切換到購物車Step1'): pass
        #proddetail.infoclose.click()
        proddetail.click_store_pick_up()
        proddetail.click_go_to_checkout()
        proddetail.than()
        with allure.step('購物車Step1，點擊我要結帳'): pass
        cartstep1 = proddetail.go_to_cart_step1_page()
        #cartstep1.click_stroe_pick_up_tab()
        cartstep1.product_img.should(be.visible)
        with allure.step('購物車Step2，點擊全家button'): pass
        cartstep2 = cartstep1.click_checkout_button()
        #cartstep2.click_store_COD_tab()
        '''with allure.step('選擇全家超商取貨門市'): pass
        familystorepage=cartstep2.click_familystore_button()
        windows=browser.driver().window_handles
        browser.driver().switch_to.window(windows[-1])
        familystorepage.input_store_id()
        familystorepage.click_query_button()
        with allure.step('購物車Step2，點擊確認結帳'): pass
        familystorepage.click_submit_img()
        windows = browser.driver().window_handles
        browser.driver().switch_to.window(windows[0])'''
        with allure.step('購物車Step3，會出現感謝付款文案'): pass
        cartstep3 = cartstep2.click_checkout_button()
        cartstep3.text24.should(be.visible)

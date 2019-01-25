# -*- coding: utf-8 -*-
import allure ,pytest
from selene.api import *
from src.pages.familystore_page import FamilyStorePage

@allure.feature('頁面單元測試')
class TestFamilyStorePage:
    @allure.story('選擇全家頁面')
    def test_open_FamilyStorePage(self):
        browser.driver().get('http://fme.map.com.tw/default.asp')

    @allure.story('輸入全家store Id')
    def test_input_store_id(self):
        FamilyStorePage().input_store_id()

    @allure.story('點擊查詢店家按鈕')
    def test_click_query_button(self):
        FamilyStorePage().click_query_button()

    @allure.story('點擊重新查詢按鈕')
    def test_click_reload_button(self):
        FamilyStorePage().click_reload_img()
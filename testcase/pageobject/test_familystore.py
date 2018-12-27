# -*- coding: utf-8 -*-
from common import *
from src.pages.familystore_page import FamilyStorePage

class TestFamilyStorePage:

    def test_open_FamilyStorePage(self):
        browser.driver().get('http://fme.map.com.tw/default.asp')
    def test_input_store_id(self):
        FamilyStorePage().input_store_id()
    def test_click_query_button(self):
        FamilyStorePage().click_query_button()
    def test_click_submit_button(self):
        FamilyStorePage().click_reload_img()
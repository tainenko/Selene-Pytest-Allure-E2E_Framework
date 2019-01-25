# -*- coding: utf-8 -*-
import allure ,pytest
from selene.api import *
from src.pages.login_page import LoginPage
from src.pages.orderhistory_page import OrderHistoryPage

class TestOrderHistoryPage:

    @pytest.fixture(scope="module", autouse=True)
    def setup(self, variables):
        while (True):
            try:
                with allure.step('前置作業-會員登入'):
                    pass
                login = LoginPage().open_login_page()
                main_page = login.login_as(variables['user'], variables['password']).than_at_main_page()
                main_page.logontext.should(be.visible)
                break
            except:
                continue

    def test_contact_helper_btn_should_be_clickable(self):
        OrderHistoryPage().open_orderhistory_page()
        assert OrderHistoryPage().contacthelperbtn.should(be.clickable)
# -*- coding: utf-8 -*-
from common import *
from src.pages.helpercenter_page import HelperCenterPage
from src.pages.login_page import LoginPage

class TestHelperCenterPage:

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

    def test_open_helper_center_page(self):
        HelperCenterPage().open_helpcenter_url()
        assert browser.title()=='聯絡我們-東森購物'

    def test_nums_of_quetion_types(self):
        assert len(HelperCenterPage().quetiontypes)==11

    def test_submit_button_should_be_clickable(self):
        assert HelperCenterPage().submitbtn.should(be.clickable)

    def test_reset_input_should_be_clickable(self):
        assert HelperCenterPage().resetinput.should(be.clickable)

    def test_select_quetion_types_by_string(self):
        HelperCenterPage().select_quetion_type()

    def test_input_textarea_content(self):
        HelperCenterPage().input_textarea_content()



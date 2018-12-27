# -*- coding: utf-8 -*-
from common import *
from src.pages.page import BasePage
from src.pages.helpercenter_page import HelperCenterPage

class OrderHistoryPage(BasePage):

    def __init__(self):
        self.contact_helper_btn=s(by.text('請洽客服'))
        self.cancel_order_btn=s(by.text('我要取消'))

    def open_orderhistory_page(self,url="/OrderHistory"):
        browser.open_url(url)
        return self

    def click_contact_helper_btn(self):
        self.contact_helper_btn[0].click()
        return HelperCenterPage()

    def click_cancel_order_btn(self):
        self.cancel_ordel_btn.click()
        return self



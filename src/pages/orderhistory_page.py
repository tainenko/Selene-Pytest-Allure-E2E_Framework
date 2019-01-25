# -*- coding: utf-8 -*-
from selene.api import *
from src.pages.page import BasePage
from src.pages.helper_center_page import HelperCenterPage
from src.pages.cancel_page import CancelPage

class OrderHistoryPage(BasePage):

    def __init__(self):
        self.contacthelperbtn = s('a[title="請洽客服"]')
        self.cancelorderbtn=s('a.n-btn.n-btn--normal.btnReturn[title="我要取消"]')
        self.numoforder=ss('a.n-btn.n-btn--normal.btnReturn[title="我要取消"]')


    def open_orderhistory_page(self,url="/OrderHistory"):
        browser.open_url(url)
        return self

    def click_contact_helper_btn(self):
        self.contacthelperbtn.click()
        return HelperCenterPage()

    def click_cancel_order_btn(self):
        self.cancelorderbtn.click()
        return CancelPage()



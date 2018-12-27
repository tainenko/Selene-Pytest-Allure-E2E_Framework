# -*- coding: utf-8 -*-
from common import *
from src.pages.page import BasePage
from src.pages.cartstep3_page import CartStep3Page
from src.pages.familystore_page import FamilyStorePage

class CartStep2Page(BasePage):
    def __init__(self):
        self.atmtab=s(by.link_text('ATM'))
        self.CODtab = s(by.link_text('貨到付款'))
        self.storeCODtab=s(by.link_text('超商取貨付款'))
        self.familystore_btn =s('a#button-pickupFamilyStoreCVS') #全家
        self.checkoutbtn=s('button.n-btn.n-btn--primary') #確認付款

    def click_ATM_tab(self):
        self.atmtab.click()
        return self

    def click_COD_tab(self):
        self.CODtab.click()
        return self

    def click_checkout_button(self):
        self.checkoutbtn.click()
        return CartStep3Page()

    def click_familystore_button(self):
        self.familystore_btn.click()
        return FamilyStorePage()

    def click_store_COD_tab(self):
        self.storeCODtab.click()
        return self
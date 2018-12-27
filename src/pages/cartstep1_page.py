# -*- coding: utf-8 -*-
from common import *
from src.pages.page import BasePage
from src.pages.cartstep2_page import CartStep2Page

class CartStep1Page(BasePage):
    def __init__(self):
        self.deliveryTab=s('ul.n-tab.n-tab--lv2#deliverTab') #配送車tab
        self.normaldelivery=s("li#0") #一般宅配
        self.fastdelivery=s("li#3") #24小時快配
        self.faststorepickup=s("li#4") #快倉超取
        self.storepickup_tab=s('li#17') #超商取貨
        self.frozenstorepickup=s('li#18') #冷凍超取
        self.checkoutbtn=s(by.text('我要結帳')) #我要結帳

    def click_stroe_pick_up_tab(self):
        self.storepickup_tab.click()
        return self

    def click_checkout_button(self):
        self.checkoutbtn.click()
        return CartStep2Page()



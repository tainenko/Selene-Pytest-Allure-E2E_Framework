# -*- coding: utf-8 -*-
from common import *
from src.pages.page import BasePage

class CartStep3Page(BasePage):
    def __init__(self):
        self.text=s('div.n-l-colmb20.n-l-bgw-border.n-cart__finish.n-cart--hints') #待付款資訊
        self.text24=s('div.n-l-colmb20.n-l-bgw-border.n-cart__finish.n-cart--deliver-info') #訂單已成立

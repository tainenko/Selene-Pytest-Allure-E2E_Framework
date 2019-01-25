# -*- coding: utf-8 -*-
from selene.api import *
from src.pages.page import BasePage
#import src.pages.orderhistory_page
class CancelPage:
    def __init__(self):
        self.reason1_input=s('input#reason1.n-form--control') #重複訂購/已有類似商品
        self.textreason=s('textarea#txtReason.n-form--control.n-textarea--other') #請簡述原因
        self.submit_btn=s('input#CancelSubmit.n-btn.btn--primary.sendGA')

    def click_reason1_input(self):
        self.reason1_input.should(be.clickable)
        self.reason1_input.click()
        return self

    def input_text_reason(self,str='測試取消交易'):
        self.textreason.set_value(str)
        return self

    def click_submit_btn(self):
        self.submit_btn.click()
        return self

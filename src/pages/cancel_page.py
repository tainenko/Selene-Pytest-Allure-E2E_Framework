# -*- coding: utf-8 -*-
from common import *
from src.pages.page import BasePage

class CancelPage:
    def __init__(self):
        self.men-title=s(by.text('取消訂單'))
        self.reason1_input=s('input#reason1.n-form--control') #重複訂購/已有類似商品
        self.txtReason=s('textarea#txtReason.n-form--control.n-textarea--other') #請簡述原因
        self.submit_btn=s('input#CancelSubmit.n-btn.btn--primary.sendGA')

    def click_reason1_input(self):
        self.reason1_input.should(be.clickable)
        self.reason1_input.click()
        return self

    def input_text_Reson(self,str=''):
        self.txtReason.set_value(str)
        return self

    def click_submit_btn(self):
        self.submit_btn.click()
        return self

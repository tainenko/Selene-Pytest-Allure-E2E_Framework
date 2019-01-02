# -*- coding: utf-8 -*-
from common import *
from src.pages.page import BasePage
from selenium.webdriver.support.ui import Select

class HelperCenterPage(BasePage):
    def __init__(self):
        self.quetiontypeselect=s('select#selectedContactType.n-form--control') #問題種類
        self.quetiontypes=ss('select#selectedContactType>option')
        self.textareacommentinput=s('textarea#textarea-comment.n-form--control') #問題內容
        self.resetinput=s('input#btn-reset.n-btn.n-btn--normal') #重新填寫
        self.submitbtn=s('input.n-btn.n-btn--primary') #確定送出

    def open_helpcenter_url(self,url='/HelpCenter/Contact'):
        browser.open_url(url)
        return self

    def select_quetion_type(self,str='商品相關查詢'):
        Selector_Element=Select(self.quetiontypeselect)
        Selector_Element.select_by_visible_text(str)
        return self

    def input_textarea_content(self,str='測試聯絡我們，問題留言'):
        self.textareacommentinput.set_value(str)
        return self
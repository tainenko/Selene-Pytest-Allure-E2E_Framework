# -*- coding: utf-8 -*-
from selene.api import *
from src.pages.page import BasePage
#from src.pages.cartstep2_page import CartStep2Page

class FamilyStorePage(BasePage):
    def __init__(self):
        self.id_input=s('input') #服務代碼查詢
        self.query_button=s('input[value="查詢"]') #查詢
        self.submit_img=s('img#submit_img') #下一步
        self.reload_img=s('font.content-12') #重新選擇
        self.newmap_iframe = s('iframe#new_map')

    def click_query_button(self):
        self.query_button.click()
        return self

    def input_store_id(self,id=16552):
        self.id_input.set_value(id)
        return self

    def click_submit_img(self):
        newmap = browser.driver().find_element_by_css_selector('iframe#new_map')
        browser.driver().switch_to.frame(newmap)
        self.submit_img.click()

    def click_reload_img(self):
        newmap=browser.driver().find_element_by_css_selector('iframe#new_map')
        browser.driver().switch_to.frame(newmap)
        self.reload_img.click()
        return self
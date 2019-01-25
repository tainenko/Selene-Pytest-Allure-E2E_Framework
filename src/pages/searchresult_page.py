# -*- coding: utf-8 -*-
from selene.api import *
from src.pages.page import BasePage

class SearchResultPage(BasePage):
    def __init__(self):
        self.items=ss("div.n-card__box")
        self.noresult=s("p.n-title--16.n-search__without-result") #搜尋無結果文案

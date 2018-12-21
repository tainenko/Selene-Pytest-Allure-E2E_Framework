from common import *
from src.pages.page import BasePage
from src.pages.main_page import MainPage

class SearchResultPage(BasePage):
    def __init__(self):
        self.items=ss("div.n-card__box")

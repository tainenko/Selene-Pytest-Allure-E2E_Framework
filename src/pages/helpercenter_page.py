# -*- coding: utf-8 -*-
from common import *
from src.pages.page import BasePage

class HelperCenterPage(BasePage):
    def __init__(self):
        self.quetion_type_select=s('select.n-form--control')
# -*- coding: utf-8 -*-
from common import *
from src.pages.main_page import MainPage
from src.pages.searchresult_page import SearchResultPage

@allure.feature('搜尋功能')
@pytest.mark.incremental
class TestSearchResult(object):
    @allure.story('搜尋結果')
    def test_search_result_must_have_values(self, variables):
        keyword = variables['keyword']
        with allure.step("開啟首頁"): pass
        mainpage=MainPage().open()
        with allure.step("輸入關鍵字:"+keyword):pass
        mainpage.input_search_keywork(keyword)
        with allure.step("點擊搜尋"):pass
        searchresultpage=mainpage.click_search24_button()
        with allure.step("搜尋列表非空值"):pass
        assert len(searchresultpage.items)>0

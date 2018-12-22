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
        with allure.step("關閉CrazyAD"):pass
        mainpage.close_crazy_banner()
        with allure.step("輸入關鍵字:"+keyword):pass
        mainpage.input_search_keyword(keyword)
        with allure.step("點擊搜尋"):pass
        searchresultpage=mainpage.click_search_button()
        with allure.step("搜尋列表非空值"):pass
        assert searchresultpage.items[0].should(be.clickable)
        assert searchresultpage.items[0].should(be.visible)
        assert len(searchresultpage.items) >0

    @allure.story('搜尋無結果')
    def test_search_result_pages_with_noresult(self, variables):
        noresult = variables['noresult']
        with allure.step("開啟首頁"): pass
        mainpage=MainPage().open()
        with allure.step("關閉CrazyAD"):pass
        mainpage.close_crazy_banner()
        with allure.step("輸入關鍵字:"+noresult):pass
        mainpage.input_search_keyword(noresult)
        with allure.step("點擊搜尋"):pass
        searchresultpage=mainpage.click_search_button()
        with allure.step("顯示搜尋無結果文案"):pass
        assert searchresultpage.noresult.should(be.visible)

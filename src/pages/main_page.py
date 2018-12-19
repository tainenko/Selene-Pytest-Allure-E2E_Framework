# -*- coding: utf-8 -*-
from common import *
from src.pages.page import BasePage

class MainPage(BasePage):
    def __init__(self):
        self.loginbtn = s("a.sendGA[href='/Login?url=%2F']")
        self.logoutbtn = s("a.sendGA[href='/Logout?url=/']")
        self.h2Title = s("div.n-title--16")                        # h2Title全站商品分類
        self.mainNavList = ss("#mainNav>li")                       # 商品分類
        self.FiveBanner = s("div#FiveBanner")                      # FiveBanner
        self.FiveBannerbnNav = s("ul#bnNav")                       # FiveBanner
        self.superBanner = s("div#mainBanner.n-banner")
        self.memberInfoModule = s("div.n-mem-info__wrap")
        self.dailySale=s(".n-left.n-daily__wrap.n-daily__clock + .n-left.n-daily__wrap.n-daily__day")
        self.dailyDayClockSale = s("div.n-left.n-hover--img.n-m-right--md")# 整點和天天
        self.liveProduct = s("section.n-film__wrap")               # 影音專區
        self.channelTab = ss("#filmTab>li")                        # 影音頻道tab
        self.ranAll = s("div#HomeChannelPush")                     # 熱銷排行榜
        self.storeSection = s("#HomeStoreChannel")                 # 頻道推薦
        self.storeSectionList = ss("#HomeStoreChannel>div>section")# 16館商品
        self.storeProductList = ss(".n-category__list.n-left>li")  # 16館商品列表，總共106個商品
        self.bankBanner = s("section#_indexBank.n-m-bottom--sm")   # 銀行活動
        self.recommendProducts = s("#RecommendProducts")           # 你可能會喜歡All
        self.recommendProductsList = ss(".n-ulike__list.n-hover--img>li")# 你可能會喜歡 - 商品列表
        self.bestProducts = s("div#homeHotPdList")                 # 更多精選商品
        self.crazyBannerCloseBtn = s("a#cBtnClose")
        self.logontext = s("div#logon>ul>li>span")
        self.registerBtn = s("a.sendGA[href='/Register?url=%2F']")

    def open(self,url='/'):
        browser.open_url(url)
        return self
    def close_crazy_banner(self):
        try:
            self.crazyBannerCloseBtn.should(be.clickable)
            self.crazyBannerCloseBtn.click()
            return self
        except:
            return self

    def go_to_login_page(self):
        self.loginbtn.click()
        return LoginPage()



    def log_out(self):
        self.logoutbtn.click()
        return self



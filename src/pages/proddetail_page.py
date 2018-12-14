# -*- coding: utf-8 -*-
from common_imports import *

from src.pages.page import BasePage
from src.pages.cartstep1_page import CartStep1Page

class ProductDetailPage(BasePage):
    def __init__(self):
        self.productImage=s('img.product-image')#商品圖
        self.lable=s('span.n-labels.n-bg--se-lighter')#屬性label
        self.addtowishlist=s('a.n-btn>i.n-icon--collect')#加入收藏
        self.delivery=ss('li.n-form--radio')#配送方式
        self.styleSelectror=s('select#styleSelector.n-form--control ')#選擇規格
        self.subStyleSelectror = s('select#subStyleSelector.n-form--control ')  # 選擇樣式
        self.quantitySelector=s('select#quantitySelector.n-form--control ')#選擇數量
        self.goToCheckout=s('button#goToCheckout')#立即結帳
        self.addToCart=s('a.n-btn.n-btn--lv2[data-action="ProdDetail_UpPurchaseInfo_AddToCart"]')#加入購物車
        self.alertinfor=s('p.mfp-alertInfo')#alert您已經成功加入購物車
        self.alertGotoCart=s('a.n-btn.n-btn--primary')#alert立即結帳
        self.alertBackToShopping=s('a.n-btn n-btn--lv3')#alert繼續購物
        self.soldout=s('a.n-btn.n-btn--disabled[title="銷售一空"]')#銷售一空
        self.arrivalNotice=s('a.n-btn.n-btn--normal[data-action="ProdDetail_UpPurchaseInfo_ArrivalNotice"]')#貨到通知

    def open_proddetail_page(self,goodid='1990867'):
        browser.open_url('/i/'+goodid)
        return self

    def click_add_to_wishlist(self):
        self.addtowishlist.click()
        return self

    def click_add_to_cart(self):
        self.addToCart.click()
        return self

    def click_go_to_checkout(self):
        self.goToCheckout.click()
        return self


    def get_normal_delivery_goodid(self):
        return '1990867'
    def get_fast_delivery_goodid(self):
        return '1942437'
    def get_fast_store_pick_up_goodid(self):
        return '2111897'
    def get_store_pick_up_goodid(self):
        return '5937027'
    def get_frozen_store_pick_up_goodid(self):
        return '1989568'


    def than(self):
        return self

    def go_to_cart_step1_page(self):
        return CartStep1Page()


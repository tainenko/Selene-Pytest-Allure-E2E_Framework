# -*- coding: utf-8 -*-
from common_imports import *

from src.pages.page import BasePage

class ProductPage(BasePage):
    def __init__(self):
        self.productImage=s('img.product-image')#商品圖
        self.lable=s('span.n-labels.n-bg--se-lighter')屬性label
        self.collect=s('i.n-icon--collect')#我的收藏
        self.delivery=ss('li.n-form--radio')#配送方式
        self.styleSelectror=s('select#styleSelector.n-form--control ')#選擇規格
        self.subStyleSelectror = s('select#subStyleSelector.n-form--control ')  # 選擇樣式
        self.quantitySelector=s('select#quantitySelector.n-form--control ')#選擇數量
        self.goToCheckout=s('button#goToCheckout.n-btn.n-btn--primary')#立即結帳
        self.addToCart=s('a.n-btn.n-btn--lv2[data-action="ProdDetail_UpPurchaseInfo_AddToCart"]')#加入購物車
        self.alertinfor=s('p.mfp-alertInfo')#alert您已經成功加入購物車
        self.alertGotoCart=s('a.n-btn.n-btn--primary')#alert立即結帳
        self.alertBackToShopping=s('a.n-btn n-btn--lv3')#alert繼續購物
        self.soldout=s('a.n-btn.n-btn--disabled[title="銷售一空"]')#銷售一空
        self.arrivalNotice=s('a.n-btn.n-btn--normal[data-action="ProdDetail_UpPurchaseInfo_ArrivalNotice"]')#貨到通知



# -*- coding: utf-8 -*-
from selene import browser
from selene.support.jquery_style_selectors import s

from src.pages.page import BasePage
from src.pages.main_page import MainPage

class LoginPage(BasePage):
    def __init__(self):
        self.username_input =s("input#loginID.n-form--control")   # 手機Email身分證字號
        self.password_input =s("input#password.n-form--control")  # 密碼
        self.loginBtn =s("button#login.n-btn.sendGA")             # 登入Btn
        self.verifySN_input =s("input#validCode.n-form--control") # 驗證碼
        self.loginTitle =s("div.n-title--18.n-m-bottom--xs.n-text--center")# Title:會員登入
        self.loginDescription =s("label.n-form--title")           # 手機Email身分字號三擇一
        self.loginIDLabel =s("span#loginID-error")                # 請輸入手機Email身分證字號
        self.passwordLabel =s("span#password-error")              # 請輸入密碼
        self.forgotIDPW =s("a#forgot.n-blue--link.sendGA")        # 忘記帳號密碼
        self.registerBtn =s("a#register.n-normal--link.sendGA")   # 免費註冊
        self.chinaLoginBtn =s(("a#ChLogin.n-normal--link.sendGA"))# 大陸會員登入
        self.tvMemberBtn =s("a.n-btn.n-btn--lv2[href='/Register/Cross?url=%2F']")# 電視會員登入
        self.logionFBbtn =s("button#Facebook")                    # FB登入btn
        self.verifyCodeImg =s("#CheckPWDIMG")                     # 驗證碼圖片
        self.validationErr =s("span.field-validation-error")      # 驗證碼錯誤訊息
        self.errors =s("div.validation-summary-errors>ul>li")

    def open_login_page(self,url='/Login'):
        browser.open_url(url)
        return self

    def login_as(self,user,passward):
        self.username_input.set_value(user)
        self.password_input.set_value(passward)
        verifycode=self.verifyCodeImg.screenshot()
        self.verifySN_input.set_value(verifycode)
        self.loginBtn.click()
        return self

    def login_with_invalid_verifySN(self,user,passward,verifySN):
        self.username_input.set_value(user)
        self.password_input.set_value(passward)
        self.verifySN_input.set_value(verifySN)
        self.loginBtn.click()
        return self

    def than(self):
        return self

    def than_at_main_page(self):
        return MainPage()





from selene.support.jquery_style_selectors import s
from selene.support.jquery_style_selectors import ss

from src.pages.page import BasePage
from src.pages.main_page import MainPage

class LoginPage(BasePage):
    def __init__(self):

        self.username_input =$("input#loginID.n-form--control")# 手機Email身分證字號
        self.password_input =$("input#password.n-form--control")# 密碼
        self.loginBtn =$("button#login.n-btn.sendGA")# 登入Btn
        self.verifySN_input =$("input#validCode.n-form--control")# 驗證碼
        self.loginTitle =$("div.n-title--18.n-m-bottom--xs.n-text--center")# Title:會員登入
        self.loginDescription =$("label.n-form--title")# 手機Email身分字號三擇一
        self.loginIDLabel =$("span#loginID-error")# 請輸入手機Email身分證字號
        self.passwordLabel =$("span#password-error")# 請輸入密碼
        self.forgotIDPW =$("a#forgot.n-blue--link.sendGA")# 忘記帳號密碼
        self.registerBtn =$("a#register.n-normal--link.sendGA")# 免費註冊
        self.chinaLoginBtn =$(("a#ChLogin.n-normal--link.sendGA"))# 大陸會員登入
        self.tvMemberBtn =$("a.n-btn.n-btn--lv2[href='/Register/Cross?url=%2F']")# 電視會員登入
        self.logionFBbtn =$("button#Facebook")# FB登入btn
        self.verifyCodeImg =$("#CheckPWDIMG")# 驗證碼圖片
        self.validationErr =$("span#validCode-error")# 驗證碼錯誤訊息
        self.errors =$("div.validation-summary-errors>ul>li")

    def open_login_page(self,url='/Login'):
        browser.open_url(url)
        return self
    
    def login_as(self,user,passward):
        self.username_input.set(user)
        self.password_input.set(passward)
        verifycode=self.verifyCodeImg.screenshot()
        self.verifySN_input.set(cerifycode)
        self.loginBtn.click()
        return MainPage()

    def login_with_invalid_verifySN(self,user,passward):
        self.username_input.set(user)
        self.password_input.set(passward)
        verifycode = self.verifyCodeImg.screenshot()
        self.verifySN_input.set(cerifycode)
        self.loginBtn.click()
        return self





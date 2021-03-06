# -*- coding: utf-8 -*-
from selene.api import *
from src.pages.page import BasePage
from src.pages.main_page import MainPage
from aip import AipOcr
import re
from PIL import Image
import pytesseract

class LoginPage(BasePage):
    def __init__(self):
        self.username_input =s("input#loginID.n-form--control") #手機Email身分證字號
        self.password_input =s("input#password.n-form--control") #密碼
        self.loginBtn =s("button#login.n-btn.sendGAWithoutCancelBubble") #登入Btn
        self.verifySN_input =s("input#validCode.n-form--control") # 驗證碼
        self.loginTitle =s("div.n-title--18.n-m-bottom--xs.n-text--center") #Title:會員登入
        self.loginDescription =s("label.n-form--title") #手機Email身分字號三擇一
        self.loginIDLabel =s("span#loginID-error") #請輸入手機Email身分證字號
        self.passwordLabel =s("span#password-error") #請輸入密碼
        self.forgotIDPW =s("a#forgot.n-blue--link.sendGA") #忘記帳號密碼
        self.registerBtn =s("a#register.n-normal--link.sendGA") #免費註冊
        self.chinaLoginBtn =s(("a#ChLogin.n-normal--link.sendGA")) #大陸會員登入
        self.tvMemberBtn =s("a.n-btn.n-btn--lv2[href='/Register/Cross?url=%2F']") #電視會員登入
        self.logionFBbtn =s("button#Facebook") #FB登入btn
        self.verifyCodeImg =s("#CheckPWDIMG") #驗證碼圖片
        self.validationErr =s("span.field-validation-error") #驗證碼錯誤訊息
        self.errors =s("div.validation-summary-errors>ul>li")
        self.verifyImgurl = "/Product/CreateCaptcha?count=1" #CaptchaImage url

    def open_login_page(self,url="/Login"):
        browser.open_url(url)
        return self

    '''def setup_login(self):
        while (True):
            try:
                with allure.step('前置作業-會員登入'):pass
                loginpage = self.open_login_page()
                mainpage = loginpage.login_as(variables['user'], variables['password']).than_at_main_page()
                mainpage.logontext.should(be.visible)
                break
            except:
                continue'''

    def login_with_invalid_verifySN(self,user,passward,verifySN):
        self.username_input.set_value(user)
        self.password_input.set_value(passward)
        self.verifySN_input.set_value(verifySN)
        self.loginBtn.click()
        return self

    def get_verify_code_with_baidu_ocr(self):
        '''
        DOC:https://cloud.baidu.com/doc/OCR/OCR-Python-SDK.html#.E9.85.8D.E7.BD.AEAipOcr
        APP_ID = '你的 App ID'
        API_KEY = '你的 Api Key'
        SECRET_KEY = '你的 Secret Key'
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        返回格式範例：
        {
        "log_id": 2471272194,
        "words_result_num": 2,
        "words_result":
            [
            {"words": " TSINGTAO"},
            {"words": "青島睥酒"}
            ]
        }
        :return:
        '''
        #create baidu-aip ocr client
        APP_ID=""
        API_KEY=""
        SECRET_KEY=""
        client=AipOcr(APP_ID,API_KEY,SECRET_KEY)
        #read screenshot imgae of verifyImg
        image=open('temp/verifySN.png','rb').read()
        #get image Ocr result
        result = client.basicGeneral(image)['words_result'][0]['words']
        return re.sub("[^0-9]", "", result)

    def get_verify_code_with_tesseract(self):
        '''
        PILLOW對驗証碼圖片進行灰度化、二值化及去閥值除干擾線
        pytesseract對處理完的圖片進行ocr
        :return: string
        '''
        img=Image.open('./temp/verifySN.png')
        img_gray=img.convert('L') #灰度化
        img_two=img_gray.point(lambda x:255 if x >150 else 0) #二值化並去閥值
        #img_two.save('./temp/temp.png')
        res = pytesseract.image_to_string(img_two,config="-c tessedit_char_whitelist=0123456789 -psm 6") #tesseract-ocr辨識並設定白名單為數字
        return res


    def get_verifyImg_screen_shot(self,seleneElement):
        '''
        定位驗証碼圖片位置，截全屏圖後裁切，只留WebElement的部份
        :param seleneElement:
        :return:
        '''
        #seleneElement.get_screenshot_as_file("./temp/verifySN.png")
        browser.driver().get_screenshot_as_file("./temp/verifySN.png") #截全屏圖
        location = seleneElement.location #獲得該WebElement位置
        size = seleneElement.size #獲得該WebElement大小
        img = Image.open("./temp/verifySN.png")
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        img = img.crop((int(left), int(top), int(right), int(bottom))) #將全屏圖截切，只留WebElement的部分
        img.resize((size['width'] * 2, size['height'] * 2), Image.BILINEAR) #圖片放大2倍
        img.save('./temp/temp.png')
        return self

    def login_as(self,user,passward):
        verifycode=self.get_verify_code_str()
        self.verifySN_input.set_value(verifycode)
        self.username_input.set_value(user)
        self.password_input.set_value(passward)
        self.loginBtn.click()
        return self

    def get_verify_code_str(self):
        browser.open_url(self.verifyImgurl)
        browser.driver().get_screenshot_as_file("./temp/verifySN.png")
        browser.driver().back()
        return self.get_verify_code_with_baidu_ocr()

    def than(self):
        return self

    def than_at_main_page(self):
        return MainPage()





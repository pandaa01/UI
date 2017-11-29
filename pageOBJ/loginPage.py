#!/usr/bin/env python
#-*-coding:utf-8-*-
from selenium.webdriver.common.by import By
from webUI.basePage.webDri import *

class login(webDri):

    loginlink_loc=(By.LINK_TEXT,u'登录')
    username_loc = (By.ID, 'TANGRAM__PSP_10__userName')
    password_loc = (By.ID, 'TANGRAM__PSP_10__password')
    loginButton_loc = (By.ID, 'TANGRAM__PSP_10__submit')
    error_loc = (By.ID, 'TANGRAM__PSP_10__error')

    def clickLogin(self):
        self.findelement(*self.loginlink_loc).click()

    def typeUsername(self, username):
        self.findelement(*self.username_loc).send_keys(username)

    def typePassword(self, password):
        self.findelement(*self.password_loc).send_keys(password)

    def clickLoginButton(self):
        self.findelement(*self.loginButton_loc).click()

    def login(self, username, password):
        self.clickLogin()
        self.typeUsername(username)
        self.typePassword(password)
        self.clickLoginButton()

    @property
    def getError(self):
        return self.findelement(*self.error_loc).text



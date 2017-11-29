#!/usr/bin/env python
#-*-coding:utf-8-*-

from selenium import webdriver
from webDDT.pageOBJ.init import *
from webDDT.pageOBJ.loginPage import *

import unittest
class loginTest(init,login):

   def test01(self):
       '''验证账户密码为空时，提示信息是否正确'''
       self.clickLogin()
       self.typeUsername('')
       self.typePassword('')
       self.clickLoginButton()
       self.assertEqual(self.getError,u'请您输入手机/邮箱/用户名')

   def test02(self):
       '''验证密码为空时，提示信息是否正确'''
       self.login('18291875606','')
       self.assertEqual(self.getError,u'请您输入密码')





if __name__=='__main__':
    unittest.main(verbosity=2)



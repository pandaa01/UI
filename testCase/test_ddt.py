#!/usr/bin/env python
#-*-coding:utf-8-*-

import unittest
import os,sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)),'basePage/webDri.py'))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)),'baseOBJ/init.py'))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)),'baseOBJ/loginPage.py'))
from pageOBJ.init import *
from webUI.pageOBJ.loginPage import *
from ddt import *
from webDDT.untis import helper

@ddt
class loginDdt(init,login):
    @data(('','',u'请您输入手机/邮箱/用户名'),('18291875606','',u'请您输入密码'),('18291875606','123456',u'请您输入验证码'))
    @unpack
    def test_all(self,name,pw,error):
        self.login(name,pw)
        self.assertEqual(self.getError,error)








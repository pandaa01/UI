#!/usr/bin/env python
#-*-coding:utf-8-*-
from selenium.common.exceptions import NoSuchElementException
import time

class webDri():

    def driver(self,driver):
        self.driver=driver


    def findelement(self,*loc):
        try:
            return self.driver.find_element(*loc)
        except NoSuchElementException as e:
            print 'error details is %s'%(e.args[0])

    def findelements(self,*loc):
        try:
            return self.driver.find_elements(*loc)
        except NoSuchElementException as e:
            print 'error details is %s'%(e.args[0])



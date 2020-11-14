# -*- coding: utf-8 -*-
"""
@Time ： 2020/9/22 21:18
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：PO设计模式
"""
import time
from selenium import webdriver
import pytest
from web.webkeys import webkeys
from _pytest.python import Function
from ddt.params import datas
from ctypes.test.test_array_in_pointer import Value
import allure
from _ast import With


@allure.feature('电商项目web自动化')
class test_Comm:
    """
    电商项目PO封装
    """
    def setup_class(self):
        """
        构造函数，创建对象的时候会执行
        初始化浏览器
        """
        self.web = webkeys()
        # 隐式等待
        # 每隔一秒钟找一次元素，如果找到了就继续运行
        # 如果超过10s还没找到，那么就是no such element
        self.web.openbroser()

    @allure.story('登录')
    @pytest.mark.parametrize('listcases',datas['loginPage'])
    def test_login(self,listcases):
        """
        登录成功的用例
        :return: None
        """
        try:
            allure.dynamic.title(listcases['title'])
            allure.description(listcases['description'])
        except Exception as e:
            pass
        
        testcases = listcases['cases']
        for cases in testcases:
            listcases = list(cases.values())
            
            with allure.step(listcases[0]):
                func = getattr(self.web, listcases[1])
                values = listcases[2:]
                func(*values)
                
    def teardown_class(self):
        self.web.quit()
            

    
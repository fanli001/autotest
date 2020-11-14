# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/4 16:05
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：allure测试报告生成
"""
import pytest
import allure
import os


@allure.story('手机加入购物车')  #表示用例名称
@allure.severity(allure.severity_level.CRITICAL)  #用例级别
@allure.description('该用例用于测试是否能成功添加【手机】到购物车')
@allure.step("字符串相加  {}".format('0099')) #添加步骤，可以用于显示传入的参数   
def test_cart():
    """将手机加入购物车"""
    with allure.step('添加购物车步骤1~~~~~~~~~~'):  #表示用例步骤
        print("添加购物车1")

@allure.story('电脑加入购物车')
@allure.severity(allure.severity_level.MINOR)
@allure.description('该用例用于测试是否能成功添加【电脑】到购物车')   
def test_cart1():
    """将电脑加入购物车"""
    with allure.step('添加购物车步骤2~~~~~~~~~~'):  #表示用例步骤
        print("添加购物车2")
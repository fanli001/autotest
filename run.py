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
from ddt.params import datas

print(datas)

if __name__ == "__main__":
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(['ddt/commerce_test.py','--alluredir', 'target/allure-results'])
    #执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
#     os.system('allure generate ./temp -o ./report --clean')
#     os.system('allure generate ./temp -o ./report --clean')

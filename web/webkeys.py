# -*- coding: utf-8 -*-
"""
@Time ： 2020/9/22 21:18
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：PO设计模式
"""
import time
from selenium import webdriver


class webkeys:
    """
    电商项目PO封装
    """
    def openbroser(self):
        """
        构造函数，创建对象的时候会执行
        初始化浏览器
        """
        self.driver = webdriver.Chrome()
        # 隐式等待
        # 每隔一秒钟找一次元素，如果找到了就继续运行
        # 如果超过10s还没找到，那么就是no such element
        self.driver.implicitly_wait(10)

#     def login(self):
#         """
#         登录成功的用例
#         :return: None
#         """
#         # 打开网站
#         self.driver.get('http://testingedu.com.cn:8000/index.php/Home/user/login.html')
# 
#         # 找到用户名输入框
#         self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('13800138006')
#         # 输入密码
#         self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
#         # 输入验证码
#         self.driver.find_element_by_xpath('//*[@id="verify_code"]').send_keys('1111')
#         # 点击登录
#         self.driver.find_element_by_xpath('//a[contains(text(),"登")]').click()
        
        
    def geturl(self,url):
        self.driver.get(url)
        
    def input(self,locator,value):
#         self.driver.find_element_by_xpath(locator).click()
#         time.sleep(1)
        self.driver.find_element_by_xpath(locator).send_keys(value)
        time.sleep(1)
        
    def click(self,locator):
        self.driver.find_element_by_xpath(locator).click()
        time.sleep(1)
        
    def sleep(self,t=1):
        time.sleep(t)
        
    def quit(self):
        self.driver.quit()

#     def Userinfo(self):
#         """
#         需要先调用登录成功的用例
#         :return:
#         """
#         # 固定等待，等页面加载完成
#         time.sleep(1)
#         self.driver.get('http://testingedu.com.cn:8000/index.php/Home/User/info.html')
#         # 点击头像图片
#         self.driver.find_element_by_xpath('//*[@id="preview"]').click()
#         # 进入iframe
#         self.driver.switch_to.frame(
#             self.driver.find_element_by_xpath('//*[@id="layui-layer-iframe1"]'))
#         # 上传图片
#         # 怎么转为相对路径？
#         self.driver.find_element_by_xpath('//*[@id="filePicker"]/div[2]/input')\
#             .send_keys('E:\software\Python\pytest_camp\lib\images\q-icon.png')
#         # 点击确定使用
#         self.driver.find_element_by_xpath('//*[@id="uploader"]/div[1]/div[3]/div[3]').click()
# 
#     def search(self):
#         """
#         依赖登录
#         :return:
#         """
#         time.sleep(1)
#         self.driver.get('http://testingedu.com.cn:8000/index.php/Home/user/index.html')
#         # 输入手机
#         self.driver.find_element_by_xpath('//*[@id="q"]').send_keys('手机')
#         # 点击搜索
#         self.driver.find_element_by_xpath('//*[@id="sourch_form"]/a').click()


# if __name__ == "__main__":
#     comm = Comm()
#     # 登录用例
#     comm.login()
#     # 搜索
#     comm.search()
#     # 上传头像
#     comm.Userinfo()
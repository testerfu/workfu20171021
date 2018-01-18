#coding=utf-8
from selenium import webdriver
import time

#测试cnode网站的注册功能
#打开网站
driver=webdriver.Chrome(executable_path='./chromedriver.exe')
url='http://118.31.19.120:3000/'
driver.get(url)
#进入注册页面
reg_pageXpath='/html/body/div[1]/div/div/ul/li[5]/a'
reg_page=driver.find_element_by_xpath(reg_pageXpath)
reg_page.click()

#输入信息注册
#定义Xpath
usernameXpath='//*[@id="loginname"]'
pwdXpath='//*[@id="pass"]'
pwdConfXpath='//*[@id="re_pass"]'
emailXpath='//*[@id="email"]'
registerXpath='//*[@id="signup_form"]/div[5]/input'

#定义输入参数
username='12345'
pwd='12345'
pwdConf='12345'
email='12345@12345.com'

usernameInput=driver.find_element_by_xpath(usernameXpath)
usernameInput.send_keys(username)
pwdInput=driver.find_element_by_xpath(pwdXpath)
pwdInput.send_keys(pwd)
pwdConfInput=driver.find_element_by_xpath(pwdConfXpath)
pwdConfInput.send_keys(pwdConf)
emailInput=driver.find_element_by_xpath(emailXpath)
emailInput.send_keys(email)
register=driver.find_element_by_xpath(registerXpath)
register.click()

#关闭浏览器
time.sleep(3)
driver.quit()
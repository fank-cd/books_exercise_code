# coding:utf-8

from selenium import webdriver
from time import sleep

browser = webdriver.Firefox(executable_path="E:\\geckodriver.exe")

# browser.find_element_by_xpath().send_keys()
#browser.quit()
# selenium完成微博模拟登录
browser.get("https://weibo.com/login.php")
print(browser.page_source)
sleep(10)
#browser.find_element_by_id("loginname").send_keys("18684028609")
browser.find_element_by_xpath(".//input[@id='loginname']").send_keys("18684028609")
browser.find_element_by_xpath(".//div[@class='info_list password']/div/input[@class='W_input']").send_keys("Cdkc201301")
browser.find_element_by_xpath(".//div[@class='info_list login_btn']/a[@node-type='submitBtn']").click()
sleep(5)
for i in range(3):
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage")
    sleep(3)
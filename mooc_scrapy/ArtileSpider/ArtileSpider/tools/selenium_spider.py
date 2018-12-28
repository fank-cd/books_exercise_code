# coding:utf-8

from selenium import webdriver


browser = webdriver.Firefox(executable_path="E:\\geckodriver.exe")

browser.get("http://www.baidu.com")

print(browser.page_source)


# browser.find_element_by_xpath().send_keys()
browser.quit()
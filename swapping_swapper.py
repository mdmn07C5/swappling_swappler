from selenium import webdriver
from selenium.webdriver import firefox
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


def login_and_Navigate(driver, base_url, username, password):
	driver.get(base_url + "/oam/Portal_Login1.html")
	login_button = driver.find_element_by_xpath("//*[@id=\"crefli_HC_SSS_STUDENT_CENTER\"]")


	driver.find_element_by_id("cf-login").clear()
	driver.find_element_by_id("password").clear()
	driver.find_element_by_id("cf-login").send_keys(username)
	driver.find_element_by_id("password").send_keys(password)
	login_button.click()

	#Go to Student Center
	driver.get(base_url + "/psp/cnyepprd/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL?FolderPath=PORTAL_ROOT_OBJECT.HC_SSS_STUDENT_CENTER&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder")
	enroll_button = driver.find_element_by_id("DERIVED_SSS_SCR_SSS_LINK_ANCHOR3")
	enroll_button.click()


def swap(driver, base_url):
	swap_button = driver.find_element_by_link_text("swap")
	select_button = driver.find_element_by_xpath("//*[@id=\"DERIVED_REGFRM1_SSR_PB_ADDTOLIST1$184$\"]")
	finish_swapping_button = driver.find_element_by_xpath("//*[@id=\"DERIVED_REGFRM1_SSR_PB_SUBMIT\"]")
	get_error = True

	while get_error:		
		swap_button.click()

		#Swap this Class: Select form your schedule
		class_from_sched = driver.find_element_by_xpath("//*[@id=\"DERIVED_REGFRM1_DESCR50$225$\"]")
		#With this Class: Select form Shopping Cart
		class_from_cart = driver.find_element_by_xpath("//*[@id=\"DERIVED_REGFRM1_DESCR50$225$\"]")
		
		Select(class_from_sched).select_by_value("8172")
		Select(class_from_cart).select_by_value("8170")

		select_button.click()

		#wait for finish_swapping_button
		while ~(finish_swapping_button.is_displayed()):
			time.sleep(1)
		else: finish_swapping_button.click()

		message_window = driver.find_element_by_xpath("//*[@id=\"win0divDERIVED_REGFRM1_SS_MESSAGE_LONG$0\"]")

		while ~(message_window.is_displayed()):
			time.sleep(1)
		else: 
			if assertRegexpMatches(message_window.text, r"Error"):
			#other enroll button at top of Enrollment:Add classes menu
				driver.find_element_by_link_text("Enroll").click()
			else: get_error = True	


if __name__ == '__main__':
	username = "Username"
	password = "Assword"
	base_url = "https://home.cunyfirst.cuny.edu/psp/cnyepprd/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL?FolderPath=PORTAL_ROOT_OBJECT.HC_SSS_STUDENT_CENTER&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder"	
	
	#firefox_capabilities = DesiredCapabilities.FIREFOX
	#firefox_capabilities['marionette'] = True

	#driver = webdriver.Firefox(capabilities=firefox_capabilities)
	driver = webdriver.Firefox()
	driver.implicitly_wait(30)

#login using username and password and navigate to enrollment page
login_and_Navigate(driver, base_url, username, password)
#swap until she can't swap no more
swap(driver, base_url)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re
import sys

def login(driver, base_url, username, password):
	driver.get(base_url + "/oam/Portal_Login1.html")
	login_button = driver.find_element_by_name("submit")

	driver.find_element_by_id("cf-login").clear()
	driver.find_element_by_id("password").clear()
	driver.find_element_by_id("cf-login").send_keys(username)
	driver.find_element_by_id("password").send_keys(password)
	login_button.click()


def navigate_to_enrollment(driver, base_url):
	#Go to Student Center
	driver.get(base_url + "/psp/cnyepprd/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL?FolderPath=PORTAL_ROOT_OBJECT.HC_SSS_STUDENT_CENTER&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder")
	#driver.switch_to_frame("ptnav2framebody")
	#driver.switch_to_frame("apple-mobile-web-app-capable")
	
	#monstrsity, temporary while we figure out cunyfirst's seekrits
	driver.get("https://hrsa.cunyfirst.cuny.edu/psc/cnyhcprd/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL?FolderPath=PORTAL_ROOT_OBJECT.HC_SSS_STUDENT_CENTER&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder/psp/cnyepprd/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL?FolderPath=PORTAL_ROOT_OBJECT.HC_SSS_STUDENT_CENTER&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder&PortalActualURL=https%3a%2f%2fhrsa.cunyfirst.cuny.edu%2fpsc%2fcnyhcprd%2fEMPLOYEE%2fHRMS%2fc%2fSA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL%3f%26IsFolder%3dfalse%26IgnoreParamTempl%3dFolderPath%252cIsFolder&PortalContentURL=https%3a%2f%2fhrsa.cunyfirst.cuny.edu%2fpsc%2fcnyhcprd%2fEMPLOYEE%2fHRMS%2fc%2fSA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL&PortalContentProvider=HRMS&PortalCRefLabel=Student%20Center&PortalRegistryName=EMPLOYEE&PortalServletURI=https%3a%2f%2fhome.cunyfirst.cuny.edu%2fpsp%2fcnyepprd%2f&PortalURI=https%3a%2f%2fhome.cunyfirst.cuny.edu%2fpsc%2fcnyepprd%2f&PortalHostNode=EMPL&NoCrumbs=yes&PortalKeyStruct=yes")
	enroll_button = driver.find_element_by_link_text("Enroll")
	enroll_button.click()


def swap(driver, base_url):
	
	get_error = True

	while get_error:
		swap_button = driver.find_element_by_link_text("swap")		
		swap_button.click()

		select_button = driver.find_element_by_xpath("//*[@id=\"DERIVED_REGFRM1_SSR_PB_ADDTOLIST1$184$\"]")

		#Swap this Class: Select from your schedule
		class_from_sched = driver.find_element_by_xpath("//*[@id=\"DERIVED_REGFRM1_DESCR50$225$\"]")
		#with this Class: Select form Shopping Cart
		class_from_cart = driver.find_element_by_xpath("//*[@id=\"DERIVED_REGFRM1_SSR_CLASSNAME_35$183$\"]")

		Select(class_from_sched).select_by_value("8172")
		Select(class_from_cart).select_by_value("8170")

		select_button.click()

		finish_swapping_button = driver.find_element_by_xpath("//*[@id=\"DERIVED_REGFRM1_SSR_PB_SUBMIT\"]")
		finish_swapping_button.click()

		message_window = driver.find_element_by_id("win0divDERIVED_REGFRM1_SS_MESSAGE_LONG$0")
		if (re.search(r"Error", str(message_window))):
			get_error = false

		driver.find_element_by_link_text("Enroll").click()	



if __name__ == '__main__':
	if len(sys.argv) is 1:
		print("\t Invoke as follows: swapping_swapper.py <username> <password>")
		sys.exit()
	else:
		username = sys.argv[1]
		password = sys.argv[2]
		base_url = "https://home.cunyfirst.cuny.edu/psp/cnyepprd/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL?FolderPath=PORTAL_ROOT_OBJECT.HC_SSS_STUDENT_CENTER&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder"	
		driver = webdriver.Chrome()	
		driver.implicitly_wait(30)

#login using username and password
login(driver, base_url, username, password)
#go to enrollment page
navigate_to_enrollment(driver, base_url)
#swap until she can't swap no more
swap(driver, base_url)	
driver.quit()
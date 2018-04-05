
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest, time, re, os, getpass, sys

def login(driver, username, password):
	# login_url = "https://ssologin.cuny.edu/cuny.html"
	login_url = "https://home.cunyfirst.cuny.edu/psp/cnyepprd/EMPLOYEE/HRMS/c/"\
		"SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL?FolderPath=PORTAL_ROOT_OBJECT"\
		".HC_SSS_STUDENT_CENTER&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder"	

	driver.get(login_url)

	username_input = driver.find_element_by_xpath("//*[@id=\"CUNYfirstUsernameH\"]")
	password_input = driver.find_element_by_xpath("//*[@id=\"CUNYfirstPassword\"]")

	username_input.clear()
	password_input.clear()

	username_input.send_keys(username)
	password_input.send_keys(password)

	driver.find_element_by_xpath("//*[@id=\"submit\"]").click()

def navigate_to_enrollment(driver):
	#Go to Student Center
	driver.find_element_by_link_text("Student Center").click()

	# monstrosity, temporary while we figure out cunyfirst's seekrits
	driver.get("https://hrsa.cunyfirst.cuny.edu/psc/cnyhcprd/EMPLOYEE/HRMS/c/"\
		"SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL?FolderPath=PORTAL_ROOT_OBJECT"\
		".HC_SSS_STUDENT_CENTER&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder"\
		"/psp/cnyepprd/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL?"\
		"FolderPath=PORTAL_ROOT_OBJECT.HC_SSS_STUDENT_CENTER&IsFolder=false&IgnoreParamTempl"\
		"=FolderPath%2cIsFolder&PortalActualURL=https%3a%2f%2fhrsa.cunyfirst.cuny.edu"\
		"%2fpsc%2fcnyhcprd%2fEMPLOYEE%2fHRMS%2fc%2fSA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL"\
		"%3f%26IsFolder%3dfalse%26IgnoreParamTempl%3dFolderPath%252cIsFolder&PortalContentURL"\
		"=https%3a%2f%2fhrsa.cunyfirst.cuny.edu%2fpsc%2fcnyhcprd%2fEMPLOYEE%2fHRMS%2fc%2f"\
		"SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL&PortalContentProvider=HRMS&PortalCRefLabel"\
		"=Student%20Center&PortalRegistryName=EMPLOYEE&PortalServletURI=https%3a%2f%2f"\
		"home.cunyfirst.cuny.edu%2fpsp%2fcnyepprd%2f&PortalURI=https%3a%2f%2f"\
		"home.cunyfirst.cuny.edu%2fpsc%2fcnyepprd%2f&PortalHostNode=EMPL&NoCrumbs"\
		"=yes&PortalKeyStruct=yes")
	driver.find_element_by_link_text("Enroll").click()

def choose_semester(driver, semester):

	WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "win0divSSR_DUMMY_RECV1$0"))
    )

	sem = {
			1: "Fall",
			2: "Winter",
			3: "Spring",
			4: "Summer"
	}

	while True:
		try:
			table = driver.find_element_by_xpath("//*[@id=\"SSR_DUMMY_RECV1$scroll$0\"]")
			radio_button = table.find_element_by_xpath(
				"./*/tr[contains(., " + "\"" + sem[semester] 
				+ "\"" + ")]//input[@type= 'radio']"
			)
			radio_button.click()
			break
		except: 
			print("Enrollment for that semester is not open.")
			semester = get_semester()
			clear()

	driver.find_element_by_link_text('Continue').click()


def spam_swap(driver, delay, class_in_sched, class_in_cart):
	
	get_error = True

	while get_error:
		#click SWAP link
		driver.find_element_by_link_text("swap").click()

		#Swap this Class: Select from your schedule
		class_from_sched = driver.find_element_by_xpath(
			"//*[@id=\"DERIVED_REGFRM1_DESCR50$225$\"]"
		)
		#with this Class: Select form Shopping Cart
		class_from_cart = driver.find_element_by_xpath(
			"//*[@id=\"DERIVED_REGFRM1_SSR_CLASSNAME_35$183$\"]"
		)

		Select(class_from_sched).select_by_value(class_in_sched)
		Select(class_from_cart).select_by_value(class_in_cart)

		#click SELECT button
		driver.find_element_by_xpath(
			"//*[@id=\"DERIVED_REGFRM1_SSR_PB_ADDTOLIST1$184$\"]"
		).click()

		finish_swapping_button = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.ID, "DERIVED_REGFRM1_SSR_PB_SUBMIT"))
		)
		finish_swapping_button.click()

		message_window = WebDriverWait(driver, 10).until(
        	EC.presence_of_element_located((By.ID, "win0divDERIVED_REGFRM1_SS_MESSAGE_LONG$0"))
		)
		if (re.search(r"Error", str(message_window))):
			get_error = False

		driver.find_element_by_link_text("Enroll").click()

		time.sleep(delay)

def spam_add(driver, delay):

	get_error = True

	while get_error:
		driver.find_element_by_link_text("add").click()

		driver.find_element_by_xpath(
			"//*[@id=\"DERIVED_REGFRM1_LINK_ADD_ENRL$82$\"]"
		).click()

		finish_enroll_button = WebDriverWait(driver, 10).until(
        	EC.presence_of_element_located((By.ID, "DERIVED_REGFRM1_SSR_PB_SUBMIT"))
    	)
		finish_enroll_button.click()

		message_window = WebDriverWait(driver, 10).until(
        	EC.presence_of_element_located((By.ID, "win0divDERIVED_REGFRM1_SS_MESSAGE_LONG$0"))
    	)
		if (re.search(r"Error", str(message_window))):
			get_error = False

		time.sleep(delay)

def get_choice():
	print("========================================")
	print("Menu")
	print("========================================")
	print("[1] enrofling enrofler")
	print("[2] swappling swappler")
	print("[3] exit")
	# print("[4] report a bug")
	# print("[5] buy this man a coffee!")
	print("========================================")

	selection = input("Wut do?: ")
	while not selection.isdigit() or int(selection) not in range(1, 4):
		selection = input("please choose from the menu: ")

	clear()
	return int(selection)

def cart_is_empty(driver):
	WebDriverWait(driver, 10).until(
        	EC.presence_of_element_located((By.ID, "win0divSSR_REGFORM_VW$0"))
    )

	try:
		driver.find_element_by_xpath("//*[@id=\"win0divP_NO_CLASSES$0\"]")
	except:
		return False
	return True;

def get_semester():
	print("========================================")
	print("Which semester are you enrolling for?")
	print("========================================")
	print("[1]Fall Semester\n[2]Winter Semester\n[3]Spring Semester\n[4]Summer Semester")
	print("========================================")
	semester = ""
	while not semester.isdigit() or int(semester) not in range(1, 5):
		semester = input("Semester: ")

	return int(semester)

def swap_opt():
	print("Which class to swap out of?")
	class_in_sched = input("Class Number: ")
	print("Which class to swap in to?")
	class_in_cart = input("Class Number: ")
	return class_in_sched, class_in_cart


def run(cwd):
	username = input("Username: ") + "@login.cuny.edu"
	password = getpass.getpass("Password: ")
	clear()

	#print main menu and ask wether user wants to swap or enroll
	user_choice = get_choice()
	if user_choice == 3:
		sys.exit(0)

	clear()

	# ask user what semester they wish to enroll/swap in
	# give numerical choice for now to avoid user autism
	semester = get_semester()

	# ask user if for the delay between trying to enroll/swap
	delay = input("Time delay between enrolling/swapping(in seconds): ")
	while not delay.isdigit():
		delay = input("Please input delay in seconds: ")

	# assuming the driver is in the same directory, run the chrome webdriver
	driver = webdriver.Chrome(cwd + "\\chromedriver.exe")

	try:
		login(driver, username, password)
		del username, password
		clear()
	except:
		print("Something went wrong. Either our credentials are wrong")

	navigate_to_enrollment(driver)

	choose_semester(driver, semester)

	if cart_is_empty(driver):
		print("Your cart is empty.")
		print("Make sure you have classes in your cart and run this again.")
		print("Press Enter to exit.")
		sys.exit(bool(input("")))	# i don't give care what your input is just press any button

	# enroll until she can't enroll no more
	if user_choice == 1:
		spam_add(driver, int(delay))
	elif user_choice == 2:
		class_in_sched, class_in_cart = swap_opt()
		spam_swap(driver, int(delay), class_in_sched, class_in_cart)

	time.sleep(600)

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
		cwd = os.getcwd()
		clear()
		run(cwd)
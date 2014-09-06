import selenium
import selenium.webdriver
import urllib2
import time
import logging
import traceback
import sys


accounts = [
	('1203210017', 'qwertyuiop'),
	#('5022', '5022'),
]


def login(browser, (user_name, user_pwd)):
	
	browser.get('http://222.24.19.190:8080/portal/index_default.jsp')
	
	user_name_element = browser.find_element_by_id('id_userName')
	user_name_element.send_keys(user_name)

	user_pwd_element = browser.find_element_by_id('id_userPwd')
	user_pwd_element.send_keys(user_pwd)

	login_button_element = browser.find_element_by_id('id_lable_loginbutton_auth')
	login_button_element.click()


def close_browser(browser):
	if browser:
		try:
			browser.quit()
		except:
			pass
	browser = None


def main():

	browser = None
	current_account = 0
	
	handler_stdout = logging.StreamHandler(sys.stdout)
	handler_stdout.setLevel(logging.DEBUG)
	handler_stdout.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
	
	handler_file = logging.FileHandler('imc_portal_auto_login.log')
	handler_file.setLevel(logging.WARNING)
	handler_file.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
	
	logger = logging.getLogger(__name__)
	logger.setLevel(logging.DEBUG)
	logger.addHandler(handler_stdout)
	logger.addHandler(handler_file)

	while True:
	
		try:
			disconnected = False
			
			logger.info('Try to open http://www.baidu.com ...')
			try:
				baidu = urllib2.urlopen('http://www.baidu.com', timeout=15).read()
			except KeyboardInterrupt:
				raise
			except:
				logger.warning('Failed to open http://www.baidu.com')
				disconnected = True
			else:
				if len(baidu) < 400:
					logger.warning('Page size of http://www.baidu.com < 400')
					disconnected = True
			
			if disconnected == True:
			
				logger.warning('It seems that we are disconnected')
				
				if browser:
					logger.info('Quit current browser ...')
					close_browser(browser)
				
				try:
					logger.info('Open a new browser ...')
					browser = selenium.webdriver.Firefox()
					
					logger.info('Try to login as ' + accounts[current_account][0] + ' ...')
					login(browser, accounts[current_account])
					
					current_account = (current_account + 1) % len(accounts)
					
				except KeyboardInterrupt:
					raise
				except:
					logger.error(traceback.format_exc())
					close_browser(browser)
			else:
				logger.info('The connection is OK')
			
			logger.info('Sleep for 30 seconds ...')
			time.sleep(30)

		except KeyboardInterrupt:
			logger.info('Quitting ...')
			close_browser(browser)
			break
		except:
			logger.error(traceback.format_exc())
			close_browser(browser)


if __name__ == '__main__':
	main()

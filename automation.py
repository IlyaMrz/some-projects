from selenium import webdriver


driver = r"C:\\Games\\VScodeProjects\\udemy_automat\\chromedriver.exe"
chrmB = webdriver.Chrome(driver)
chrmB.maximize_window()

chrmB.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
assert 'Selenium Easy' in chrmB.page_source
um = chrmB.find_element_by_id('user-message')
um.clear()
um.send_keys('aaaaaaaaaaaa')

button_text = chrmB.find_element_by_class_name('btn-default')

button_text.click()

chrmB.close()

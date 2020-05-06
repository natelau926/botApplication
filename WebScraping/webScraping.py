from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("")   # link
for i in range(1,3):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
class_name = driver.find_elements_by_class_name('covershot-con')
links = [elem.get_attribute('href') for elem in class_name]
for link in links:
    print(link)

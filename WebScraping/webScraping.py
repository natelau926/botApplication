from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("")   # link
for i in range(1,35):  # scroll time
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
class_name = driver.find_elements_by_class_name("tile__covershot")
#class_name = driver.find_elements_by_class_name("covershot-con")
links = [elem.get_attribute('href') for elem in class_name]

for link in links:
    print("ed.auto_offer('" + link + "')")

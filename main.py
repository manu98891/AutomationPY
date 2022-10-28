from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('chromedriver.exe')

driver.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')

time.sleep(3)

user_box = driver.find_element(By.NAME,'email')
pass_box= driver.find_element(By.NAME,'passwd')
submit_button = driver.find_element(By.NAME,'SubmitLogin')

user_box.send_keys('manulos@gmail.com')
pass_box.send_keys('123456aA!')
submit_button.click()

time.sleep(3)

driver.quit()
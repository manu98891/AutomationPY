from lib2to3.pgen2 import driver
from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time 

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.google.com')
time.sleep(2)

search_box = driver.find_element(By.NAME,'q')
search_box.send_keys('Python selenium')

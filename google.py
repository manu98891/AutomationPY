from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time 

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.google.com')
time.sleep(2)

#search_box = driver.find_element(By.NAME,'q')
#search_box = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_box = driver.find_element(By.CSS_SELECTOR,'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
search_box.send_keys('Python selenium')

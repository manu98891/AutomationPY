import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select # Para usar la libreria de select de selenium

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://katalon-demo-cura.herokuapp.com/profile.php#login')

time.sleep(3)

userName_box = driver.find_element(By.NAME,'username')
userPass_box = driver.find_element(By.NAME,'password')
logIn_button = driver.find_element(By.ID,'btn-login')

time.sleep(3)

userName_box.send_keys('John Doe')
userPass_box.send_keys('ThisIsNotAPassword')

time.sleep(3)

logIn_button.click()

time.sleep(5)

countryDropDown = Select(driver.find_element(By.NAME,'facility')) # Llamar al dropdown
countryDropDown.select_by_value('Seoul CURA Healthcare Center')

time.sleep(5)

driver.quit()
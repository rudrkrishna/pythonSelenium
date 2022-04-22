import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service("../BrowserDrivers/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("http://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")

# with visible text
wait = WebDriverWait(driver, 15)
wait.until(EC.element_to_be_clickable(driver.find_element(by=By.ID, value="dropdowm-menu-1")))
sel1 = Select((driver.find_element(by=By.ID, value="dropdowm-menu-1")))
sel1.select_by_visible_text("Python")
time.sleep(3)

# with value
wait.until(EC.element_to_be_clickable(driver.find_element(by=By.ID, value="dropdowm-menu-2")))
sel2 = Select(driver.find_element(by=By.ID, value="dropdowm-menu-2"))
sel2.select_by_value("maven")
time.sleep(3)

# with Index
wait.until(EC.element_to_be_clickable(driver.find_element(by=By.ID, value="dropdowm-menu-3")))
sel3 = Select(driver.find_element(by=By.ID, value="dropdowm-menu-3"))
sel3.select_by_index(3)
time.sleep(3)


# checkBoxes
checkbox1 = driver.find_element(by=By.XPATH, value="//input[@value='option-1']")
checkbox2 = driver.find_element(by=By.XPATH, value="//input[@value='option-2']")
checkbox3 = driver.find_element(by=By.XPATH, value="//input[@value='option-3']")
checkbox4 = driver.find_element(by=By.XPATH, value="//input[@value='option-4']")

checkbox1.click()
checkbox2.click()
checkbox3.click()
checkbox4.click()
checkbox1.click()

# radio button

radio1 = driver.find_element(by=By.XPATH, value="//input[@value='yellow']")
radio1.click()
time.sleep(3)
driver.quit()
import time
import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


s = Service("../BrowserDrivers/chromedriver")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))
alert = Alert(driver)
driver.get("http://webdriveruniversity.com/File-Upload/index.html")

driver.find_element(by=By.XPATH, value="//input[@id='myFile']").send_keys("/Users/rudrkrishna/Downloads/Mini Assignment 1 - Xpath.docx")
time.sleep(5)
driver.find_element(by=By.XPATH, value="//input[@id='submit-button']").click()
alert.accept()
time.sleep(5)
driver.quit()
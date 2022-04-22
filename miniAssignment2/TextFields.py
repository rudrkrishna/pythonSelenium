from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service("../BrowserDrivers/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("http://webdriveruniversity.com/Autocomplete-TextField/autocomplete-textfield.html")
str= "B"
driver.find_element(by=By.XPATH, value="//input[@id='myInput']").send_keys(str)
food = driver.find_element(by=By.XPATH,value="(//div[@id='myInputautocomplete-list']/div)[1]")
food.click()
driver.find_element(by=By.XPATH, value="//input[@id='submit-button']").click()
currentURL = driver.current_url
if currentURL.__contains__(str):
    print("Yes")
else:
    print("No")

driver.quit()
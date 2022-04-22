from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

s = Service("../BrowserDrivers/chromedriver")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
alert = Alert(driver)
driver.get("http://webdriveruniversity.com/Actions/index.html")
driver.implicitly_wait(10)
driver.set_page_load_timeout(10)
action = ActionChains(driver)
source = driver.find_element(by=By.XPATH, value="//div[@id='draggable']//p")
target = driver.find_element(by=By.XPATH, value="//b[normalize-space()='DROP HERE!']")
action.drag_and_drop(source, target)
double_click = driver.find_element(by=By.XPATH, value="//h2[normalize-space()='Double Click Me!']")
action.double_click(double_click)

link1 = driver.find_element(by=By.XPATH, value="//button[normalize-space()='Hover Over Me First!']")
link11 = driver.find_element(by=By.XPATH,
                             value="//div[@class='dropdown hover']//a[@class='list-alert'][normalize-space()='Link 1']")
action.move_to_element(link1).move_to_element(link11).click().perform()
alert.accept()


click_and_hold_element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='Click and Hold!']")
action.click_and_hold(click_and_hold_element)

driver.quit()
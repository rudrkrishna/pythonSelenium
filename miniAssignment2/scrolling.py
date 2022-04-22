
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service("../BrowserDrivers/chromedriver")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("http://webdriveruniversity.com/Scrolling/index.html")
driver.implicitly_wait(10)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


driver.execute_script("window.scrollBy(0,2000)","")
target = driver.find_element(by=By.XPATH, value="//div[@id='zone4']")
driver.execute_script('arguments[0].scrollIntoView(true);', target)


target1 = driver.find_element(by=By.XPATH, value="//h1[@id='zone2-entries']")
driver.execute_script('arguments[0].scrollIntoView(true);', target1)


target2 = driver.find_element(by=By.XPATH, value="//h1[@id='zone3-entries']")
driver.execute_script('arguments[0].scrollIntoView(true);', target2)


target3 = driver.find_element(by=By.XPATH, value="//div[@id='zone1']")
driver.execute_script('arguments[0].scrollIntoView(true);', target3)


action = ActionChains(driver)
action.move_to_element(driver.find_element(by=By.XPATH,value="//div[@id='zone1']")).move_to_element(driver.find_element(by=By.XPATH, value="//h1[@id='zone3-entries']")).move_to_element(driver.find_element(by=By.XPATH, value="//h1[@id='zone2-entries']")).move_to_element(driver.find_element(by=By.XPATH, value="//div[@id='zone4']")).move_to_element(driver.find_element(by=By.XPATH, value="//h1[@id='zone2-entries']")).perform()

driver.quit()
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class buttonclicktest:
    s = Service("../BrowserDrivers/chromedriver")
    driver = webdriver.Chrome(service=s)
    driver.get("http://webdriveruniversity.com/Click-Buttons/index.html")

    try:
        # Button Click Using normal/inbuilt method
        element1 = driver.find_element(by=By.XPATH, value="//*[text()='CLICK ME!']")
        element1.click()
        wait = WebDriverWait(driver, 15)
        close1 = driver.find_element(by=By.XPATH,
                                     value="//div[@id='myModalClick']//button[@type='button'][normalize-space()='Close']")
        wait.until(EC.element_to_be_clickable(close1))
        close1.click()
        driver.implicitly_wait(10)

        # Button Click Using JavaScript
        element2 = driver.find_element(by=By.XPATH, value="//*[text()='CLICK ME!!']")
        driver.execute_script("arguments[0].click();", element2)
        close2 = driver.find_element(by=By.XPATH,
                                     value="//div[@class='modal-dialog modal-md']//button[@type='button'][normalize-space()='Close']")
        wait.until(EC.element_to_be_clickable(close2))
        close2.click()
        time.sleep(1)

        # Button Click Using Action Class
        element3 = driver.find_element(by=By.XPATH, value="//*[text()='CLICK ME!!!']")
        action = ActionChains(driver)
        action.move_to_element(element3).click().perform()
        close3 = driver.find_element(by=By.XPATH,
                                     value="//div[@id='myModalMoveClick']//button[@type='button'][normalize-space()='Close']")
        wait.until(EC.element_to_be_clickable(close3))
        close3.click()
    finally:
        driver.quit()



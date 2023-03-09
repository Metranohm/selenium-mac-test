from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

s=Service('/Users/Andrew/documents/webdrivers/chromedriver')
driver = webdriver.Chrome(service=s)

driver.get("http://www.booking.com")
time.sleep(3)
driver.get(By.CLASS_NAME, "fc63351294 a822bdf511 e3c025e003 fa565176a8 f7db01295e c334e6f658 ae1678b153").click()
time.sleep(3)
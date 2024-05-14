from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome();
driver.get('https://google.com/doodles/celebrating-garden-gnomes')
time.sleep(2)
# driver.find_element(By., 'cta-canvas').click()
driver.find_element(By.XPATH, '/html/body/div/div/div[4]').click()
time.sleep(10)
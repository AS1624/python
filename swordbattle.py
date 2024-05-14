import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
keys = ['w', 'a', 's', 'd']
current = 0
driver = webdriver.Chrome()
driver.get('https://swordbattle.io')
element = WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.NAME, "close"))
)
driver.find_element(By.NAME, "close").click()
element = WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.NAME, "name"))
)
driver.find_element(By.NAME, 'name').send_keys('RizzardOfOz')
driver.find_element(By.NAME, 'btn').click()
element = WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.TAG_NAME, "canvas"))
)
time.sleep(5)
while True:
  driver.find_element(By.TAG_NAME, 'body').send_keys(keys[current])
  #if random(0, 100) > 99:
  #  current = round(random(0.5, 4.499)) - 1
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.geoguessr.com/quiz/seterra/challenge/3Z43M')
time.sleep(10)
# driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
# time.sleep(1)
northern = driver.find_element(By.XPATH, '//g[31]/circle[2]')
interior = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div[1]/div/div[2]/div[1]/svg/g[32]/circle[2]')
central  = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div[1]/div/div[2]/div[1]/svg/g[33]/circle[2]')
east     = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div[1]/div/div[2]/div[1]/svg/g[34]/circle[2]')
west     = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div[1]/div/div[2]/div[1]/svg/g[35]/circle[2]')
aleutian = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div[1]/div/div[2]/div[1]/svg/g[36]/circle[2]')

# northern.click()
time.sleep(10)
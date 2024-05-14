import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

gpt = webdriver.Chrome()
survey = webdriver.Chrome()

survey.get('http://surveyjunkie.com/?login')
element = WebDriverWait(survey, 120).until(
  EC.presence_of_element_located((By.CLASS_NAME, "survey-v2-button ng-binding"))
)
survey.find_element(By.CLASS_NAME, "survey-v2-button ng-binding").click()
element = WebDriverWait(survey, 10).until(
  EC.presence_of_element_located((By.CLASS_NAME, "entry-label"))
)
survey.find_element(By.CLASS_NAME, 'entry-label')
time.sleep(45)
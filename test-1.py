from selenium import webdriver
#import cv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
answers = 'ABCD'
accumilated = []
driver = webdriver.Chrome()
image_tab = webdriver.Chrome()
print('\n\n\n\n\n\n\n\n\n\n')
while True:
    driver.get('https://online.dmv.alaska.gov/practiceknowledgetest/')
    driver.find_element(By.ID, 'ContentPlaceHolder1_Button7').click()
    question = driver.find_element(By.ID, 'ContentPlaceHolder1_TextBox7').text
    driver.find_element(By.ID, 'ContentPlaceHolder1_Button1').click()
    answerIndex = driver.find_element(By.ID, 'ContentPlaceHolder1_Result').get_attribute('value').split()
    answerIndex = answers.find(answerIndex[len(answerIndex) - 1])
    answerPath = '/html/body/div[2]/div[6]/div/div/form/table/tbody/tr[6]/td/table/tbody/tr[{}]/td[3]/input'
    answer = driver.find_element(By.XPATH, answerPath.format(answerIndex + 4)).get_attribute('value')
    if not (question + ' ' + answer) in accumilated:
        print(question, answer, len(accumilated))
        accumilated.append(question + ' ' + answer)
        # driver.get_screenshot_as_file('driver1_{}.png'.format((len(accumilated)-1)))
        Img_url = driver.find_element(By.ID, 'ContentPlaceHolder1_Image1').get_attribute('src')
        Img_size = driver.find_element(By.ID, 'ContentPlaceHolder1_Image1').get_attribute('style').split(':')
        print(Img_size)
        image_tab.get(Img_url)
        image_tab.set_window_size(int(Img_size[2].split('p')[0]), int(Img_size[1].split('p')[0]))
        image_tab.get_screenshot_as_file('driver_{}.png'.format((len(accumilated)-1)))

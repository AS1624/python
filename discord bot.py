from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading

# Function to perform actions in the Discord channel
def run(driver: webdriver.Chrome):
    while True:
        try:
            driver.find_element(By.XPATH, '//*[@id="message-accessories-1237922259239178292"]/div/div/div/button[1]').click()
            driver.find_element(By.XPATH, '//*[@id="message-accessories-1237922259239178292"]/div/div/div/button[2]').click()
            time.sleep(1)
        except Exception as e:
            #try:
            driver.refresh()
            time.sleep(10)
            #except:
            #    print("cant reload")
            print("Failed with", e)

# Same credentials for all instances
email = "thebest1dudes@gmail.com"
password = "the best 1"

# List to store instances of drivers and threads
drivers = []
threads = []

# Function to create and run WebDriver instance
def create_and_run():
    driver = webdriver.Chrome()
    drivers.append(driver)
    driver.get('https://discord.com/channels/1226710864376365178/1235278175915999343')
    time.sleep(3)

    driver.find_element(By.XPATH, "//*[@id=\"app-mount\"]/div[2]/div[1]/div[1]/div/div/div/section/div[2]/button[2]/div").click()
    time.sleep(3)

    inputs = driver.find_elements(By.TAG_NAME, "input")
    inputs[0].send_keys(email)
    inputs[1].send_keys(password)
    driver.find_elements(By.TAG_NAME, "button")[1].click()
    time.sleep(10)

    run(driver)

# Create and start threads for WebDriver instances
for _ in range(2):  # Create 5 instances
    thread = threading.Thread(target=create_and_run)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Quit all instances of WebDriver
for driver in drivers:
    driver.quit()

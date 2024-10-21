from selenium import webdriver
from multiprocessing import Process
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

<<<<<<< HEAD
url = "https://docs.google.com/forms/d/e/1FAIpQLSf38RjrNRJUu5kGxtiA86xxEFeXN0zs5RgGDjTFFIDF7aEJ7w/viewform?entry.292038320=Additional+homework+for+students&entry.292038320=Increased+student+work+load&entry.294099767=6+period+days+are+better&entry.613315111=Additional+homework+for+students&entry.613315111=Increased+student+work+load&entry.646371755=Students&entry.297938067=&dlut=1729538272138&entry.646371755_sentinel=&entry.1950717998_sentinel=&entry.1241312645_sentinel=&entry.292038320_sentinel=&entry.613315111_sentinel=&fvv=1&partialResponse=%5Bnull%2Cnull%2C%22-1480974334428333231%22%5D&pageHistory=0&fbzx=9221023663716217541&submissionTimestamp=1729540671063"
emails = ["seeman.avery@asdk12.net"]#, "seeman.avery@asdk12.net", "seeman.avery@asdk12.net", "seeman.avery@asdk12.net", "seeman.avery@asdk12.net", "seeman.avery@asdk12.net", "seeman.avery@asdk12.net", "seeman.avery@asdk12.net", "seeman.avery@asdk12.net", "seeman.avery@asdk12.net"]
times = 100000

def open_url(url):
    driver = webdriver.Firefox()
    driver.get(url)

    """
    adress_box = driver.find_element(By.ID, "identifierId")
    adress_box.send_keys(address)
    adress_box.send_keys(Keys.ENTER)

    time.sleep(5)

    driver.find_element(By.ID, "userNameInput").send_keys(username)
    password_box = driver.find_element(By.ID, "passwordInput")
    password_box.send_keys(password)
    password_box.send_keys(Keys.ENTER)

    """
    time.sleep(5)
    
    print(url)
    time.sleep(2)
    while i < times:
        time.sleep(0.5)
        if i % 100 == 0:
            print(i)
        i += 1

# List of URLs to open in parallel

# print(__name__)

if __name__ == "__main__":
    # Create a separate process for each URL
    processes = [Process(target=open_url, args=(url,)) for _ in range(numThreads)]

    # Start each process
    for process in processes:
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()
    print(numThreads * times)

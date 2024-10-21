from selenium import webdriver
from multiprocessing import Process
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

url = "https://docs.google.com/forms/u/1/d/e/1FAIpQLSeVARGqLX_hi7FK8pJnQEQJkbEBSwW91fntO8ZLjXI8RjiL3A/formResponse?entry.8664394=Duncan+Brabec+&entry.579291710=None&entry.1449904202=None&entry.278202488=Jayla+Angelina+Baguyos+&entry.1028584163=None&entry.1262475601=Damien+Meyer+&entry.778541354=Luna+Summerlin+&entry.819522117=None&hud=true&fvv=1&partialResponse=[[[null%2C1262475601%2C[%22Damien+Meyer+%22]%2C0]%2C[null%2C1449904202%2C[%22None%22]%2C0]%2C[null%2C778541354%2C[%22Luna+Summerlin+%22]%2C0]%2C[null%2C579291710%2C[%22None%22]%2C0]%2C[null%2C8664394%2C[%22Duncan+Brabec+%22]%2C0]%2C[null%2C819522117%2C[%22None%22]%2C0]%2C[null%2C278202488%2C[%22Jayla+Angelina+Baguyos+%22]%2C0]%2C[null%2C1028584163%2C[%22None%22]%2C0]]%2Cnull%2C%225095739895225131253%22]&pageHistory=0%2C0&fbzx=5095739895225131253&submissionTimestamp=1728435583171"

times = 100000
numThreads = 8

address = "seeman.avery@asdk12.net"
username = "seeman.avery"
password = "the best 11"



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
    i = 0
    while i < times:
        time.sleep(0.2)
        driver.get(url)
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

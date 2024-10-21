from selenium import webdriver
from multiprocessing import Process
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# options.add_argument('--headless')

url = "https://docs.google.com/forms/u/1/d/e/1FAIpQLScgGWBSXz4IszkVjaQQAckirK_c8uaXa9-oN-9x4IcMOV1e3Q/formResponse?entry.754656146=never+gonna+give+you+up+-+Rick+Astley&entry.447877497=never+gonna+give+you+up+-+Rick+Astley&entry.625087713=never+gonna+give+you+up+-+Rick+Astley&emailAddress=seeman.avery@asdk12.net&dlut=1699496541730&fvv=1&partialResponse=%5Bnull%2Cnull%2C"+"%"+"22404859635932592667"+"%"+"22%5D&pageHistory=0&fbzx=404859635932592667"
emails = 1
address = "seeman.avery@asdk12.net"
username = "seeman.avery"
password = "the best 11"
times = 100


def open_url():
    driver = webdriver.Firefox()
    driver.get(url)

    adress_box = driver.find_element(By.ID, "identifierId")
    adress_box.send_keys(address)
    adress_box.send_keys(Keys.ENTER)

    time.sleep(5)

    driver.find_element(By.ID, "userNameInput").send_keys(username)
    password_box = driver.find_element(By.ID, "passwordInput")
    password_box.send_keys(password)
    password_box.send_keys(Keys.ENTER)

    time.sleep(5)

    driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()

    time.sleep(5)

    i = 0
    while i < times:
        print(i)
        try:
            driver.find_element(By.CLASS_NAME, 'uArJ5e UQuaGc kCyAyd l3F1ye ARrCac M9Bg4d')
        except:
            driver.get(url)
            print("not found")
        else:
            print("found")
            driver.find_element(By.CLASS_NAME, 'uArJ5e UQuaGc kCyAyd l3F1ye ARrCac M9Bg4d').click()
            driver.find_element(By.CLASS_NAME, "uArJ5e UQuaGc Y5sE8d VkkpIf QvWxOd")
            time.sleep(1)
            driver.get(url)
        i += 1

# List of URLs to open in parallel

# print(__name__)

if __name__ == "__main__":
    # Create a separate process for each URL
    processes = [Process(target=open_url) for i in range(emails)]

    # Start each process
    for process in processes:
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()
    print(emails * times)

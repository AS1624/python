from selenium import webdriver
from multiprocessing import Process
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
# options.add_argument('--headless')

url = "https://docs.google.com/forms/u/1/d/e/1FAIpQLScgGWBSXz4IszkVjaQQAckirK_c8uaXa9-oN-9x4IcMOV1e3Q/formResponse?entry.754656146=never+gonna+give+you+up+-+Rick+Astley&entry.447877497=never+gonna+give+you+up+-+Rick+Astley&entry.625087713=never+gonna+give+you+up+-+Rick+Astley&emailAddress=seeman.avery@asdk12.net&partialResponse=%5Bnull%2Cnull%2C" # +"%"+"22404859635932592667"+"%"+"22%5D"
emails = 5
address = "seeman.avery@asdk12.net"
username = "seeman.avery"
password = "the best 11"
times = 1000000


def open_url(index):
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(10 + 15 * emails)

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
        # print(i)
        '''
        if driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[3]/div").get_attribute("role") == "button":
            # print("found")
            driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[3]/div").click()
            driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div").click()
            elem = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "Submit another response"))
                )
            driver.get(url)
        else:
            driver.get(url)
            # print("not found")
        '''
        driver.get(url)
        if driver.current_url == url:
            i += 1
        else:
            print(i, index, sep=", ")
            return False
        if i % 100 == 0:
            print(i, index, sep=", ")

# List of URLs to open in parallel

# print(__name__)

if __name__ == "__main__":
    # Create a separate process for each URL
    processes = [Process(target=open_url, args=(i,)) for i in range(emails)]

    # Start each process
    for process in processes:
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()
    print(emails * times)
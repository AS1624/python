from selenium import webdriver
from multiprocessing import Process
import time

url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSfQDJGLouQfgqqvNUk9YG-RdJyAh4xYZq6Mu0ABPtG7SWrhuQ/formResponse?entry.499746011=Multi2&entry.1262844392=Option+1&entry.1410038430=Option+1&emailAddress={}&&partialResponse=%5Bnull%2Cnull%2C"+"%"+"222207935557372852228"+"%"+"22%5D"
emails = ["seeman.avery@asdk12.net", "seeman.avery@asdk12.net", "seeman.avery@asdk12.net", "seeman.avery@asdk12.net", "seeman.avery@asdk12.net", "seeman.avery@asdk12.net", "seeman.avery@asdk12.net", "seeman.avery@asdk12.net", "seeman.avery@asdk12.net", "seeman.avery@asdk12.net"]
times = 100


def open_url(url):
    driver = webdriver.Chrome()
    driver.get(url)
    print(url)
    time.sleep(200)
    i = 0
    while i < times:
        driver.get(url)
        i += 1

# List of URLs to open in parallel

# print(__name__)

if __name__ == "__main__":
    # Create a separate process for each URL
    processes = [Process(target=open_url, args=(url.format(email),)) for email in emails]

    # Start each process
    for process in processes:
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()
    print(len(emails) * times)

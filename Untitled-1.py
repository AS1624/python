import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# define custom options for the Selenium driver
options = Options()
# free proxy server URL
proxy_server_url = "162.248.225.124:80"
options.add_argument(f'--proxy-server={proxy_server_url}')

# create the ChromeDriver instance with
# custom options
driver = webdriver.Chrome(
    options=options
)

# print the IP the request comes from 
driver.get('http://httpbin.org/ip')
print(driver.find_element(By.TAG_NAME, "body").text)
time.sleep(100)
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import random

# the list of proxy to rotate on 
PROXIES = [
    'http://19.151.94.248:88',
    'http://149.169.197.151:80',
    # ...
    'http://212.76.118.242:97'
]

# randomly extract a proxy
random_proxy = random.choice(PROXIES)

# set the proxy in Selenium Wire
seleniumwire_options = {
    'proxy': {
        'http': f'{random_proxy}',
        'https': f'{random_proxy}',
        'verify_ssl': False,
    },
}

# create a ChromeDriver instance
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    seleniumwire_options=seleniumwire_options
)

driver.visit('https://example.com/')

# scraping logic...

driver.quit()
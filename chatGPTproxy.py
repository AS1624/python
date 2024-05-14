from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

# Define the proxy server settings
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = "http://47.49.228.234:80"
proxy.ssl_proxy = "https://47.49.228.234:80"

# Create a desired capabilities object and set the proxy
capabilities = webdriver.DesiredCapabilities.CHROME.copy()
proxy.to_capabilities(capabilities)

# Start the Chrome WebDriver with the desired capabilities
driver = webdriver.Chrome(desired_capabilities=capabilities)

# Now you can use the driver to navigate websites through the proxy
driver.get("https://example.com")
time.sleep(10)
# Don't forget to close the WebDriver when you're done
driver.quit()
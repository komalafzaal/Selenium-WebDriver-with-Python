#Running scripts and PATH
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com/')


# Add a delay of 5 seconds to observe the website
time.sleep(5)

# Close the browser
driver.quit()
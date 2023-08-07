# Implicit Wait:
# Implicit wait sets a default wait time for the WebDriver instance.
# If an element is not immediately available, WebDriver will wait for
# the specified time before throwing an exception. The implicit wait is applied
# globally for all elements in the WebDriver session.

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Wait for up to 10 seconds for elements to be found


# Explicit Wait:
# Explicit wait is used to wait for a specific condition to be met for a certain element.
# It allows you to define a wait for a particular condition, and it will wait only for
# that specific condition to be satisfied before proceeding further.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds for the condition to be satisfied

# Wait for an element to be clickable
element = wait.until(EC.element_to_be_clickable((By.ID, "myElementID")))

# Perform actions on the element
element.click()

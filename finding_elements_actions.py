from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com/')

#By id
cart = driver.find_element(By.ID, "site-header-cart")
print(cart)
print(type(cart))
cart_text = cart.text
print(cart_text)


#Actions
#Sending Keys (Typing into Input Fields):

search_field = driver.find_element(By.ID, 'woocommerce-product-search-field-0')
search_field.send_keys("hoodie")
search_field.send_keys(Keys.ENTER)

#By Name
filter_field = driver.find_element(By.NAME, 'orderby')
filter_field.send_keys("Sort by Latest")

# Add a delay of 5 seconds to observe the website
time.sleep(500)

# Close the browser
driver.quit()



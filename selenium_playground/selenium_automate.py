from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
assert driver.title == "Selenium Easy Demo - Simple Form to Automate using Selenium"
message_form = driver.find_element_by_id("user-message")
message_form.send_keys("Hello world!")
button = driver.find_element_by_css_selector("button.btn-default")
button.click()
assert driver.find_element_by_css_selector("span#display").text == "Hello world!"
driver.quit()



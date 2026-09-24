from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("https://webdriveruniversity.com/Contact-Us/contactus.html")

first_name_input = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
first_name_input.send_keys("Prueba")

last_name_input = driver.find_element(By.XPATH, "//input[@name='last_name']")
last_name_input.send_keys("Test")

email_input = driver.find_element(By.XPATH, "//input[@name='email']")
email_input.send_keys("test@ejemplo.com")

comments_input = driver.find_element(By.XPATH, "//textarea[@name='message']")
comments_input.send_keys("Mensaje de prueba")

submit_button = driver.find_element(By.XPATH, "//input[@value='SUBMIT']")

time.sleep(10)


driver.quit()
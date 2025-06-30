from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/automation-practice-form")

driver.maximize_window()

time.sleep(2)
First_Name = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
First_Name.clear()
First_Name.send_keys("sneha")
Last_Name = driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
Last_Name.clear()
Last_Name.send_keys("latha")
Email = driver.find_element(By.XPATH, "(//input[@type='text'])[3]")
Email.clear()
Email.send_keys("sneha@gmail.com")

time.sleep(3)
driver.quit()

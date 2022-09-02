import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")
driver.get("http://localhost:8120/")
elemento1 = driver.find_element(By.ID, "user")
elemento1.clear()
elemento1.send_keys("root")

elemento2 = driver.find_element(By.NAME, "pass")
elemento2.clear()
elemento2.send_keys("password")
elemento2.submit()
time.sleep(1)
driver.get("http://localhost:8120/")
time.sleep(1)

elemento3 = driver.find_element(By.ID, "CreateTicketInQueue")
elemento3.click()

elemento4 = driver.find_element(By.NAME, "Subject")
elemento4.send_keys("Test michel")
time.sleep(1)
elemento5 = driver.find_element(By.NAME, "SubmitTicket").click()
time.sleep(5)
driver.close()


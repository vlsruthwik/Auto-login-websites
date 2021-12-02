from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


username = "20BCI7030"
password = "1234"
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://172.18.10.10:8090/")

driver.find_element_by_id("details-button").click()

driver.find_element_by_id("proceed-link").click()

driver.find_element_by_id("username").send_keys(username)

driver.find_element_by_id("password").send_keys(password)

driver.find_element_by_id("loginbutton").click()

sleep(1)
driver.close()
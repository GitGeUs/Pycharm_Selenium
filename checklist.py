from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'https://www.ironspider.ca/forms/checkradio.htm'
driver.get(url)

time.sleep(1)

# driver.find_element(By.XPATH, '//*[@id="Content"]/div[1]/blockquote[1]/form/input[2]').click()
checked =  driver.find_element(By.XPATH, '//*[@id="Content"]/div[1]/blockquote[1]/form/input[2]').is_selected()
if checked:
    print("Already checked")
else:
    driver.find_element(By.XPATH, '//*[@id="Content"]/div[1]/blockquote[1]/form/input[2]').click()
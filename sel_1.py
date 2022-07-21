from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.google.com/")

# driver.refresh()
# driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').click
aa = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
aa.send_keys('no war')
time.sleep(1)
aa.clear()
time.sleep(1)
aa.send_keys('toyota camry us price')
aa.send_keys(Keys.ENTER)
# aa.send_keys(Keys.RETURN) #alternative 1
# aa.submit() #alternative 2


time.sleep(2)
driver.back()
time.sleep(1)
# driver.implicitly_wait(2.5)
driver.forward()
time.sleep(1)

# driver.fullscreen_window()
# driver.maximize_window()
# driver.set_window_size(900, 600)
driver.set_window_rect(x=100, y=50, width=1200, height=500)

time.sleep(1)

# print(driver.title)
ab = driver.title
# print("TiTle of This Page is " + ab)
print("TiTle of This Page is " + '"' + ab + '"')

time.sleep(2)
driver.quit()

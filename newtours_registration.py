from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
url = 'https://demo.guru99.com/test/newtours/register.php'
driver.get(url)

# assertion verifies if el_1 has text == "CONTACT". If it pass, the assertions do not impact the code after, If not, script execution will stop.
el_1 = driver.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[4]/a')
assert el_1.text == 'CONTACT'

# asserts that text "Mercury" is in page title
assert "Mercury" in driver.title

# resize page to 1100x700 px, windows position 100px and 50px from left top corner
driver.set_window_rect(x=100, y=50, width=1100, height=700)
real_title = driver.title

# defined function just for practice
def verify_title():
    if real_title.__contains__("Register"):
        print("das ma boi")
    else:
        print("naaa")
verify_title()


# fill the fields of registration page
driver.find_element(By.NAME, "firstName").send_keys("Jimsher")
driver.find_element(By.NAME, "lastName").send_keys("Dadiani")
driver.find_element(By.NAME, "phone").send_keys("+995559000000")
driver.find_element(By.ID, "userName").send_keys("jimsher@superstar.io")
driver.find_element(By.NAME, "address1").send_keys("Lexington 123")
driver.find_element(By.NAME, "city").send_keys("Brooklyn")
driver.find_element(By.NAME, "state").send_keys("NY ")
driver.find_element(By.NAME, "postalCode").send_keys("11235")

# fill drop down by select_by_visible_text
country = driver.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[11]/td[2]/select')
sel_country = Select(country)
sel_country.select_by_visible_text("UNITED STATES")

# alternative
# country = Select(driver.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[11]/td[2]/select'))
# country.select_by_visible_text("UNITED STATES")

# alternative
# sel_country = Select(country).select_by_visible_text("UNITED STATES")

driver.find_element(By.ID, "email").send_keys("JimStar")
driver.find_element(By.NAME, "password").send_keys("123456")
driver.find_element(By.NAME, "confirmPassword").send_keys("123456")

press_enter = driver.find_element(By.NAME, "submit")
time.sleep(3) # time before you hit "submit" button.
press_enter.send_keys(Keys.ENTER)

# Regarding last 3 lines of code. When you need to click "Submit" button to send data from registration forms.
# I expected to use .submit(), like this:
# press_enter.submit()
# or
# driver.find_element(By.NAME, "submit").submit()
# but it doesn't work. Have no idea why.
# So instead I used .send_keys(Keys.ENTER)
# Update: Submit. In Selenium 4 this is no longer implemented with a separate endpoint and functions by executing a script.
# As such, it is recommended not to use this method and to click the applicable form submission button instead.

time.sleep(7)
driver.quit()

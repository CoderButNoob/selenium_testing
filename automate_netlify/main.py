from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import  time
import  random



driver = webdriver.Chrome()
driver.get("https://trytestingthis.netlify.app/index.html")
driver.maximize_window()

time.sleep(2)

# first name
first_name =  driver.find_element(By.ID, "fname")
first_name.send_keys("Aniket")

time.sleep(1)

#last name
last_name = driver.find_element(By.ID, "lname")
last_name.send_keys("Sonar")

time.sleep(1)

#select gender -> male
male = driver.find_element(By.ID , "male")
male.click()

time.sleep(1)

# #select gender -> female
# female = driver.find_element(By.ID, "female")
# female.click()
#
# #select gender -> others(
# other = driver .find_element(By.ID, "other")
# other.click()

#select option DROPDOWN
dropdown_elements = driver.find_element(By.ID, "option")
select = Select(dropdown_elements)


select.select_by_visible_text("Option 1")
# select.select_by_visible_text("Option 2")
# select.select_by_visible_text("Option 3")

time.sleep(1)

#select checkbox (can be multiple)
checkboxs = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
for checkbox in checkboxs:
    value = checkbox.get_attribute("value")
    if value in ["Option 1", "Option 2"]:
        if not checkbox.is_selected():
            checkbox.click()

time.sleep(1)

#Auto-Guess DropDown
datalist = driver.find_element(By.NAME,"Options")
datalist.send_keys("Vanilla")
time.sleep(1)

#Select Color
select_color = driver.find_element(By.ID,"favcolor")
select_color.send_keys("#0000FF")
time.sleep(1)

#select date
select_date = driver.find_element(By.ID, "day")
select_date.send_keys("02-12-2002")
time.sleep(1)

#select range
select_range = driver.find_element(By.ID,"a")
select_range.send_keys(Keys.ARROW_RIGHT * 19)
time.sleep(1)

#add file
file_path = "C:/Users/anike/Downloads/ANIKET-SONAR-Resume.pdf"
file_input = driver.find_element(By.ID,"myfile")
file_input.send_keys(file_path)
time.sleep(1)

#Range Box
range_box = driver.find_element(By.ID, "quantity")
num = random.randint(1,5)
range_box.send_keys(num)
time.sleep(1)

#Long Message Box
long_message =  driver.find_element(By.NAME,"message")
long_message.clear()
long_message.send_keys("Hi I am Aniket and I am doing Python Automation")
time.sleep(1)

#final submit button
submit_btn = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/form/fieldset/button")
submit_btn.click()
time.sleep(2)


# driver.quit()


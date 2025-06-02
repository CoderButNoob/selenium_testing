from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from utils import fill_input, click_element, click_checkboxes, select_from_dropdown

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Input fields
fill_input(driver, 'name', 'Aniket')
fill_input(driver, 'email', 'sonar@gmail.com')
fill_input(driver, 'phone', '6295531812')
fill_input(driver, 'textarea', 'Hi my name is Aniket and I am doing selenium automation testing')

# Gender radio button
click_element(driver, 'male')

# Check all days
click_checkboxes(driver, "//input[@type='checkbox' and contains(@id,'day')]")
time.sleep(2)

# Country input
fill_input(driver, 'country', 'India')
time.sleep(2)

# Select dropdowns
select_from_dropdown(driver, 'colors', 'White')
time.sleep(2)
select_from_dropdown(driver, 'animals', 'Rabbit')
time.sleep(2)

#date picker 1
year = '2026'
month = 'January'
day = '02'

driver.find_element(By.ID,'datepicker').click()

while True:
    m = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    y = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if month == m and year == y:
        break
    else:
        next_arrow = driver.find_element(By.XPATH,"//a[@title='Next']")
        next_arrow.click()

dates = driver.find_elements(By.XPATH,'//tbody/tr/td/a')
for date in dates:
    if date.text == str(int(day)) :
        date.click()
        time.sleep(2)
        break


#date picker 2
year = '2026'
month = 'Jan'
day = '02'

driver.find_element(By.XPATH,'//*[@id="txtDate"]').click()

month_drop = Select(driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/select[1]'))
month_drop.select_by_visible_text(month)

year_drop = Select(driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/select[2]'))
year_drop.select_by_visible_text(year)

dates  = driver.find_elements(By.XPATH,'//tbody/tr/td/a')
for date in dates:
    if date.text == str(int(day)):
        date.click()
        time.sleep(2)
        break

#single file upload
file_path = "C:/Users/anike/Downloads/Ge_intro.docx"
driver.find_element(By.ID,'singleFileInput').send_keys(file_path)
driver.find_element(By.XPATH,'//*[@id="singleFileForm"]/button').click()

#multiple file upload
file_paths = ["C:/Users/anike/Downloads/Ge_intro.docx","C:/Users/anike/Downloads/Get_Started_With_Smallpdf.pdf"]
for path in file_paths:
    driver.find_element(By.XPATH,'//*[@id="multipleFilesInput"]').send_keys(path)
driver.find_element(By.XPATH,'//*[@id="multipleFilesForm"]/button').click()



time.sleep(5)



driver.quit()

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests as requests
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


#Alerts
driver.find_element(By.XPATH,'//*[@id="alertBtn"]').click()
alert_window =driver.switch_to.alert
alert_window.accept()
time.sleep(4)

driver.find_element(By.XPATH,'//*[@id="confirmBtn"]').click()
confirmation_alert = driver.switch_to.alert
confirmation_alert.dismiss()

driver.find_element(By.XPATH,'//*[@id="promptBtn"]').click()
promt_alert = driver.switch_to.alert
promt_alert.send_keys("Aniket")
promt_alert.accept()

#new tab
original_window = driver.current_window_handle
driver.find_element(By.XPATH,'//*[@id="HTML4"]/div[1]/button').click()
time.sleep(2)
all_windows = driver.window_handles
for window in all_windows:
    if window != original_window:
        driver.switch_to.window(window)
        break
print("Current Tab Title:", driver.title)
driver.switch_to.window(original_window) #move back to orignal tab

#pop-up window
main_window = driver.current_window_handle
driver.find_element(By.XPATH,'//*[@id="PopUp"]').click()
time.sleep(2)
all_windows = driver.window_handles
for handle in all_windows:
    if handle != main_window:
        driver.switch_to.window(handle)
        break
print("Popup Title:", driver.title)
driver.close()
driver.switch_to.window(main_window)
print("Back to Main Window:", driver.title)


#mouse hover
point_me = driver.find_element(By.XPATH,'//*[@id="HTML3"]/div[1]/div/button')
act = ActionChains(driver)
act.move_to_element(point_me).perform()
time.sleep(4)

#doublr_click
fill_input(driver,'field1',"Hello There!!")
double_click = driver.find_element(By.XPATH,'//*[@id="HTML10"]/div[1]/button')
act.double_click(double_click).perform()
time.sleep(4)

#Drag and Drop
drag_ele = driver.find_element(By.XPATH,'//*[@id="draggable"]')
drop_ele = driver.find_element(By.XPATH,'//*[@id="droppable"]')
act.drag_and_drop(drag_ele,drop_ele).perform()
time.sleep(4)

#slider
min_slider = driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[1]') #{'x': 975, 'y': 2047}
max_slider = driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[2]') #{'x': 1105, 'y': 2047}
print(min_slider.location ,'\n', max_slider.location)

act.drag_and_drop_by_offset(min_slider,25,0).perform()
act.drag_and_drop_by_offset(max_slider,95,0).perform()
print(min_slider.location ,'\n', max_slider.location)

#scrolling dropdown
driver.find_element(By.ID,'comboBox').click()
container =  driver.find_element(By.ID,'dropdown')
target = 'Item 38'
options = driver.find_elements(By.XPATH,"//div[@class='option']")
found =  False
for option in options:
    driver.execute_script("arguments[0].scrollIntoView();", option)
    if option.text.strip() == target:
        option.click()
        found = True
        break
time.sleep(4)

#Handle Links
all_links = driver.find_elements(By.XPATH,"//a[@class='link']")
count = 0

for link in all_links:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None
    if res.status_code>=400:
        print(url, " is broken link")
        count+=1
    else:
        print(url, " is valid link")

print("total no of broken links:",count)

#static table
rows = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")
print("No. of rows -> ",len(rows))

cols = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr/th")
print("No of cols -> ",len(cols))

#read all data from table
for r in range(2,len(rows)+1):
    for c in range(1,len(cols)+1):
        data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]")
        print(data.text,end=' | ')
    print()
#
# Dynamic Table
wait = WebDriverWait(driver, 10, poll_frequency=2 , ignored_exceptions=[Exception])

headers = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "//table[@id='taskTable']/thead/tr/th")))
header_text = [h.text for h in headers]
print("{:<20} {:<10} {:<15} {:<15} {:<15}".format(*header_text))
print("-" * 80)

# Get all table rows (not just cells)
rows = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "//table[@id='taskTable']/tbody/tr")))

# Loop through each row and print the columns
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    data = [col.text for col in cols]
    print("{:<20} {:<10} {:<15} {:<15} {:<15}".format(*data))


#Pagination Web Table
# total_rows = 0
# total_cols = 0
# page = 1
# pagination_links = driver.find_elements(By.XPATH, "//a[@href='#']")
#
# total_pages = len(pagination_links)
# print(f"Total Pages Found: {total_pages}")
# while True:
#     print(f"\n Page {page}")
#
#     #click all checkboxes
#     checkboxes = driver.find_elements(By.XPATH,"//table[@id='productTable']/tbody/tr/td[4]/input[@type='checkbox']")
#     for checkbox in checkboxes:
#         if not checkbox.is_selected():
#             checkbox.click()

total_pages = len(driver.find_elements(By.XPATH, "//ul[@class='pagination']/li"))

for page in range(1, total_pages + 1):
    # Wait and get all checkboxes on current page
    checkboxes = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//table[@id='productTable']/tbody/tr/td/input[@type='checkbox']"))
    )

    # Click only if not already selected
    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()

    # Move to next page if not the last one
    if page < total_pages:
        next_page = driver.find_element(By.XPATH, f"//ul[@class='pagination']/li[{page + 1}]/a")
        next_page.click()
        time.sleep(1)

# Shadow DOM
shadow_host = driver.find_element(By.ID, "shadow_host")
shadow_root = shadow_host.shadow_root

input1 = shadow_root.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("Aniket")
input2 = shadow_root.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
input2.click()
input3 = shadow_root.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(
    r"C:\Users\anike\Downloads\Ge_intro.docx"
)

blog_link = shadow_root.find_element(By.CSS_SELECTOR, "a[href='https://www.pavantestingtools.com/']")
driver.execute_script("arguments[0].click();", blog_link)

driver.back()
driver.quit()

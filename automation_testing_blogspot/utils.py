from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def fill_input(driver, element_id, value, clear_before=True):
    element = driver.find_element(By.ID, element_id)
    if clear_before:
        try:
            element.clear()
        except:
            print(f"[WARN] Could not clear input with ID: {element_id}")
    element.send_keys(value)

def click_element(driver, element_id):
    driver.find_element(By.ID, element_id).click()

def click_checkboxes(driver, xpath):
    checkboxes = driver.find_elements(By.XPATH, xpath)
    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()

def select_from_dropdown(driver, element_id, value):
    element = driver.find_element(By.ID, element_id)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    select = Select(element)
    select.select_by_visible_text(value)


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def fill_input(driver , element_id , value , clear_before = True):
    element = driver.find_element(By.ID,element_id)
    if clear_before:
        try:
            element.clear()
        except:
            print("Element cant be cleared",{element_id})
    element.send_keys(value)


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://spcentral.amazon.in/ap/register?clientContext=259-1527148-6422162&openid.return_to=https%3A%2F%2Fspcentral.amazon.in%2F&prevRID=MM71CRR6WDGXTM5MPBTA&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_spc_desktop_in&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=amzn_spc_desktop_in&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
driver.maximize_window()

fill_input(driver,'ap_customer_name','Aniket Sonar')
fill_input(driver,'ap_email','aniketkojobdilao@gmail.com')
fill_input(driver,'ap_password','Password')
fill_input(driver,'ap_password_check','Password')

driver.find_element(By.XPATH,'//*[@id="continue"]').click()
time.sleep(10)



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from  selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options()
options.add_experimental_option("detach", True)

# if __name__ =='__main__':
s = Service("C:\sele\chrom\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)
driver.get('https://rahulshettyacademy.com/AutomationPractice/') # here location of the testing website 
driver.maximize_window()
print(driver.window_handles)
print("**************")

window= driver.find_element(By.ID,"openwindow")
window.click()
time.sleep(2)
tab = driver.find_element(By.ID,"opentab")
tab.click()
time.sleep(2)
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])# because , 1 , we are going to the next window or we are fetching the next id that is opentab
# driver.find_element() ----> then we should perform a new task in the window 
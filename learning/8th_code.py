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
frames = driver.find_element(By.XPATH , '//*[@id="courses-iframe"]')
driver.switch_to.frame(frames)
time.sleep(2)
driver.find_element("xpath","/html/body/div/header/div[3]/div/div/div[2]/nav/div[2]/ul/li[2]/a").click()

driver.switch_to.default_content()
time.sleep(2)
driver.find_element("xpath",'//*[@id="name"]').send_keys("rakesh")
# to come back to default content
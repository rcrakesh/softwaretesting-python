import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from  selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

# if __name__ =='__main__':
s = Service("C:\sele\chrom\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
    # print(driver.title)
    # print(driver.current_url)
    # driver.find_element(By.NAME , "enter-name").send_keys("rakesh r c ")
driver.find_element(By.ID , "checkBoxOption1").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='checkBoxOption3']").click()
time.sleep(5)
driver.find_element(By.NAME , "enter-name").send_keys("rakesh")
time.sleep(5)
# driver.find_element(By.LINK_TEXT , "Free Access to InterviewQues/ResumeAssistance/Material").click()
# time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/fieldset/label[2]/input").click()
time.sleep(2)
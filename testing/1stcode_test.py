import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from  selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.select import Select
import pytest 


def test_1st():
    options = Options()
    options.add_experimental_option("detach", True)

    # if __name__ =='__main__':
    s = Service("C:\\sele\\chrom\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get('https://rahulshettyacademy.com/AutomationPractice/')
    driver.maximize_window()
    driver.find_element(By.ID , "checkBoxOption1").click()
    time.sleep(2)
def test_2nd():
    options = Options()
    options.add_experimental_option("detach", True)

    # if __name__ =='__main__':
    s = Service("C:\\sele\\chrom\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get('https://rahulshettyacademy.com/AutomationPractice/')
    driver.maximize_window()
    driver.find_element(By.XPATH,"//*[@id='checkBoxOption3']").click()
    time.sleep(2)
def test_3rd():
    options = Options()
    options.add_experimental_option("detach", True)

    # if __name__ =='__main__':
    s = Service("C:\\sele\\chrom\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get('https://rahulshettyacademy.com/AutomationPractice/')
    driver.maximize_window()
    driver.find_element(By.NAME , "enter-name").send_keys("rakesh")
    time.sleep(2)
def test_4th():
    options = Options()
    options.add_experimental_option("detach", True)

    # if __name__ =='__main__':
    s = Service("C:\\sele\\chrom\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get('https://rahulshettyacademy.com/AutomationPractice/')
    driver.maximize_window()
    driver.find_element(By.LINK_TEXT , "Free Access to InterviewQues/ResumeAssistance/Material").click()
    time.sleep(2)
def test_5th():
    options = Options()
    options.add_experimental_option("detach", True)

    # if __name__ =='__main__':
    s = Service("C:\\sele\\chrom\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get('https://rahulshettyacademy.com/AutomationPractice/')
    driver.maximize_window()
    drop = driver.find_element(By.ID , "dropdown-class-example")# here we can use the xpath also by seeing the chrome browser 
    select = Select(drop)
    select.select_by_index(2) 
    time.sleep(2)
def test_6th():
    options = Options()
    options.add_experimental_option("detach", True)

    # if __name__ =='__main__':
    s = Service("C:\\sele\\chrom\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get('https://rahulshettyacademy.com/AutomationPractice/')
    driver.maximize_window()
    blink = driver.find_element(By.CLASS_NAME,"blinkingText")
    print(blink.text)
    print(blink.get_attribute("href"))
    time.sleep(2)
def test_7th():
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
    driver.switch_to.window(driver.window_handles[1])    
def test_8th():
    options = Options()
    options.add_experimental_option("detach", True)

    # if __name__ =='__main__':
    s = Service("C:\sele\chrom\chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options)
    driver.get('https://rahulshettyacademy.com/AutomationPractice/') # here location of the testing website 
    driver.maximize_window()
    driver.find_element(By.XPATH,"/html/body/header/div/a/button").click()
    time.sleep(2)
def test_9th():
    options = Options()
    options.add_experimental_option("detach", True)

    # if __name__ =='__main__':
    s = Service("C:\sele\chrom\chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options)
    driver.get('https://rahulshettyacademy.com/AutomationPractice/') # here location of the testing website 
    driver.maximize_window()
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/fieldset/label[1]/input").click()
    time.sleep(2) 
def test_10th():
    options = Options()
    options.add_experimental_option("detach", True)

    # if __name__ =='__main__':
    s = Service("C:\sele\chrom\chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options)
    driver.get('https://rahulshettyacademy.com/AutomationPracticeaaaa/') # here location of the testing website 
    driver.maximize_window()
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/fieldset/label[3]/input").click()
    time.sleep(2)       

   
# pytest for full 
# pytest -s 
# pytest -v
# pytest -s -v
# pytest --html=myreport.html -s -v 






# ------------------------------------------------------------------------------------------------




#assert if , if false them print this 
# # print("tihis is my first test")
# @pytest.mark.skip is to skip the function and import pytest     
# @pytest.mark.runthis  is to runthis function and import pytest  
# @pytest.mark.xfail   is putting that function to xfail condtion .. not in fail condition 


### for only the particular case to run " pytest -s -v test_1stcode.py::test_3rdtest " in the terminal 
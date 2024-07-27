from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from  selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


options = Options()
options.add_experimental_option("detach", True)

# if __name__ =='__main__':
s = Service("C:\sele\chrom\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)
driver.get('https://rahulshettyacademy.com/AutomationPractice/') # here location of the testing website 
driver.maximize_window()


# pipenv shell

# this is selenium slides "https://docs.google.com/presentation/d/1lKng7v8Pu8a6quciMcwQx2YQv9IyBL1C4cnfCpFB1oQ/edit#slide=id.g2184f451856_0_7"
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
driver.get('https://www.flipkart.com/') # here location of the testing website 
driver.maximize_window()
# WebDriverWait(driver , 2).until(EC.visibility_of_any_elements_located((By.XPATH, "//span[text()='✕']")))
# login = driver.find_element(By.XPATH,"//span[text()='✕']")
# login.click()
action = ActionChains(driver , duration=2000)
action.move_to_element(driver.find_element(By.XPATH,"//div/a[contains(@href,'/account/login?ret=/')]"))
action.click().perform()
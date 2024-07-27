import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from  selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = Options()
options.add_experimental_option("detach", True)

# if __name__ =='__main__':
s = Service("C:\sele\chrom\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://www.ajio.com/')
# driver.get('https://www.ajio.com/skybags-men-logo-print-backpack/p/460823558_grey')
driver.maximize_window()
time.sleep(2)
    # print(driver.title)
    # print(driver.current_url)
    # driver.find_element(By.NAME , "enter-name").send_keys("rakesh r c ")
driver.find_element(By.NAME , "searchVal").click()

driver.find_element(By.NAME , "searchVal").send_keys("laptop")
time.sleep(2)
driver.find_element(By.CLASS_NAME , "rilrtl-button").click()
time.sleep(2)
driver.find_element(By.XPATH , "/html/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div/div[1]/div/a/div/div[1]/div[1]/img").click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
wait = WebDriverWait(driver, 30)  # Wait up to 10 seconds
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "pdp-addtocart-button")))
element.click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR , ".pdp-cart-buttons .btn-cart").click()
time.sleep(5)
# driver.find_element(By.XPATH,"//*[@id='checkBoxOption3']").click()
# driver.find_element(By.NAME , "enter-name").send_keys("rakesh")
# driver.find_element(By.LINK_TEXT , "Free Access to InterviewQues/ResumeAssistance/Material").click()
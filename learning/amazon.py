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
driver.get('https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=155259815513&hvpone=&hvptwo=&hvadid=674842289437&hvpos=&hvnetw=g&hvrand=12712122684366303185&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062031&hvtargid=kwd-10573980&hydadcr=14453_2316415&gad_source=1')
driver.maximize_window()
    # print(driver.title)
    # print(driver.current_url)
    # driver.find_element(By.NAME , "enter-name").send_keys("rakesh r c ")
driver.find_element(By.ID , "twotabsearchtextbox").click()
time.sleep(2)
# driver.find_element(By.XPATH,"//*[@id='checkBoxOption3']").click()
driver.find_element(By.ID , "twotabsearchtextbox").send_keys("mobile")
time.sleep(3)
driver.find_element(By.ID , "nav-search-submit-button").click()
time.sleep(3)
driver.find_element(By.XPATH , "/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH ,"/html/body/div[2]/div/div[5]/div[3]/div[1]/div[4]/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div/div[38]/div[1]/span/span/span/input").click()
time.sleep(3)
driver.find_element(By.XPATH ,"/html/body/div[8]/div[3]/div[3]/div/div[1]/div[3]/div[1]/div[2]/div[3]/span/span").click()
time.sleep(3)
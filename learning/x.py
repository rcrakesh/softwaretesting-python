# //*[@id="radio-btn-example"]/fieldset/label[2]
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from  selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time 

options = Options()
options.add_experimental_option("detach", True)

s = Service(r"C:\sele\chrom\chromedriver.exe")

driver = webdriver.Chrome(service=s, options=options)
driver.get("https://www.ajio.com/")

driver.maximize_window()

driver.find_element(By.NAME , "searchVal").send_keys("rakesh")
time.sleep(3)

# <div class="react-autosuggest__container react-autosuggest__container--open"><input autocomplete="off" aria-label="Search Ajio" class="react-autosuggest__input react-autosuggest__input--open" placeholder="Search AJIO" name="searchVal" type="text" value=""></div>
from selenium import webdriver
import time
import sys
from selenium.webdriver.chrome.service import Service

# from webdriver_manager.chrome import ChromeDriverManager

def user_chat():
    pass

if __name__ == '__main__':
    s= Service("C:/sele/chrom/chromedriver.exe")
    # my_options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service= s)
    browser.get('https://www.youtube.com/watch?v=E_Zlm6dvhhY')

    time.sleep(20)
    
# chrom\chromedriver.exe

# driver = webdriver.Chrome("D://chromedriver.exe")
# driver.get('https://www.youtube.com/watch?v=ISc5_x_3MWM')
# time.sleep(3)
# driver.quit()

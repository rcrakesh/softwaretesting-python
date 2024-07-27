from selenium import webdriver
import time
import sys
from selenium.webdriver.chrome.service import Service

# from webdriver_manager.chrome import ChromeDriverManager
if __name__ == '__main__':
    s = Service("C:/sele/chrom/chromedriver.exe")
    my_option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=s, options= my_option)
    driver.get('https://www.youtube.com/watch?v=ISc5_x_3MWM')
    time.sleep(20)
    # driver.quit()

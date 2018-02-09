
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import bs4
from bs4 import BeautifulSoup
import urllib 
import requests
import json
import datetime
import webbrowser 



#function to replace the url 
def replace_in_url(url_name):
    if "01" in url_name:
        url1 = url_name.replace("01","02")
    elif "02" in url_name:
        url1 = url_name.replace("02","03")
    elif "03" in url_name:
        url1 = url_name.replace("03","04")
    else:
        url1 = url_name.replace("04","05") 

    return url1


import time 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException



#driver = webdriver.Chrome('C:\\Users\sravanthi.kanchi\AppData\Local\Programs\Python\Python36\chromedriver_win32.exe')  # Optional argument, if not specified will search path.
#driver.get('http://www.google.com/xhtml');
##time.sleep(10) # Let the user actually see something!
##search_box = driver.find_element_by_name('q')
##search_box.send_keys('ChromeDriver')
##search_box.submit()
##time.sleep(5) # Let the user actually see something!
##driver.quit()


## Creating chrome object - incognito mode  

option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# executable path -- link where we downloaded the chrome driver

browser = webdriver.Chrome(executable_path= 'C:\\Users\sravanthi.kanchi\AppData\Local\Programs\Python\Python36\chromedriver_win32\chromedriver.exe', chrome_options=option) 
url = "https://www.basketball-reference.com/players/j/jamesle01.html"
browser.get(url)

# Wait 50 seconds for page to load
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="all_per_minute"]')))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()
            


#totals table row year
totals_year_2018 = browser.find_elements_by_xpath('//*[@id="totals.2018"]/th/a')

if len(totals_year_2018):
    print("element present")
else:
    print("not present")
    new_url = replace_in_url(url)
    print(new_url)
    browser.get(new_url)
    

##data section 

#player position
totals_pos = browser.find_elements_by_xpath('//*[@id="totals.2018"]/td[4]')
if len(totals_pos) > 0:
    print("player position " + totals_pos[-1].text) 

#three pointers made
totals_fg3 = browser.find_elements_by_xpath('//*[@id="totals.2018"]/td[11]')
if len(totals_fg3) > 0:
    print("three pointers made "  + totals_fg3[-1].text)

#three pointers attempted
totals_fg3a = browser.find_elements_by_xpath('//*[@id="totals.2018"]/td[12]')
if len(totals_fg3a) > 0:
    print("three pointers attempted " + totals_fg3a[-1].text)

#no of games 
totals_g = browser.find_elements_by_xpath('//*[@id="totals.2018"]/td[5]')
print("no of games " + totals_g[-1].text)

#no of games started
totals_gs = browser.find_elements_by_xpath('//*[@id="totals.2018"]/td[6]')
print("no of games started " + totals_gs[-1].text) 

#total rebounds
totals_trb = browser.find_elements_by_xpath('//*[@id="totals.2018"]/td[23]')
total_rebounds = totals_trb[-1].text
print("total rebounds " + total_rebounds) 

    
#assists
totals_ast = browser.find_element_by_xpath('//*[@id="totals.2018"]/td[24]')
print("assists " + totals_ast.text)

    
#steals
totals_stl = browser.find_elements_by_xpath('//*[@id="totals.2018"]/td[25]')
print("steals "  + totals_stl[-1].text)
  
#blocks
totals_blk = browser.find_element_by_xpath('//*[@id="totals.2018"]/td[26]')
print("blocks " + totals_blk.text)

#turnovers
totals_tov = browser.find_elements_by_xpath('//*[@id="totals.2018"]/td[27]')
print("turnovers " + totals_tov[-1].text) 

#points 
totals_pts = browser.find_elements_by_xpath('//*[@id="totals.2018"]/td[29]')
print("points " + totals_pts[-1].text)



    


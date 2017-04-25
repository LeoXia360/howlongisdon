#import requests

import datetime
import pytz

from bs4 import BeautifulSoup

from pyvirtualdisplay import Display

from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#binary = FirefoxBinary('/Applications/Firefox.app')/usr/local/bin/geckodriver-0.16.0
#browser = webdriver.Firefox(firefox_binary=binary)
#browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
display = Display(visible=0, size=(1366, 768))
display.start()
browser = webdriver.Firefox()
browser.get('https://www.google.com/search?q=don+japanese+food+truck&ie=utf-8&oe=utf-8')
html_source = browser.page_source
browser.quit()
display.stop
display.popen.terminate()
soup = BeautifulSoup(html_source,'html.parser')

html = soup.prettify("utf-8")
with open("output.html", "wb") as file:
    file.write(html)
file.close()
print ("Updated")
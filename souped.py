#import requests

import datetime
import pytz

from bs4 import BeautifulSoup

#from selenium import webdriver  
#from selenium.common.exceptions import NoSuchElementException  
#from selenium.webdriver.common.keys import Keys  
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from flask import Flask
from flask import render_template
app = Flask(__name__)

#binary = FirefoxBinary('/Applications/Firefox.app')/usr/local/bin/geckodriver-0.16.0
#browser = webdriver.Firefox(firefox_binary=binary)

@app.route('/')
@app.route('/<name>')
def calculate(name=None):
    #browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
    #browser.get('https://www.google.com/search?q=don+japanese+food+truck&ie=utf-8&oe=utf-8')
    #html_source = browser.page_source
    #browser.quit()

    #soup = BeautifulSoup(html_source,'html.parser')

    #html = soup.prettify("utf-8")
    #with open("output.html", "rb") as file:
    #   file.write(html)
    #file.close()

    soup = BeautifulSoup(open("output.html"),'html.parser')

    current = soup.find("div", {"class": "lubh-bar lubh-sel"})
    if current is not None:
        #print(current['style'])
        print ("The wait time is about: " + str(int(int(current['style'][32:-2])*75/81)) + " minutes.")
    else:
        vals = soup.findAll("div", {"class": "lubh-bar"})
        #print (vals[20]['style'])
        tz = pytz.timezone('US/Central')
        time_now = datetime.datetime.now(tz)
        day = 'NONE'
        #print(time_now.hour)
        if time_now.weekday() == 0:
            if time_now.hour < 12:
                day = 'NONE'
            elif time_now.hour < 13:
                day = 'Mon1'
            elif time_now.hour < 14:
                day = 'Mon2'
            elif time_now.hour < 15:
                day = 'Mon3'
        elif time_now.weekday() == 1:
            if time_now.hour < 12:
                day = 'NONE'
            elif time_now.hour < 13:
                day = 'Tues1'
            elif time_now.hour < 14:
                day = 'Tues2'
            elif time_now.hour < 15:
                day = 'Tues3'
        elif time_now.weekday() == 2:
            if time_now.hour < 12:
                day = 'NONE'
            elif time_now.hour < 13:
                day = 'Wed1'
            elif time_now.hour < 14:
                day = 'Wed2'
            elif time_now.hour < 15:
                day = 'Wed3'
        elif time_now.weekday() == 3:
            if time_now.hour < 12:
                day = 'NONE'
            elif time_now.hour < 13:
                day = 'Thurs1'
            elif time_now.hour < 14:
                day = 'Thurs2'
            elif time_now.hour < 15:
                day = 'Thurs3'
        elif time_now.weekday() == 4:
            if time_now.hour < 12:
                day = 'NONE'
            elif time_now.hour < 13:
                day = 'Fri1'
            elif time_now.hour < 14:
                day = 'Fri2'
            elif time_now.hour < 15:
                day = 'Fri3'
        elif time_now.weekday() == 5:
            if time_now.hour < 12:
                day = 'NONE'
            elif time_now.hour < 13:
                day = 'Sat1'
            elif time_now.hour < 14:
                day = 'Sat2'
            elif time_now.hour < 15:
                day = 'Sat3'
        elif time_now.weekday() == 6:
            if time_now.hour < 12:
                day = 'NONE'
            elif time_now.hour < 13:
                day = 'Sun1'
            elif time_now.hour < 14:
                day = 'Sun2'
            elif time_now.hour < 15:
                day = 'Sun3'
        times = {
            'Mon1': vals[0]['style'][7:-2],
            'Mon2': vals[1]['style'][7:-2],
            'Mon3': vals[2]['style'][7:-2],
            'Tues1': vals[3]['style'][7:-2],
            'Tues2': vals[4]['style'][7:-2],
            'Tues3': vals[5]['style'][7:-2],
            'Wed1': vals[6]['style'][7:-2],
            'Wed2': vals[7]['style'][7:-2],
            'Wed3': vals[8]['style'][7:-2],
            'Thurs1': vals[9]['style'][7:-2],
            'Thurs2': vals[10]['style'][7:-2],
            'Thurs3': vals[11]['style'][7:-2],
            'Fri1': vals[12]['style'][7:-2],
            'Fri2': vals[13]['style'][7:-2],
            'Fri3': vals[14]['style'][7:-2],
            'Sat1': vals[15]['style'][7:-2],
            'Sat2': vals[16]['style'][7:-2],
            'Sat3': vals[17]['style'][7:-2],
            'Sun1': vals[18]['style'][7:-2],
            'Sun2': vals[19]['style'][7:-2],
            'Sun3': vals[20]['style'][7:-2],
            'NONE': "Sorry, Don is closed!"
        }

        if len(times[day]) > 3:
            with app.app_context():
                return render_template('index.html', name=times[day])
        else:
            with app.app_context():
                return render_template('index.html', name="The wait time is about: " + str(int(int(times[day])*75/81)) + " minutes.")



calculate()











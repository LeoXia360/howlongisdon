#import requests

import datetime
import pytz

from bs4 import BeautifulSoup

#from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from flask import Flask
import flask_login
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import os

app = Flask(__name__)
app.secret_key=os.urandom(12)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

users = {'howlongisdon': {'pw': 'test'}}

#binary = FirefoxBinary('/Applications/Firefox.app')/usr/local/bin/geckodriver-0.16.0
#browser = webdriver.Firefox(firefox_binary=binary)
class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['pw'] == users[email]['pw']

    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('admin.html')

    email = request.form['email']
    if request.form['pw'] == users[email]['pw']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for('protected'))

    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    return render_template('protected.html')

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect('http://www.howlongisdon.info/login')

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'




@app.route('/')
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

    soup = BeautifulSoup(open("/home/howlongisdon/mysite/output.html"))

    current = soup.find("div", {"class": "lubh-bar lubh-sel"})
    if current is not None:
        #print(current['style'])
        with app.app_context():
            return render_template('index.html', name=str(int(int(filter(str.isdigit, current['style']))*75/81)) + " minutes")
        #print ("The wait time is about: " + str(int(int(current['style'][32:-2])*75/81)) + " minutes.")
    else:
        vals = soup.findAll("div", {"class": "lubh-bar"})
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
            'Mon1': (filter(str.isdigit, vals[0]['style'])),
            'Mon2': (filter(str.isdigit, vals[1]['style'])),
            'Mon3': (filter(str.isdigit, vals[2]['style'])),
            'Tues1': (filter(str.isdigit, vals[3]['style'])),
            'Tues2': (filter(str.isdigit, vals[4]['style'])),
            'Tues3': (filter(str.isdigit, vals[5]['style'])),
            'Wed1': (filter(str.isdigit, vals[6]['style'])),
            'Wed2': (filter(str.isdigit, vals[7]['style'])),
            'Wed3': (filter(str.isdigit, vals[8]['style'])),
            'Thurs1': (filter(str.isdigit, vals[9]['style'])),
            'Thurs2': (filter(str.isdigit, vals[10]['style'])),
            'Thurs3': (filter(str.isdigit, vals[11]['style'])),
            'Fri1': (filter(str.isdigit, vals[12]['style'])),
            'Fri2': (filter(str.isdigit, vals[13]['style'])),
            'Fri3': (filter(str.isdigit, vals[14]['style'])),
            'Sat1': (filter(str.isdigit, vals[15]['style'])),
            'Sat2': (filter(str.isdigit, vals[16]['style'])),
            'Sat3': (filter(str.isdigit, vals[17]['style'])),
            'Sun1': (filter(str.isdigit, vals[18]['style'])),
            'Sun2': (filter(str.isdigit, vals[19]['style'])),
            'Sun3': (filter(str.isdigit, vals[20]['style'])),
            'NONE': "Sorry, Don is closed!"
        }

        if len(times[day]) > 3:
            with app.app_context():
                return render_template('index.html', name=times[day])
        else:
            with app.app_context():
                #print (times[day])
                return render_template('index.html', name=str(int(int(times[day])*75/81)) + " minutes")

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/admin.html')
def admin():
    return render_template('admin.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/reviews.html')
def reviews():
    return render_template('reviews.html')

@app.route('/', methods=['POST'])
def signup():
    text = request.form['email']
    flag = 0

    f = open('/home/howlongisdon/mysite/subscribers.txt','r')
    lines = f.readlines()
    f.close()

    f = open('/home/howlongisdon/mysite/subscribers.txt','w')
    for line in lines:
        if line != text + "\n" :
            f.write(line)
        else:
            flag = 1
    f.close()

    if flag == 0:
        with open ('/home/howlongisdon/mysite/subscribers.txt','a') as f:
            f.write(text + "\n")
        f.close()
    return ('', 204)

if __name__ == '__main__':
    app.debug = True
    app.run()









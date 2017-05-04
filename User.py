import smtplib
import datetime
import pytz
from bs4 import BeautifulSoup


soup = BeautifulSoup(open("/home/howlongisdon/mysite/output.html"))

current = soup.find("div", {"class": "lubh-bar lubh-sel"})
if current is not None:
    minutes = str(int(int(filter(str.isdigit, current['style']))*75/81))
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
        minutes = "0";
    else:
        minutes = str(int(int(times[day])*75/81))

if minutes != "0":
    with open("/home/howlongisdon/mysite/subscribers.txt") as f:
        content = f.readlines()
    f.close()
    # remove whitespace at the end of each line
    content = [x.strip() for x in content]

    #ALLOW LESS SECURE APPS ON GOOGLE
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("howlongisdon@gmail.com", "donislong")

    for email in content:
        subject = 'Subject: Estimated Time Right Now\n'
        msg = subject + 'The estimated wait time for Don Japanese Food Truck is currently ' + minutes + ' minutes!\n\n\nPlease resubmit the form on our website if you wish to unsubscribe to these notifications.'
        server.sendmail("howlongisdon@gmail.com", email, msg)
        print "Sent to " + email
    server.quit
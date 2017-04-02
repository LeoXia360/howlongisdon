import smtplib

#ALLOW LESS SECURE APPS ON GOOGLE
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("howlongisdon@gmail.com", "donislong")
 
subject = 'Subject: Testing Mail\n'
msg = subject +  'fyoure gr8!'
server.sendmail("leoxia@utexas.edu", "schilukuri@utexas.edu", msg)
server.quit
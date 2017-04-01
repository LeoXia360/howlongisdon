import smtplib

#ALLOW LESS SECURE APPS ON GOOGLE
server = smtplib.SMTP('smtp.gmail.com', 587)
()server.starttls()
server.login("leoxia@utexas.edu", "password")
 
msg = "fyoure gr8!"
server.sendmail("leoxia@utexas.edu", "schilukuri@utexas.edu", msg)
server.quit
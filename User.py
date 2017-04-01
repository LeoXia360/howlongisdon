import smtplib

#ALLOW LESS SECURE APPS ON GOOGLE
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("leoxia@utexas.edu", "le0ishgg")
 
msg = "fyoure gr8!"
server.sendmail("leoxia@utexas.edu", "schilukuri@utexas.edu", msg)
server.quit()
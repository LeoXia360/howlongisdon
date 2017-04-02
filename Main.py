from Owner import Owner
from mod_python import apache

x = Owner('don_owner')
y = False

while(y == False):
    y = x.login()
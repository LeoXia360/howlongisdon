#MAKE SURE THIS IS SITE IS NOT CODE INJECTABLE
from cryptography.fernet import Fernet

"""Owner class uses the Singleton design pattern
	We don't want multiple people to be able create accounts
	only one master account for Don's owner."""

class Owner():
    #only allows one Owner object to be created


    class __Owner():
        """Regular methods are in here so they can't be accessed"""

        logged_in = False
        cipher_suite = None
        cipher_username = ""
        cipher_password = ""
        subscriber_list = []

        def __init__(self, arg):
            self.val = arg
            self.key = Fernet.generate_key()
            username = raw_input('Create Username: ')
            password = raw_input('Create Password: ')

            self.cipher_suite = Fernet(self.key)
            self.cipher_username = self.cipher_suite.encrypt(username)
            self.cipher_password = self.cipher_suite.encrypt(password)

        def login(self):
            """Allows the user to login allows access to other features"""
            entered_username = raw_input('Enter your username: ')
            entered_password = raw_input('Enter your password: ')
            cipher_suite = Fernet(self.key)
            username = self.cipher_suite.decrypt(self.cipher_username)
            password = self.cipher_suite.decrypt(self.cipher_password)
            if (entered_username == username) and (entered_password == password):
                logged_in = True
                print "log in successful"
                return True
            else:
                print "log in failed"
                return False


        def logout(self):
            """Allows the user to logout prevents access to other features"""
            print "logging out..."
            logged_in = False

        def manually_send_newsletter(self):
            """Allows user to manually send out a notification to all subscribers"""
            if not logged_in:
                print "Sorry, you cannot access this you are not logged in."
                return

        def update_coupon_code(self):
            """Allows user to update the coupon code on the website"""
            if not logged_in:
                print "Sorry, you cannot access this you are not logged in."
                return

    instance = None

    def __init__(self, arg):
        if not Owner.instance:
            Owner.instance = Owner.__Owner(arg)
        else:
            Owner.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)










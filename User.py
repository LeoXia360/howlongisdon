#MAKE SURE THIS IS SITE IS NOT CODE INJECTABLE

"""User class uses the Singleton design pattern
	We don't want multiple people to be able create accounts
	only one master account for Don's owner."""

class User:
    #only allows one user object to be created
    class __User:
        """Regular methods are in here so they can't be accessed"""

        logged_in = False
        __username = ""
        __password = ""

        def __init__(self, arg):
            self.val = arg
        def login(self):
            """Allows the user to login allows access to other features"""
            print "logging in..."

            #Code HERE

            logged_in = True

        def logout(self):
            """Allows the user to logout prevents access to other features"""
            print "logging out..."

            #Code here

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
        if not User.instance:
            User.instance = User.__User(arg)
        else:
            User.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)

    

x = User('leo');
x.login()





"""User class uses the Singleton design pattern
	We don't want multiple people to be able create accounts
	only one master account for Don's owner."""

class User:
    #only allows one user object to be created
    class __User:
        def __init__(self, arg):
            self.val = arg

    instance = None
    logged_in = False

    def __init__(self, arg):
        if not User.instance:
            User.instance = User.__User(arg)
        else:
            User.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def login():
        """Allows the user to login
        allows access to other features"""


        #Code HERE

        logged_in = True

    def logout():
        """Allows the user to logout
        prevents access to other features"""

        #Code here

        logged_in = False


    def manually_send_newsletter():
        """Allows user to manually send out a notification
        to all subscribers"""
        if not logged_in:
            return

    def update_coupon_code():
        """Allows user to update the coupon code on the website"""
        if not logged_in:
            return






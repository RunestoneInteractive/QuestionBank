.. activecode:: c1a
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: ClassesBasics
    :subchapter: UserDefinedClasses
    :topics: ClassesBasics/UserDefinedClasses
    :from_source: None

    class Account:
        '''Account class to model bank accounts'''

        def __init__(self, name):
            '''Create a new account for owner name and a zero balance'''
            self.owner = name
            self.balance = 0.00

    p = Account('Jan')        # Instantiate an object of type Account
    q = Account('Dan')        # and make a second Account

    print("Nothing seems to have happened with the accounts")
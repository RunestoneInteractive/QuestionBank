.. activecode:: c1d
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: ClassesBasics
    :subchapter: MethodswithParameters
    :topics: ClassesBasics/MethodswithParameters
    :from_source: None

    class Account:
        '''Account class to model bank accounts'''

        def __init__(self, name):
            '''Create a new account for owner name and a zero balance'''
            self.owner = name
            self.balance = 0.00

        def getBalance(self):
            return self.balance

        def deposit(self, amount):
            self.balance += amount

        def withdraw(self, amount):
            self.balance -= amount


    p = Account('Jan')
    print(p.getBalance())

    print(p.getBalance())

    print(p.getBalance())
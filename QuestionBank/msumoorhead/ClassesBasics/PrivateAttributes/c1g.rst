.. activecode:: c1g
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: ClassesBasics
    :subchapter: PrivateAttributes
    :topics: ClassesBasics/PrivateAttributes
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
            '''increase balance by a positive amount'''
            if amount >= 0:
                self.balance += amount

        def withdraw(self, amount):
            '''reduce balance by amount but do not an allow overdraft'''
            if self.balance >= amount:
                self.balance -= amount

    p = Account('Jan')
    print(p.getBalance())
    p.balance = -12345     # trying to directly change the attribute
    print(p.getBalance())  # notice what is displayed
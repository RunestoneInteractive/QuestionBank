.. activecode:: c1j
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: ClassesBasics
    :subchapter: ConvertinganObjecttoaString
    :topics: ClassesBasics/ConvertinganObjecttoaString
    :from_source: None

    class Account:
        '''Account class to model bank accounts'''

        def __init__(self, name):
            '''Create a new account for owner name and a zero balance'''
            self.__owner = name
            self.__balance = 0.00

        def getBalance(self):
            return self.__balance

        def deposit(self, amount):
            '''increase balance by a positive amount'''
            if amount >= 0:
                self.__balance += amount

        def withdraw(self, amount):
            '''reduce balance by amount but do not an allow overdraft'''
            if self.__balance >= amount:
                self.__balance -= amount

        def __str__(self):
            return "{} ${:,.2f}".format(self.__owner, self.__balance)

    p = Account('Jan')
    p.deposit(150)
    print(str(p))
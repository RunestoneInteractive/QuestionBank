.. activecode:: c2a
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: ClassesDiggingDeeper
    :subchapter: Inheritance
    :topics: ClassesDiggingDeeper/Inheritance
    :from_source: None

    class Account:
        def __init__(self, name):
            self.__owner = name
            self.__balance = 0.00

        def getBalance(self):
            return self.__balance

        def deposit(self, amount):
            self.__balance += amount

        def withdraw(self, amount):
            if self.__balance >= amount:
                self.__balance -= amount

        def __str__(self):
            return "{} ${:,.2f}".format(self.__owner, self.__balance)

    class LOC(Account):
        '''LOC inherits everything from Account'''

    a = LOC('Jan')
    a.deposit(100)
    print(a)
    a.withdraw(300)
    print(a.getBalance())
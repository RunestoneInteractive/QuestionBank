.. activecode:: c2e
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: ClassesDiggingDeeper
    :subchapter: Decorators
    :topics: ClassesDiggingDeeper/Decorators
    :from_source: None

    class CAD:
        """Canadian Dollar"""
        __USD = 0.75   # the value of a CAD in terms of a USD (private)
        def __init__(self, amt):
            self.__amount = amt

        def getAmount(self):
            return self.__amount

        def exchange(self):
            return self.__amount * CAD.__USD # using class attribute

        @staticmethod
        def changeRate(rate):
            CAD.__USD = rate # change the class exchange rate

    c = CAD(100) # 100 Canadian dollars
    print(c.getAmount(), 'Canadian dollars is worth')
    print(c.exchange(), 'US dollars')
    print('changing the exchange rate')
    CAD.changeRate(0.8)
    print(c.exchange(), 'US dollars')
.. activecode:: c2g
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: ClassesDiggingDeeper
    :subchapter: Decorators
    :topics: ClassesDiggingDeeper/Decorators
    :from_source: None

    class CAD:
        """Canadian Dollar"""
        def __init__(self, amt):
            self.__amount = amt

        @property
        def amount(self):
            return self.__amount

        @amount.setter
        def amount(self, amt):
            if amt >= 0:
                self.__amount = amt


    c = CAD(0)
    print(c.amount)
    c.amount = 100            #using the setter property
    print(c.amount)
    c.amount = c.amount - 30  #using both getter and setter properties
    print(c.amount)
    c.amount = -10 # notice the object does not go to an illegal state
    print(c.amount)
.. activecode:: c2f
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


    c = CAD(100)
    print(c.amount)
    d = CAD(50)
    print(c.amount + d.amount)
.. activecode:: c2t
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: ClassesDiggingDeeper
    :subchapter: Polymorphism
    :topics: ClassesDiggingDeeper/Polymorphism
    :from_source: None

    class Fraction:
        def __init__(self, top, bottom):
            self.__num = top        # the numerator is on top
            self.__den = bottom     # the denominator is on the bottom

        def __str__(self):
            return '{}/{}'.format(self.__num, self.__den)


    a = 100
    b = 1.23
    c = Fraction(6,5)
    print(isinstance(a, int))
    print(isinstance(b, float))
    print(isinstance(c, Fraction))
    print(isinstance(a, (int,float)))
    print(isinstance(c, (int,float)))
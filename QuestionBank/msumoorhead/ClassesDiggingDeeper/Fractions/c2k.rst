.. activecode:: c2k
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: ClassesDiggingDeeper
    :subchapter: Fractions
    :topics: ClassesDiggingDeeper/Fractions
    :from_source: None

    class Fraction:
        def __init__(self, top, bottom):
            self.__num = top        # the numerator is on top
            self.__den = bottom     # the denominator is on the bottom

        def __str__(self):
            return '{}/{}'.format(self.__num, self.__den)

        @property
        def num(self):
            return self.__num

        @property
        def den(self):
            return self.__den

    myfraction = Fraction(3, 4)
    print(myfraction)
    print(myfraction.num)
    print(myfraction.den)
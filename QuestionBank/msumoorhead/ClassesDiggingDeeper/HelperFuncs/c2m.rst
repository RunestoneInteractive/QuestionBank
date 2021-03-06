.. activecode:: c2m
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: ClassesDiggingDeeper
    :subchapter: HelperFuncs
    :topics: ClassesDiggingDeeper/HelperFuncs
    :from_source: None

    def gcd(m, n):
        while m % n != 0:
            oldm = m
            oldn = n
            m = oldn
            n = oldm % oldn
        return n

    class Fraction:
        def __init__(self, top, bottom):
            self.__num = top        # the numerator is on top
            self.__den = bottom     # the denominator is on the bottom

        def __str__(self):
            return '{}/{}'.format(self.__num, self.__den)

        def simplify(self):
            common = gcd(self.__num, self.__den)
            return Fraction(self.__num // common, self.__den // common)

    myfraction = Fraction(12, 16)
    print(myfraction)
    newfraction = myfraction.simplify()
    print(newfraction)
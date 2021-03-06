.. activecode:: c2s
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: ClassesDiggingDeeper
    :subchapter: ArithmeticMethods
    :topics: ClassesDiggingDeeper/ArithmeticMethods
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

        @property
        def num(self):
            return self.__num

        @property
        def den(self):
            return self.__den

        def __add__(self,other):
            newnum = self.__num * other.__den + self.__den * other.__num
            newden = self.__den * other.__den
            common = gcd(newnum, newden)
            return Fraction(newnum // common, newden // common)

    if __name__ == "__main__":
        import test
        f1 = Fraction(1, 6)
        f2 = Fraction(1, 2)
        f3 = f1 + f2
        test.testEqual(f3.num, 2)
        test.testEqual(f3.den, 3)
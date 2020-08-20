.. activecode:: fractions_is
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: ClassesDiggingDeeper
    :subchapter: Sameness
    :topics: ClassesDiggingDeeper/Sameness
    :from_source: T

    class Fraction:

        def __init__(self, top, bottom):

            self.num = top        # the numerator is on top
            self.den = bottom     # the denominator is on the bottom

        def __str__(self):
            return str(self.num) + "/" + str(self.den)


    myfraction = Fraction(3, 4)
    yourfraction = Fraction(3, 4)
    print(myfraction is yourfraction)

    ourfraction = myfraction
    print(myfraction is ourfraction)
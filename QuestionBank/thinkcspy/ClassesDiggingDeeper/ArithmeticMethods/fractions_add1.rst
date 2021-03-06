.. activecode:: fractions_add1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: ClassesDiggingDeeper
    :subchapter: ArithmeticMethods
    :topics: ClassesDiggingDeeper/ArithmeticMethods
    :from_source: T
    :pct_on_first: 0.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 5.0

    def gcd(m, n):
        while m % n != 0:
            oldm = m
            oldn = n
    
            m = oldn
            n = oldm % oldn
    
        return n
    
    class Fraction:
    
        def __init__(self, top, bottom):
    
            self.num = top        # the numerator is on top
            self.den = bottom     # the denominator is on the bottom
    
        def __str__(self):
            return str(self.num) + "/" + str(self.den)
    
        def simplify(self):
            common = gcd(self.num, self.den)
    
            self.num = self.num // common
            self.den = self.den // common
    
        def add(self,otherfraction):
    
            newnum = self.num*otherfraction.den + self.den*otherfraction.num
            newden = self.den * otherfraction.den
    
            common = gcd(newnum, newden)
    
            return Fraction(newnum // common, newden // common)
    
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 4)
    
    f3 = f1.add(f2)
    print(f3)
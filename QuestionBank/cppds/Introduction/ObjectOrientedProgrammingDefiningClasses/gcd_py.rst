.. activecode:: gcd_py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: ObjectOrientedProgrammingDefiningClasses
    :topics: Introduction/ObjectOrientedProgrammingDefiningClasses
    :from_source: T
    :optional:

    def gcd(m,n):
        while m%n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm%oldn
        return n

    print(gcd(20,10))
.. activecode::  gcd_cl
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: Introduction
    :subchapter: ObjectOrientedProgramminginPythonDefiningClasses
    :topics: Introduction/ObjectOrientedProgramminginPythonDefiningClasses
    :from_source: T
    :caption: The Greatest Common Divisor Function

    def gcd(m, n):
        while m % n != 0:
            m, n = n, m % n
        return n

    print(gcd(20, 10))
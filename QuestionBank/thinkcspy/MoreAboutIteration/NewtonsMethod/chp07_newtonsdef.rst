.. activecode:: chp07_newtonsdef
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: MoreAboutIteration
    :subchapter: NewtonsMethod
    :topics: MoreAboutIteration/NewtonsMethod
    :from_source: T

    def newtonSqrt(n, howmany):
        approx = 0.5 * n
        for i in range(howmany):
            betterapprox = 0.5 * (approx + n/approx)
            approx = betterapprox
        return betterapprox

    print(newtonSqrt(100, 10))
    print(newtonSqrt(4, 10))
    print(newtonSqrt(1, 10))
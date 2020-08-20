.. activecode:: itl
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: MoreAboutIteration
    :subchapter: Newton'sMethod
    :topics: MoreAboutIteration/Newton'sMethod
    :from_source: None

    def newtonSqrt(n, howmany):
        approx = 0.5 * n
        for i in range(howmany):
            betterapprox = 0.5 * (approx + n/approx)
            approx = betterapprox
        return betterapprox

    print(newtonSqrt(100, 10))
    print(newtonSqrt(4, 10))
    print(newtonSqrt(1, 10))
.. codelens:: chp07_newtonswhile
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: MoreAboutIteration
    :subchapter: NewtonsMethod
    :topics: MoreAboutIteration/NewtonsMethod
    :from_source: T

    def newtonSqrt(n):
        approx = 0.5 * n
        better = 0.5 * (approx + n/approx)
        while better != approx:
            approx = better
            better = 0.5 * (approx + n/approx)
        return approx

    print(newtonSqrt(10))
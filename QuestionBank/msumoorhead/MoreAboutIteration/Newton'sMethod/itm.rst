.. activecode:: itm
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: MoreAboutIteration
    :subchapter: Newton'sMethod
    :topics: MoreAboutIteration/Newton'sMethod
    :from_source: None

    def sqrt(n):
        approx = 0.5 * n
        better = 0.5 * (approx + n/approx)
        while better != approx:
            approx = better
            better = 0.5 * (approx + n/approx)
        return approx

    print(sqrt(100))
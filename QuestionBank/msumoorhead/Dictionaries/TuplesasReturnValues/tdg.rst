.. activecode:: tdg
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Dictionaries
    :subchapter: TuplesasReturnValues
    :topics: Dictionaries/TuplesasReturnValues
    :from_source: None


    def circleInfo(r):
        """ Return (circumference, area) of a circle of radius r """
        c = 2 * 3.14159 * r
        a = 3.14159 * r * r
        return (c, a)

    (circum, area) = circleInfo(10)
    print('area =', area)
    print('circumference =', circum)

    t = circleInfo(10)
    print(t)
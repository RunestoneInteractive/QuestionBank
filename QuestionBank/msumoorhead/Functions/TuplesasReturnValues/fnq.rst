.. activecode:: fnq
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Functions
    :subchapter: TuplesasReturnValues
    :topics: Functions/TuplesasReturnValues
    :from_source: None


    def circleInfo(r):
        """ Return (circumference, area) of a circle of radius r """
        c = 2 * 3.14159 * r
        a = 3.14159 * r * r
        return (c, a)

    result = circleInfo(10)
    print('circumference and area are:', result)
    (circum, area) = circleInfo(10)
    print('circumference =', circum)
    print('area =', area)
.. activecode:: chp09_tuple3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Lists
    :subchapter: TuplesasReturnValues
    :topics: Lists/TuplesasReturnValues
    :from_source: T
    :pct_on_first: 0.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 3.0

    
    def circleInfo(r):
        """ Return (circumference, area) of a circle of radius r """
        c = 2 * 3.14159 * r
        a = 3.14159 * r * r
        return (c, a)
    
    print(circleInfo(10))
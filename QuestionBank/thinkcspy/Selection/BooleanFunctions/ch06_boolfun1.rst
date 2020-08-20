.. activecode:: ch06_boolfun1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Selection
    :subchapter: BooleanFunctions
    :topics: Selection/BooleanFunctions
    :from_source: T
    :pct_on_first: 1.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 1.0

    def isDivisible(x, y):
        if x % y == 0:
            result = True
        else:
            result = False
    
        return result
    
    print(isDivisible(10, 5))
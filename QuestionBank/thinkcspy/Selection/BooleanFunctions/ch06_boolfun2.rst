.. activecode:: ch06_boolfun2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Selection
    :subchapter: BooleanFunctions
    :topics: Selection/BooleanFunctions
    :from_source: T

    def isDivisible(x, y):
        return x % y == 0

    if isDivisible(10, 5):
        print("That works")
    else:
        print("Those values are no good")
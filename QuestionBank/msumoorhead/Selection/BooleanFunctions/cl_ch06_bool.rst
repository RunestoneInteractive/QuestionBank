.. codelens:: cl_ch06_bool
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Selection
    :subchapter: BooleanFunctions
    :topics: Selection/BooleanFunctions
    :from_source: None
    :showoutput:

    def isDivisible(x, y):
        if x % y == 0:
            result = True
        else:
            result = False

        return result

    if isDivisible(10, 5):
        print("That works")
    else:
        print("Those values are no good")
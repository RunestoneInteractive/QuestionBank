.. activecode:: bol
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Selection
    :subchapter: BooleanFunctions
    :topics: Selection/BooleanFunctions
    :from_source: None

    def isDivisible(x, y):
        '''is x evenly divisible by y?'''
        if x % y == 0:
            result = True
        else:
            result = False

        return result

    print(isDivisible(10, 5))
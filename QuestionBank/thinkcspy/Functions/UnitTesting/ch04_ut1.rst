.. activecode:: ch04_ut1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: UnitTesting
    :topics: Functions/UnitTesting
    :from_source: T

    def square(x):
        '''raise x to the second power'''
        return x * x

    import test
    print('testing square function')
    test.testEqual(square(10), 100)
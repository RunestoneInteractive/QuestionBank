.. activecode:: fnj
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Functions
    :subchapter: UnitTesting
    :topics: Functions/UnitTesting
    :from_source: None
    :nocodelens:

    def square(x):
        '''raise x to the second power'''
        return x * x

    import test
    print('testing square function')
    test.testEqual(square(10), 100)
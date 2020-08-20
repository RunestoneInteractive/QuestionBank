.. activecode:: list_writeMiddleq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-WriteCode
    :topics: 08-lists/08-WriteCode
    :from_source: T

    Write a function called ``middle`` that takes a list as its argument and
    returns a new list that contains all but the first and last elements.
    ~~~~
    def middle():

    ====
    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(middle([1,2,3,4,5]),[2,3,4],"Tested middle on input [1,2,3,4.5]")
            self.assertEqual(middle([1,3,5,7,9,10]),[2,3,5,7,9],"Tested middle on input [1,3,5,7,9,10]")
            self.assertEqual(middle([2,9]),[],"Tested middle on input [2,9]")

    myTests().main()
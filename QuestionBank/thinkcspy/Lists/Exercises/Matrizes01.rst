.. activecode:: Matrizes01
    :author: Ana Mafalda Martins
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Lists
    :subchapter: Exercises
    :topics: Lists/Exercises
    :from_source: F
    :language: python

    Ecrevava.  So if N is 4 then your function should add 0 + 1 + 2 + 3
    ~~~~
    def sum_first_n(N):
        # your code here

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(sum_first_n(4),6,feedback="0 + 1 + 2 + 3 == 6")
            self.assertEqual(sum_first_n(0),0,feedback="summing 0 numbers should be 0")

myTests().main()
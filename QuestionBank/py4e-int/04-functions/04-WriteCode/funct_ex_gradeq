.. activecode:: funct_ex_gradeq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-WriteCode
    :topics: 04-functions/04-WriteCode
    :from_source: T
    :practice: T
    :autograde: unittest

    Rewrite the grade program from the previous chapter using a function called ``computegrade``
    that takes a score as its parameter and returns a grade as a string. If someone enters an
    invalid score, return 'Bad score'.

    .. code-block:: python

        Score    Grade
        >= 0.9     A
        >= 0.8     B
        >= 0.7     C
        >= 0.6     D
        < 0.6      F
    ~~~~
    def computegrade(r):
        # your code here

    ====
    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(computegrade(.95),'A',"Tested input: computegrade(.95)")
            self.assertEqual(computegrade('perfect'),'Bad score',"computegrade('perfect')")
            self.assertEqual(computegrade(10.0),'Bad score',"Tested input: computegrade(10.0)")
            self.assertEqual(computegrade(.75),'C',"Tested input: computegrade(.75)")
            self.assertEqual(computegrade(.5),'F',"Tested input: computegrade(.5)")


    myTests().main()
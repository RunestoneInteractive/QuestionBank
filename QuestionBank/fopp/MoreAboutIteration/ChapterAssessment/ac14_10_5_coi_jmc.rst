.. activecode:: ac14_10_5_coi_jmc
    :author: Jonny Comes
    :difficulty: 0.0
    :basecourse: fopp
    :chapter: MoreAboutIteration
    :subchapter: ChapterAssessment
    :topics: MoreAboutIteration/ChapterAssessment
    :from_source: F
    :autograde: unittest
    :practice: T

    Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while loop instead of a for loop. Assign the accumulated total in the while loop code to the variable ``sum2``. Once complete, sum2 should equal sum1.
    ~~~~

    sum1 = 0

    lst = [65, 78, 21, 33]

    for x in lst:
        sum1 = sum1 + x

    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

       def testFive(self):
          self.assertEqual(sum2, 197, "Testing that sum2 is assigned to correct value.")
          self.assertIn('while', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")

    myTests().main()
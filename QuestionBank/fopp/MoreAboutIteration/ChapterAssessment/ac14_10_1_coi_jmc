.. activecode:: ac14_10_1_coi_jmc
    :author: Jonny Comes
    :difficulty: 0.0
    :basecourse: fopp
    :chapter: MoreAboutIteration
    :subchapter: ChapterAssessment
    :topics: MoreAboutIteration/ChapterAssessment
    :from_source: F
    :autograde: unittest
    :practice: T
    :topics: MoreAboutIteration/listenerLoop

    Write a function, ``sublist``, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).
    ~~~~

    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

       def testThree(self):
          self.assertEqual(sublist([1, 2, 3, 4, 5, 6, 7, 8]), [1, 2, 3, 4], "Testing that sublist([1, 2, 3, 4, 5, 6, 7, 8]) returns [1, 2, 3, 4]")
          self.assertEqual(sublist([5]), [], "Testing that sublist([5]) returns []")
          self.assertEqual(sublist([8, 6, 5]), [8, 6], "Testing that sublist([8, 6, 5]) returns [8, 6]")
          self.assertEqual(sublist([1, 6, 2, 3, 9]), [1, 6, 2, 3, 9], "Testing that sublist([1, 6, 2, 3, 9]) returns ([1, 6, 2, 3, 9])")

    myTests().main()
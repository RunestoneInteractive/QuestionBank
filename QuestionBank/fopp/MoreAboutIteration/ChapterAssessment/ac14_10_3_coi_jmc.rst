.. activecode:: ac14_10_3_coi_jmc
    :author: Jonny Comes
    :difficulty: 0.0
    :basecourse: fopp
    :chapter: MoreAboutIteration
    :subchapter: ChapterAssessment
    :topics: MoreAboutIteration/ChapterAssessment
    :from_source: F
    :autograde: unittest
    :practice: T

    Write a function, ``sublist``, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string "STOP" (it should not contain the string "STOP").
    ~~~~

    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

       def testFour(self):
          self.assertEqual(sublist(["bob", "joe", "lucy", "STOP", "carol", "james"]), ["bob", "joe", "lucy"], "Testing that sublist(['bob', 'joe', 'lucy', 'STOP', 'carol', 'james']) returns ['bob', 'joe', 'lucy']")
          self.assertEqual(sublist(["STOP"]), [], "Testing that sublist(['STOP']) returns []")
          self.assertEqual(sublist(["jackie", "paul", "STOP"]), ["jackie", "paul"], "Testing that sublist(['jackie', 'paul', 'STOP']) returns ['jackie', 'paul']")

    myTests().main()
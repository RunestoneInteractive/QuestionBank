.. activecode:: assess_ac2_1_1_10
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Sequences
    :subchapter: week2a1
    :topics: Sequences/week2a1
    :from_source: T
    :autograde: unittest
    :language: python
    :practice: T

    Write code that uses slicing to get rid of the the second 8 so that here are only two 8's in the list bound to the variable `nums`.
    ~~~~
    nums = [4, 2, 8, 23.4, 8, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]


    =====

    from unittest.gui import TestCaseGui
    import re

    class myTests(TestCaseGui):

      def test_output(self):
        self.assertEqual(nums, [4, 2, 8, 23.4, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4], "Testing that nums is set correctly.")
        self.assertTrue(re.search(r'\s*:', self.getEditorText()), "Testing that you are using slices to remove the second 8 (Don't worry about actual and expected values)")

    myTests().main()
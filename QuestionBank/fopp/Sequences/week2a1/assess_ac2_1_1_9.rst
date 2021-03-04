.. activecode:: assess_ac2_1_1_9
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

    Write code to determine how many 9's are in the list ``nums`` and assign that value to the variable ``how_many``. Do not use a for loop to do this.
    ~~~~
    nums = [4, 2, 23.4, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]


    =====

    from unittest.gui import TestCaseGui
    import re

    class myTests(TestCaseGui):

      def test_output(self):
        self.assertEqual(how_many, 3, "Testing that how_many is set correctly.")
        self.assertNotIn('for', self.getEditorText(), "Testing that you didn't use a for loop.")
        self.assertFalse(re.search(r'how_many\s*=\s*3', self.getEditorText()), "Hardcode check")

    myTests().main()
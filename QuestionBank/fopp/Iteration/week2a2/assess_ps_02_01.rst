.. activecode:: assess_ps_02_01
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Iteration
    :subchapter: week2a2
    :topics: Iteration/week2a2
    :from_source: T
    :language: python
    :autograde: unittest
    :practice: T

    Write one for loop to print out each character of the string ``my_str`` on a separate line.
    ~~~~
    my_str = "MICHIGAN"

    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

      def test_output(self):
        self.assertIn('for', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")
        self.assertIn("M\nI\nC\nH\nI\nG\nA\nN", self.getOutput(), "Testing output (Don't worry about actual and expected values).")

    myTests().main()
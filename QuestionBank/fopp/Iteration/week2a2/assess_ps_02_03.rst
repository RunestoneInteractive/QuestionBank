.. activecode:: assess_ps_02_03
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
    :topics: Iteration/Listsandforloops

    Write code that uses iteration to print out **the length** of each element of the list stored in ``str_list``.
    ~~~~
    str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

    # Write your code here.
    =====
    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):
        def test_output(self):
            self.assertIn("for", self.getEditorText(), "Testing whether you used a for loop (Don't worry about actual and expected values).")
            self.assertIn("5\n0\n7\n9\n13", self.getOutput(), "Testing output (Don't worry about actual and expected values).")

    myTests().main()
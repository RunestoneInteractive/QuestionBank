.. activecode:: assess_ps_02_05
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

    Write code to count the number of characters in ``original_str`` using the accumulation pattern and assign the answer to a variable ``num_chars``. Do NOT use the ``len`` function to solve the problem (if you use it while you are working on this problem, comment it out afterward!)
    ~~~~
    original_str = "The quick brown rhino jumped over the extremely lazy fox."


    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
           self.assertEqual(num_chars, len(original_str), "Testing whether num_chars_sent has the correct value")
           self.assertNotIn('len', self.getEditorText(), "Testing that you are not including the len function in your code. (Don't worry about Actual and Expected Values.)")

    myTests().main()
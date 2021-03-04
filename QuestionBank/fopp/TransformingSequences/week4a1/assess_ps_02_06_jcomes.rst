.. activecode:: assess_ps_02_06_jcomes
    :author: Jonny Comes
    :difficulty: 0.0
    :basecourse: fopp
    :chapter: TransformingSequences
    :subchapter: week4a1
    :topics: TransformingSequences/week4a1
    :from_source: F
    :language: python
    :autograde: unittest
    :practice: T

    Write code to create a **list of word lengths** for the words in ``original_str`` using the accumulation pattern and assign the answer to a variable ``num_words_list``. (You should use the ``len`` function).

    ~~~~
    original_str = "The quick brown rhino jumped over the extremely lazy fox"


    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
           self.assertEqual(num_words_list, list(map(len, original_str.split())), "Testing whether num_words_list has the correct value")
           self.assertIn('for', self.getEditorText(), "Testing that you are using a for loop in your code.")

    myTests().main()
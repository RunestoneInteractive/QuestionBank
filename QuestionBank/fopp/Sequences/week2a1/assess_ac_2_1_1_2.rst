.. activecode:: assess_ac_2_1_1_2
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

    Write a program that extracts the last three items in the list ``sports`` and assigns it to the variable ``last``. Make sure to write your code so that it works no matter how many items are in the list.
    ~~~~
    sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']


    =====

    from unittest.gui import TestCaseGui
    import re

    class myTests(TestCaseGui):

      def test_output(self):
         self.assertEqual(last, ['curling', 'ping pong', 'hockey'], "Testing that the value of last is the last three items in sports.")
         self.assertTrue(re.search(r'last\s*=\s*\S*3:', self.getEditorText()), "Hardcode check")


    myTests().main()
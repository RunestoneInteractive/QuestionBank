.. activecode:: assess_ac4_1_1_4
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: TransformingSequences
    :subchapter: week4a1
    :topics: TransformingSequences/week4a1
    :from_source: T
    :language: python
    :practice: T
    :autograde: unittest

    Write code to add 'horseback riding' to the third position (i.e., right before volleyball) in the list ``sports``.
    ~~~~
    sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']


    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

      def test_output(self):
        self.assertEqual(sports, ['cricket', 'football', 'horseback riding', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey'], "Testing that sports is set correctly.")
        self.assertIn('.insert(', self.getEditorText(), "Testing that insert was used in your code.")

    myTests().main()
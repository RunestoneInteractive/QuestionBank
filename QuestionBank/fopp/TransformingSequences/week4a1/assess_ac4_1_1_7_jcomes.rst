.. activecode:: assess_ac4_1_1_7_jcomes
    :author: Jonny Comes
    :difficulty: 0.0
    :basecourse: fopp
    :chapter: TransformingSequences
    :subchapter: week4a1
    :topics: TransformingSequences/week4a1
    :from_source: F
    :autograde: unittest
    :language: python
    :practice: T

    Write code to rearrage the strings in the list ``winners`` so that they are in alphabetical order from A to Z.
    ~~~~
    winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']


    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

      def test_output(self):
        self.assertEqual(winners, ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu'], "Testing that winners is set correctly (Don't worry about actual and expected values).")

    myTests().main()
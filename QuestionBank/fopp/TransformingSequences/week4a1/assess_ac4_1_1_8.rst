.. activecode:: assess_ac4_1_1_8
    :author: Brad Miller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: TransformingSequences
    :subchapter: week4a1
    :topics: TransformingSequences/week4a1
    :from_source: F
    :language: python
    :practice: T

    Write code to switch the order of the ``winners`` list so that it is now Z to A. Assign this list to the variable ``z_winners``.
    ~~~~
    winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']


    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

      def test_output(self):
        self.assertEqual(z_winners, ['Youyou Tu','Rainer Weiss', 'Malala Yousafzai','Kazuo Ishiguro', 'Alvin E. Roth', 'Alice Munro'], "Testing that z_winners is set correctly (Don't worry about actual and expected values).")

    myTests().main()
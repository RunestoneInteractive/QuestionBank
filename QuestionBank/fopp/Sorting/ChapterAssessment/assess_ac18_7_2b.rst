.. activecode:: assess_ac18_7_2b
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Sorting
    :subchapter: ChapterAssessment
    :topics: Sorting/ChapterAssessment
    :from_source: T
    :language: python
    :practice: T

    Write code to switch the order of the ``winners`` list so that it is now Z to A, by first name. Assign this list to the variable ``z_winners``.
    ~~~~
    winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']


    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

      def test_output(self):
        self.assertEqual(z_winners, ['Youyou Tu','Rainer Weiss', 'Malala Yousafzai','Kazuo Ishiguro', 'Alvin E. Roth', 'Alice Munro'], "Testing that z_winners is set correctly.")

    myTests().main()
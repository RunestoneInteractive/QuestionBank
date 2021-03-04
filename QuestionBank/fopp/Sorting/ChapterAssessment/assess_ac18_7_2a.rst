.. activecode:: assess_ac18_7_2a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Sorting
    :subchapter: ChapterAssessment
    :topics: Sorting/ChapterAssessment
    :from_source: T
    :language: python
    :practice: T

    Write code to rearrange the strings in the list ``winners`` so that they are in alphabetical order by first name from A to Z.
    ~~~~
    winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']


    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

      def test_output(self):
        self.assertEqual(winners, ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu'], "Testing that winners is set correctly.")

    myTests().main()
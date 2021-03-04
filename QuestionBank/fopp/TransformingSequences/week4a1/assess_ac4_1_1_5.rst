.. activecode:: assess_ac4_1_1_5
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: TransformingSequences
    :subchapter: week4a1
    :topics: TransformingSequences/week4a1
    :from_source: T
    :language: python
    :autograde: unittest
    :practice: T

    Write code to take 'London' out of the list ``trav_dest``.
    ~~~~
    trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']


    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

      def test_output(self):
        self.assertEqual(trav_dest, ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne'], "Testing that trav_dest is set correctly.")
        self.assertTrue('.remove(' in self.getEditorText() or '.pop(' in self.getEditorText(), "Testing that a method invocation was used in your code.")

    myTests().main()
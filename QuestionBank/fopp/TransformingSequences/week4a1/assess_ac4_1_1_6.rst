.. activecode:: assess_ac4_1_1_6
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

    Write code to add 'Guadalajara' to the end of the list ``trav_dest`` using a list method.
    ~~~~
    trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']


    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

      def test_output(self):
        self.assertEqual(trav_dest, ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne', 'Guadalajara'], "Testing that trav_dest is set correctly.")
        self.assertNotIn('+', self.getEditorText(), "Testing that you are not using concatenation (+).")
        self.assertIn('.', self.getEditorText(), "Testing that a method invocation was used in your code.")

    myTests().main()
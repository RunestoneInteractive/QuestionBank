.. activecode:: asign_c01_01
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

   Below are a set of scores that students have received in the past semester. Write code to determine how many are 90 or above and assign that result to the value ``a_scores``.
   ~~~~
   scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(a_scores, 10, "Testing that you got the right count.")
         self.assertIn('for', self.getEditorText(), "Testing that you used a for loop.")
         self.assertIn('if', self.getEditorText(), "Testing that you used a conditional.")

   myTests().main()
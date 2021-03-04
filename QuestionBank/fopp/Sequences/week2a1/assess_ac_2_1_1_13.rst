.. activecode:: assess_ac_2_1_1_13
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: week2a1
   :topics: Sequences/week2a1
   :from_source: T
   :language: python
   :autograde: unittest
   :practice: T

   Create a variable called ``wrds`` and assign to it a list whose elements are the words in the string ``sent``. Do not worry about punctuation.
   ~~~~
   sent = "The bicentennial for our university was in 2017"

   =====

   from unittest.gui import TestCaseGui
   import re

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(wrds, sent.split(), "Testing that wrds has been correctly assigned.")
         self.assertFalse(re.search(r'wrds\s*=\s*\S*The\S', self.getEditorText()), "Hardcoding Check (Don't worry about actual and expected values)")


   myTests().main()
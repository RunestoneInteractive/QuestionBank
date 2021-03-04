.. activecode:: quiz_6_splitOrJoin_1_coi_jmc
   :author: Jonny Comes
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: week2a1
   :topics: Sequences/week2a1
   :from_source: F
   :language: python
   :autograde: unittest

   Use ``join`` to create a string obtained by combining all the words in the list ``items`` separated by commas.
   Assign your string to a variable named ``things``.
   Be sure to include a space after each comma in your answer so that ``things`` has value
   "tv, computer, car, phone, key".
   Do not modify the value of ``items``.
   ~~~~
   items = ['tv', 'computer', 'car', 'phone', 'key']

   =====

   from unittest.gui import TestCaseGui
   import re

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(things, ', '.join(items), "Testing that things has been correctly assigned.")
         self.assertTrue(re.search('join', self.getEditorText()), "Checking that join was used (Don't worry about actual and expected values)")
         self.assertFalse(re.search(r'things\s*=\s*\S*tv\S', self.getEditorText()), "Hardcoding Check (Don't worry about actual and expected values)")


   myTests().main()
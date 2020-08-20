.. activecode:: quiz_6_splitOrJoin_2_coi_jmc
   :author: Jonny Comes
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: week2a1
   :topics: Sequences/week2a1
   :from_source: F
   :language: python
   :autograde: unittest
   :topics: Sequences/SplitandJoin

   Use ``split`` to create a list whose elements are the words in the string ``items``. Assign your list to a variable named ``foods``. The elements in your list should not have any spaces or ``*``'s. Do not modify the value of ``items``.
   ~~~~
   items = "apple * banana * carrot * pie * taco"

   =====

   from unittest.gui import TestCaseGui
   import re

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(foods, items.split(' * '), "Testing that foods has been correctly assigned.")
         self.assertTrue(re.search('split', self.getEditorText()), "Checking that split was used (Don't worry about actual and expected values)")
         self.assertFalse(re.search(r'foods\s*=\s*\S*apple\S', self.getEditorText()), "Hardcoding Check (Don't worry about actual and expected values)")


   myTests().main()
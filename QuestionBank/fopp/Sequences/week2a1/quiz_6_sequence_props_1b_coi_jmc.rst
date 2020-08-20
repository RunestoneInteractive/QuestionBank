.. activecode:: quiz_6_sequence_props_1b_coi_jmc
   :author: Jonny Comes
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: week2a1
   :topics: Sequences/week2a1
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 1.0

   Assign the number of 5's in the list below to a variable called ``fives``. Avoid hardcoding! In other words, your code should work regardless of the specific value of ``lst``.
   ~~~~
   lst = [5, 2, 4, 7, 2, 5, 23, 5, 22, 5, 2, 4, 5, 2, 5, 23, 5, 37, 5, 2, 4, 7, 2, 5, 23, 5, 29]
   # Do not modify the line above!
   
   =====
   
   from unittest.gui import TestCaseGui
   import re
   
   class myTests(TestCaseGui):
   
      def testOne(self):
         self.assertEqual(fives, lst.count(5), "Checking the value of fives")
         self.assertFalse(re.search('10', self.getEditorText()), "Hardcoding Check (Don't worry about actual and expected values)")
   
   myTests().main()
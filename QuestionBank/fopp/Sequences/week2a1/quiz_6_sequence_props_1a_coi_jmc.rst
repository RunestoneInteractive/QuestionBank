.. activecode:: quiz_6_sequence_props_1a_coi_jmc
   :author: Jonny Comes
   :difficulty: 1.0
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

   Assign the total number of elements in the list below to a variable called ``tot_num``. Avoid hardcoding! In other words, your code should work regardless of the specific value of ``lst``.
   ~~~~
   lst = [5, 2, 4, 7, 2, 5, 23, 5, 22, 5, 2, 4, 5, 2, 5, 23, 5, 37, 5, 2, 4, 7, 2, 5, 23, 5, 29]
   # Do not modify the line above!
   
   =====
   
   from unittest.gui import TestCaseGui
   import re
   
   class myTests(TestCaseGui):
   
      def testOne(self):
         self.assertEqual(tot_num, len(lst), "Checking the value of tot_num")
         self.assertFalse(re.search('27', self.getEditorText()), "Hardcoding Check (Don't worry about actual and expected values)")
   
   myTests().main()
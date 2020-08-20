.. activecode:: quiz_6_sequence_props_2a_coi_jmc
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

   Assign the last element in the list below to a variable called ``last``. Avoid hardcoding! In other words, your code should work regardless of the specific value of ``nums``.
   ~~~~
   nums = [5, 4, 3, 67, 23, 4, 1, 5, 4, 23, 4, 1, 5, 4, 3, 17, 23, 4, 1, 5, 4, 3, 4, 23, 4, 1, 52]
   # Do not modify the line above!
   
   =====
   
   from unittest.gui import TestCaseGui
   import re
   
   class myTests(TestCaseGui):
   
      def testOne(self):
         self.assertEqual(last, nums[-1], "Checking the value of last")
         self.assertFalse(re.search(r'=\s52', self.getEditorText()), "Hardcoding Check (Don't worry about actual and expected values)")
   
   myTests().main()
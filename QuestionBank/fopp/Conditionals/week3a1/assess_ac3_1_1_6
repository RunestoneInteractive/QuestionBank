.. activecode:: assess_ac3_1_1_6
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: week3a1
   :topics: Conditionals/week3a1
   :from_source: T
   :language: python
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.3950795948
   :total_students_attempting: 691
   :num_students_correct: 513.0
   :mean_clicks_to_correct: 3.2436647173

   Create one conditional so that if "Friendly" is in ``w``, then "Friendly is here!" should be assigned to the variable ``wrd``. If it's not, check if "Friend" is in ``w``. If so, the string "Friend is here!" should be assigned to the variable ``wrd``, otherwise "No variation of friend is in here." should be assigned to the variable ``wrd``. (Also consider: does the order of your conditional statements matter for this problem? Why?)
   ~~~~
   w = "Friendship is a wonderful human experience!"
   
   =====
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
      def testOne(self):
         self.assertEqual(wrd, "Friend is here!", "Testing the value of wrd")
         self.assertIn("else", self.getEditorText(), "Checking that you used an else clause.")
         self.assertIn("elif", self.getEditorText(), "Checking that you used an elif clause.")
   
   myTests().main()
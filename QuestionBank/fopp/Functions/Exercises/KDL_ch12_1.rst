.. activecode:: KDL_ch12_1
   :author: Kaelyn Leake
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.25
   :total_students_attempting: 12
   :num_students_correct: 10.0
   :mean_clicks_to_correct: 4.2

   Create a function ``remove_letter`` that accepts a string and a letter. The function should remove the letter from the string and return the new string. For example "cats drinks milks" remove "s" would get "cat drink milk".
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           
           self.assertEqual(remove_letter('dogs and cats',' '), 'dogsandcats', "Testing the remove_letter function on input 'dogs and cats' and ' '.")
           
   myTests().main()
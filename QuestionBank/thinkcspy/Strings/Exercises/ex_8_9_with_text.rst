.. actex:: ex_8_9_with_text
   :author: Karl Sickendick
   :difficulty: 2.0
   :basecourse: thinkcspy
   :chapter: Strings
   :subchapter: Exercises
   :topics: Strings/Exercises
   :from_source: F
   :practice: T
   :autograde: unittest
   :pct_on_first: 0.1666666667
   :total_students_attempting: 18
   :num_students_correct: 7.0
   :mean_clicks_to_correct: 2.0

   Write a function that counts how many non-overlapping occurrences of a substring appear in a string.
   ~~~~
   
   def count(substr,theStr):
       # your code here
   
   
   ====
   
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
         def testOne(self):
             self.assertEqual(count("is","Mississippi"),2,"Tested count on inputs of 'is' and 'Mississippi'")
             self.assertEqual(count("an","banana"),2,"Tested count on inputs of 'an' and 'banana'")
             self.assertEqual(count("ana","banana"),1,"Tested count on inputs of 'ana' and 'banana'")
             self.assertEqual(count("nana","banana"),1,"Tested count on inputs of 'nana' and 'banana'")
             self.assertEqual(count("nanan","banana"),0,"Tested count on inputs of 'nanan' and 'banana'")
             self.assertEqual(count("aaa","aaaaaa"),2,"Tested count on input of 'aaa' and 'aaaaaa'")
   
   
   
   
   myTests().main()
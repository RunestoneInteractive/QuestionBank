.. actex:: ermHW
   :author: Eric Reed
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Labs
   :subchapter: Exercises
   :topics: Labs/Exercises
   :from_source: F
   :autograde: unittest
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 2.0

   Write a program below that outputs "Hi There!"
   ~~~~
   
   hi
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertIn(self.getOutput(),"Hello World\n", "hi" )
   
   myTests().main()
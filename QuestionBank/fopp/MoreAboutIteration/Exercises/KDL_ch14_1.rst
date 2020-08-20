.. activecode:: KDL_ch14_1
   :author: Kaelyn Leake
   :difficulty: 1.2671638937
   :basecourse: fopp
   :chapter: MoreAboutIteration
   :subchapter: Exercises
   :topics: MoreAboutIteration/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.1162790698
   :total_students_attempting: 43
   :num_students_correct: 28.0
   :mean_clicks_to_correct: 5.5357142857

   The answer to the question, "How far can a stack of ``n`` identical books overhand the edge of a table without falling off?" is given by: d=0.5*sum(1/n) as you sum from 1 to n. Where ``d`` is the distance from the edge of the table to the outside edge of the top book.  Use a while loop to figure out the number of books(n) that are needed to have a book length over hang (aka d>1).  
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
            self.assertIn('while', self.getEditorText(), 'Contains while')
            self.assertEqual(n, 4, "Testing to see if book number is correct.")
   
           
   myTests().main()
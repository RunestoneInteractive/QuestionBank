.. activecode:: rab_lab_ex_06_03
   :author: Richard Bernatz
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :nocodelens: 
   :pct_on_first: 0.6851851852
   :total_students_attempting: 54
   :num_students_correct: 54.0
   :mean_clicks_to_correct: 1.7962962963

    Use this active code window for lab activity 3 in Chapter 6. Refer to the course web page for instructions.
   ~~~~
   # your name
   def roll_average(roll_list):
    
    
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(roll_average([4,3,5,2,6,4]), 4.0, "Tested [4,3,5,2,6,4] with average = 4.0")
           self.assertEqual(roll_average([6,4,5,4,2]), 4.2, "Tested [6,4,5,4,2] with average = 4.2")
           self.assertEqual(roll_average([1,2,3,3,2,1,2,1,3]), 2.0, "Tested [1,2,3,3,2,1,2,1,3] with average = 2.0")
           self.assertEqual(roll_average([1,2,3,4,5,6]), 3.5, "Tested [1,2,3,4,5,6] with average = 3.5")
           
          
   myTests().main()
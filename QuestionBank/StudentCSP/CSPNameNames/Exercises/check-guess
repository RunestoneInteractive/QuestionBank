.. activecode:: check-guess
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPNameNames
   :subchapter: Exercises
   :topics: CSPNameNames/Exercises
   :from_source: F
   :autograde: unittest
   :nocodelens: 
   :pct_on_first: 0.6933333333
   :total_students_attempting: 150
   :num_students_correct: 148.0
   :mean_clicks_to_correct: 1.6824324324

   Finish the function below to return 'too low' if the guess is less than the passed 
   target, 'correct' if they are equal, and 'too high' if the guess is greater than the 
   passed target.  For example, check_guess(5,7) returns 'too low', 
   check_guess(7,7) returns 'correct', and check_guess(9,7) returns 'too high'. 
   ~~~~
   def check_guess(guess, target):
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertEqual(check_guess(5, 7), 'too low', "check_guess(5, 7)")
           self.assertEqual(check_guess(7, 7), 'correct', "check_guess(7, 7)")
           self.assertEqual(check_guess(9, 7), 'too high', "check_guess(9, 7)")
           self.assertEqual(check_guess(3, 9), 'too low', "check_guess(3, 9)")
           self.assertEqual(check_guess(3, 3), 'correct', "check_guess(3, 3)")
           self.assertEqual(check_guess(20, 9), 'too high', "check_guess(20, 9)")
           self.assertEqual(check_guess(-5, 7), 'too low', "check_guess(-5, 7)")
         
              
   myTests().main()
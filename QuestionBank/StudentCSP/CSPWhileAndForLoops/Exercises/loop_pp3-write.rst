.. activecode:: loop_pp3-write
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPWhileAndForLoops
   :subchapter: Exercises
   :topics: CSPWhileAndForLoops/Exercises
   :from_source: F
   :autograde: unittest
   :nocodelens: 

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
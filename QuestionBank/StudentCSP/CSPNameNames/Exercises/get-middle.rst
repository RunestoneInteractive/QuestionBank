.. activecode:: get-middle
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPNameNames
   :subchapter: Exercises
   :topics: CSPNameNames/Exercises
   :from_source: F
   :autograde: unittest
   :nocodelens: 
   :pct_on_first: 0.0446428571
   :total_students_attempting: 112
   :num_students_correct: 89.0
   :mean_clicks_to_correct: 9.0561797753

   Finish the function below to return the middle characters from the passed string.
   If the string has less than 3 characters then return the passed string.  
   If the string has an odd length then return the middle character.  If the string has an even 
   length return the two middle characters.  For example, get_middle('abc') returns 
   'b' and get_middle('abcd') returns 'bc'.  
   ~~~~
   def get_middle(str):
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertEqual(get_middle('abc'), 'b', "get_middle('abc')")
           self.assertEqual(get_middle('abcd'), 'bc', "get_middle('abcd')")
           self.assertEqual(get_middle('12345'), '3', "get_middle('12345')")
           self.assertEqual(get_middle('123456'), '34', "get_middle('123456')")
           self.assertEqual(get_middle('ab'), 'ab', "get_middle('ab')")
           self.assertEqual(get_middle('a'), 'a', "get_middle('a')")
           self.assertEqual(get_middle(''), '', "get_middle('')")
          
   
              
   myTests().main()
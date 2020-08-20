.. activecode:: temp-to-string
       :author: Barbara  Ericson
       :difficulty: 0.0
       :basecourse: StudentCSP
       :chapter: CSPNameNames
       :subchapter: Exercises
       :topics: CSPNameNames/Exercises
       :from_source: F
       :nocodelens: 
       :autograde: unittest
       :pct_on_first: 0.3863636364
       :total_students_attempting: 44
       :num_students_correct: 42.0
       :mean_clicks_to_correct: 2.5952380952

       Given an integer that represents a temperature return "too cold" if the temp is
       below 30, "a bit cold" if the temperature is between 30 and 64, "good" if it is 
       between 65 and 80 (inclusive), and "too hot" if it is warmer than 80.  
       ~~~~
       def check_temp(temp):
       
       ====
       from unittest.gui import TestCaseGui
       
       class myTests(TestCaseGui):
       
           def testOne(self):
               self.assertEqual(check_temp(20), "too cold", 'check_temp(20)')
               self.assertEqual(check_temp(29), "too cold", 'check_temp(29)')
               self.assertEqual(check_temp(30), "a bit cold", 'check_temp(30)')
               self.assertEqual(check_temp(31),  "a bit cold", 'check_temp(31)')
               self.assertEqual(check_temp(64),  "a bit cold", 'check_temp(64)')
               self.assertEqual(check_temp(65),  "good", 'check_temp(65)')
               self.assertEqual(check_temp(70),  "good", 'check_temp(70)')
               self.assertEqual(check_temp(80),  "good", 'check_temp(80)')
               self.assertEqual(check_temp(81), "too hot", 'check_temp(81)')
               self.assertEqual(check_temp(95), "too hot", 'check_temp(95)')
       
       myTests().main()
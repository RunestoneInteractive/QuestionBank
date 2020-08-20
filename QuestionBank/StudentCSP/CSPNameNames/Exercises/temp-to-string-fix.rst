.. activecode:: temp-to-string-fix
       :author: Barbara  Ericson
       :difficulty: 0.0
       :basecourse: StudentCSP
       :chapter: CSPNameNames
       :subchapter: Exercises
       :topics: CSPNameNames/Exercises
       :from_source: F
       :autograde: unittest
       :pct_on_first: 0.8795180723
       :total_students_attempting: 83
       :num_students_correct: 83.0
       :mean_clicks_to_correct: 1.2289156627

       Fix the code below so that given an integer that represents a temperature it will return "too cold" if the temp is
       below 30, "a bit cold" if the temperature is between 30 and 64, "good" if it is 
       between 65 and 80 (inclusive), and "too hot" if it is warmer than 80.  
       ~~~~
       def check_temp(temp):
           if temp < 30:
               return too cold
           else if temp >= 30 && temp <= 64
                return "a bit cold"
           else if temp >= 65 and <= 80:
                ret "good"
           else:
                return "too hot"
       
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
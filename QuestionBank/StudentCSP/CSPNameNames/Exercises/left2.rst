.. activecode:: left2
       :author: Barbara  Ericson
       :difficulty: 1.0
       :basecourse: StudentCSP
       :chapter: CSPNameNames
       :subchapter: Exercises
       :topics: CSPNameNames/Exercises
       :from_source: F
       :nocodelens: 
       :autograde: unittest
       :pct_on_first: 0.6176470588
       :total_students_attempting: 34
       :num_students_correct: 34.0
       :mean_clicks_to_correct: 2.7647058824

       Given a string, str, return a "rotated left 2" version where the first
       two letters are moved to the end.  The string length will be at least 2.
       For example, left2("Hello") will return "lloHe"
       ~~~~
       def left2(str):
       
       ====
       from unittest.gui import TestCaseGui
       
       class myTests(TestCaseGui):
       
           def testOne(self):
               self.assertEqual(left2("Hello"), "lloHe", 'left2("Hello")')
               self.assertEqual(left2("Python"), "thonPy", 'left2("Python")')
               self.assertEqual(left2("Hi"), "Hi", 'left2("Hi")')
               self.assertEqual(left2("code"), "deco", 'left2("code")')
               self.assertEqual(left2("Chocolate"), "ocolateCh", 'left2("Chocolate")')
               self.assertEqual(left2("bricks"), "icksbr", 'left2("bricks")')
       
       myTests().main()
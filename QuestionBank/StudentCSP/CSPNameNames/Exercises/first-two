.. activecode:: first-two
       :author: Barbara  Ericson
       :difficulty: 0.0
       :basecourse: StudentCSP
       :chapter: CSPNameNames
       :subchapter: Exercises
       :topics: CSPNameNames/Exercises
       :from_source: F
       :nocodelens: 
       :autograde: unittest
       :pct_on_first: 0.5166666667
       :total_students_attempting: 60
       :num_students_correct: 55.0
       :mean_clicks_to_correct: 2.2181818182

       Given a string, return the string made of its first two chars, so the String 
       "Hello" yields "He". If the string is shorter than length 2, return whatever 
       there is, so first_two("Hello") returns "He" and first_two("X") returns "X".    
       ~~~~
       def first_two(str):
       
       ====
       from unittest.gui import TestCaseGui
       
       class myTests(TestCaseGui):
       
           def testOne(self):
       
               self.assertEqual(first_two('Hello'), 'He', "first_two('Hello')")
               self.assertEqual(first_two('abcdefg'), 'ab', "first_two('abcdefg')")
               self.assertEqual(first_two('X'), 'X', "first_two('X')")
               self.assertEqual(first_two('ab'), 'ab', "first_two('ab')")
               self.assertEqual(first_two('a'), 'a', "first_two('a')")
               self.assertEqual(first_two(""), "", 'first_two("")')
       
       myTests().main()
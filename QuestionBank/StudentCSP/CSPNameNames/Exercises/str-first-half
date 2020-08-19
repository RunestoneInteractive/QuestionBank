.. activecode:: str-first-half
       :author: Barbara  Ericson
       :difficulty: 0.0
       :basecourse: StudentCSP
       :chapter: CSPNameNames
       :subchapter: Exercises
       :topics: CSPNameNames/Exercises
       :from_source: F
       :nocodelens: 
       :autograde: unittest
       :pct_on_first: 0.0
       :total_students_attempting: 1
       :num_students_correct: 1.0
       :mean_clicks_to_correct: 3.0

       Given a string (str), finish the function below to return the first half
       of the string.  For example, if given the string "WooHoo" it should
       return "Woo"
       ~~~~
       def first_half(str):
       
       ====
       from unittest.gui import TestCaseGui
       
       class myTests(TestCaseGui):
       
           def testOne(self):
               self.assertEqual(first_half("WooHoo"), "Woo", 'first_half("WooHoo")')
               self.assertEqual(first_half("HelloThere"), "Hello", 'first_half("HelloThere")')
               self.assertEqual(first_half('abcdef'), 'abc', "first_half('abcdef')")
               self.assertEqual(first_half('ab'), 'a', "first_half('ab')")
               self.assertEqual(first_half(''), '', "first_half('')")
               self.assertEqual(first_half('0123456789'), '01234', "first_half('0123456789')")
               self.assertEqual(first_half('kitten'), 'kit', "first_half('kitten')")
       
       myTests().main()
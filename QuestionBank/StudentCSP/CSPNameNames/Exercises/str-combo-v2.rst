.. activecode:: str-combo-v2
       :author: Barbara  Ericson
       :difficulty: 1.0
       :basecourse: StudentCSP
       :chapter: CSPNameNames
       :subchapter: Exercises
       :topics: CSPNameNames/Exercises
       :from_source: F
       :nocodelens: 
       :autograde: unittest
       :pct_on_first: 0.696969697
       :total_students_attempting: 33
       :num_students_correct: 33.0
       :mean_clicks_to_correct: 1.7878787879

       Given two strings, a and b, return a string of the form short + long +
       short, with the shorter string on the outside and the longer string on
       the inside.  The strings will not be the same length, but they may
       be empty.  For example, combo_string("Hello", "hi") will return "hiHellohi".
       ~~~~
       def combo_string(a, b):
       
       ====
       from unittest.gui import TestCaseGui
       
       class myTests(TestCaseGui):
       
           def testOne(self):
               self.assertEqual(combo_string("Hello", "hi"), "hiHellohi", 'combo_string("Hello", "hi")')
               self.assertEqual(combo_string("hi", "Hello"), "hiHellohi", 'combo_string("hi", "Hello")')
               self.assertEqual(combo_string("aaa", "b"), "baaab", 'combo_string("aaa", "b")')
               self.assertEqual(combo_string("aaa",""), 'aaa', 'combo_string("aaa","")')
               self.assertEqual(combo_string('', 'bb'), 'bb', "combo_string('', 'bb')")
               self.assertEqual(combo_string("aaa","1234"), "aaa1234aaa", 'combo_string("aaa","1234")')
               self.assertEqual(combo_string("a","bb"), "abba", 'combo_string("a","bb")')
               self.assertEqual(combo_string("bb","a"), "abba", 'combo_string("bb","a")')
       
       myTests().main()
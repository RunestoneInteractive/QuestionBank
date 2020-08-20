.. activecode:: con-two-no-first-letter
              :author: Barbara  Ericson
              :difficulty: 0.0
              :basecourse: StudentCSP
              :chapter: CSPNameNames
              :subchapter: Exercises
              :topics: CSPNameNames/Exercises
              :from_source: F
              :nocodelens: 
              :autograde: unittest
              :pct_on_first: 1.0
              :total_students_attempting: 1
              :num_students_correct: 1.0
              :mean_clicks_to_correct: 1.0

              Given two strings, a and b, return them appended together, but
              withtout the first letter in each string.  The strings will be
              of length one or greater.  For example, appRest("Hello", "There") will 
              return "ellohere".
              ~~~~
              def app_rest(a, b):
              
              ====
              from unittest.gui import TestCaseGui
              
              class myTests(TestCaseGui):
              
                  def testOne(self):
                      self.assertEqual(app_rest("Hello", "There"), "ellohere", 'app_rest("Hello", "There")')
                      self.assertEqual(app_rest("Python", "code"), "ythonode", 'app_rest("Python", "code")')
                      self.assertEqual(app_rest("ab", "xy"), "by", 'app_rest("ab", "xy")')
                      self.assertEqual(app_rest("ab", "x"), "b", 'app_rest("ab", "x")')
                      self.assertEqual(app_rest("a", "xy"), "y", 'app_rest("a", "xy")')
                      self.assertEqual(app_rest("a", "x"), "", 'app_rest("a", "x")')
              
              myTests().main()
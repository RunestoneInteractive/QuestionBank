.. activecode:: exp1_q4_total_values
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPNameNames
   :subchapter: Exercises
   :topics: CSPNameNames/Exercises
   :from_source: F
   :autograde: unittest
   :nocodelens: 
   :pct_on_first: 0.6111111111
   :total_students_attempting: 90
   :num_students_correct: 84.0
   :mean_clicks_to_correct: 1.8333333333

   Finish the function total_values that takes a dictionary (dict) and returns the total of the values in the dictionary. For example, total_dict_values({'red': 3, 'blue': 2, 'green’: 20}) would return 25.
   
   ~~~~
   def total_values(dict):
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertEqual(total_values({'red':2, 'blue':3, 'green':20}),25, "total_values({'red':2, 'blue':3, 'green':20})")
           self.assertEqual(total_values({'a': 3}), 3, "total_values({'a': 3})")
           self.assertEqual(total_values({'a': 3, 'b': -5}), -2, "total_values({'a': 3, 'b': -5})")
           self.assertEqual(total_values({'a': 3, 'b': -3}), 0, "total_values({'a': 3, 'b': -3})")
           self.assertEqual(total_values({}), 0, "total_values({})")
   
   myTests().main()
.. activecode:: exp1_q5_write
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPNameTurtles
   :subchapter: Exercises
   :topics: CSPNameTurtles/Exercises
   :from_source: F
   :autograde: unittest
   :nocodelens: 
   :pct_on_first: 0.3943661972
   :total_students_attempting: 71
   :num_students_correct: 61.0
   :mean_clicks_to_correct: 3.6393442623

   Finish the function get_names that takes a list of dictionaries and returns a list of strings with the names from the dictionaries.  The key for the first name is 'first' and the key for the last name is 'last'.  Return a list of the full names (first last) as a string.  If the 'first' or 'last' key is missing in the dictionary use 'Unknown'.
   
   ~~~~
   def get_names(d_list):
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
       def testOne(self):
           d1 = {'first': 'Tsi', 'last': 'Choi'}
           d2 = {'first': 'Joy', 'last': 'Ali'}
           d3 = {'first': 'Jose', 'last': 'Capo'}
           d4 = {'first': 'Malik'}
           d5 = {'last': 'Owens'}
           d_l1 = [d1, d2]
           d_l2 = [d3]
           d_l3 = [d4]
           d_l4 = [d5]
           self.assertEqual(get_names(d_l1), ['Tsi Choi', 'Joy Ali'], "get_names([{'first': 'Tsi', 'last': 'Choi'}, {'first': 'Joy', 'last': 'Ali'}])")
           self.assertEqual(get_names(d_l2), ['Jose Capo'], "get_names([{'first': 'Jose', 'last': 'Capo'}])")
           self.assertEqual(get_names(d_l3), ['Malik Unknown'], "get_names([{'first': 'Malik'}])")
           self.assertEqual(get_names(d_l4), ['Unknown Owens'], "get_names([{'last': 'Owens'}])")
           
            
   myTests().main()
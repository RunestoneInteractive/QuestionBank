.. activecode:: get_index_duplicate-fix
       :author: Barbara  Ericson
       :difficulty: 0.0
       :basecourse: StudentCSP
       :chapter: CSPWhileAndForLoops
       :subchapter: Exercises
       :topics: CSPWhileAndForLoops/Exercises
       :from_source: F
       :autograde: unittest
       :pct_on_first: 0.0
       :total_students_attempting: 1
       :num_students_correct: 1.0
       :mean_clicks_to_correct: 2.0

       Fix the code below to return the index of the first adjacent duplicate value in a 
       list or -1 if no duplicates were found.  For example, get_index_dup([1, 2, 2, 3]) 
       returns 2 and get_index_dup([1, 2, 3]) returns -1.  
       ~~~~
       def get_index_dup(a_list):
           prev = a_list[0]
           for index in range(1, len(a_list)):
               if index = prev:
                   return index
           return -1
               
       
       ====
       from unittest.gui import TestCaseGui
       
       class myTests(TestCaseGui):
       
           def testOne(self):
               self.assertEqual(get_index_dup([1, 2, 2, 3]), 2, 'get_index_dup([1, 2, 2, 3])')
               self.assertEqual(get_index_dup([1, 2, 3]), -1, 'get_index_dup([1, 2, 3])')
               self.assertEqual(get_index_dup([1, 1, 3]), 1, 'get_index_dup([1, 1, 3])')
               self.assertEqual(get_index_dup([1, 2, 2]), 2, 'get_index_dup([1, 2, 2])') 
               self.assertEqual(get_index_dup([2, 2, 2]), 1, 'get_index_dup([2, 2, 2])')
       
            
       
       myTests().main()
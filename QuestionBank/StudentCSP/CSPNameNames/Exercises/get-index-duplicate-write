.. activecode:: get-index-duplicate-write
       :author: Barbara  Ericson
       :difficulty: 0.0
       :basecourse: StudentCSP
       :chapter: CSPNameNames
       :subchapter: Exercises
       :topics: CSPNameNames/Exercises
       :from_source: F
       :autograde: unittest
       :pct_on_first: 1.0
       :total_students_attempting: 1
       :num_students_correct: 1.0
       :mean_clicks_to_correct: 1.0

       Fix the code below to return the index of the first adjacent duplicate value in the list or -1 if there are no duplicates.  
       For example, get_index_duplicate([1, 1, 2] return 1 and get_index_duplicate([0,1,2]) returns -1.
       ~~~~
       def get_index_duplicate(num_list):
           prev = num_list[1]
           for index in range(1,len(num_list):
               curr = num_list[index]
                   if curr == prev:
                       return index
               return -1
              
       
       ====
       from unittest.gui import TestCaseGui
       
       class myTests(TestCaseGui):
       
           def testOne(self):
               self.assertEqual(get_index_duplicate([1,1,2]), 1, 'get_index_duplicate([1,1,2])')
               self.assertEqual(get_index_duplicate([0,1,1]), 2, 'get_index_duplicate([0,1,1])')
               self.assertEqual(get_index_duplicate([0,1,2]), -1, 'get_index_duplicate([0,1,2])')
               self.assertEqual(get_index_duplicate([1, 0, 1]), -1, 'get_index_duplicate([1, 0, 1])')
               self.assertEqual(get_index_duplicate([1, 1, 1]), 1, 'get_index_duplicate([1, 1, 1])')
               self.assertEqual(get_index_duplicate([1, 2, 3, 4, 4]), 4, 'get_index_duplicate([1, 2, 3, 4, 4])')
       
       
       myTests().main()
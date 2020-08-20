.. actex:: hollins_table_intro_2_ac
   :author: Stephen Wassell
   :difficulty: 1.0
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 81
   :num_students_correct: 81.0
   :mean_clicks_to_correct: 1.0

   
   We can print each number of the table on a separate line using 
   nested for loops. 
   The outer for loop iterator variable ``i`` indexes the 3 rows,
   and the inner for loop iterator variable ``j`` indexes the 4 columns. 
   Run the code and study the output to make sure you see how the
   nested for loops work.
        
   ~~~~
   table = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]
   
   for i in range(3):
       for j in range(4):
           print("i:", i, " j:", j, " num:", table[i][j])
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):  
           self.assertTrue(True)
   myTests().main()
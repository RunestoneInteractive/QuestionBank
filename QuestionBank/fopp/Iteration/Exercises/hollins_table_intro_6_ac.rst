.. actex:: hollins_table_intro_6_ac
   :author: Stephen Wassell
   :difficulty: 1.0990059529
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.3289473684
   :total_students_attempting: 76
   :num_students_correct: 47.0
   :mean_clicks_to_correct: 2.6808510638

   
   Now it is your turn! Using nested for loops,
   multiply each number in the table by 5 (try not to
   copy and paste from previous code segments!).
   If you want to print the table, feel free, but that's not required.
        
   ~~~~
   table = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]
   
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           target = [ [5, 10, 15, 20],
                     [25, 30, 35, 40],
              [45, 50, 55, 60] ]
    for i in range(len(target)):
        for j in range(len(target[i])):
            self.assertEqual(table[i][j], target[i][j])
   myTests().main()
.. actex:: hollins_table_intro_7_ac
   :author: Stephen Wassell
   :difficulty: 1.0818885297
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.2784810127
   :total_students_attempting: 79
   :num_students_correct: 41.0
   :mean_clicks_to_correct: 2.3902439024

   
   In this code segment, there are two tables, ``table1`` and ``table2``,
   each with 3 rows and 4 columns. Using nested for loops, create a new 
   table called ``table3`` (having 3 rows and 4 columns), so that each number 
   in ``table3`` is the sum of the corresponding numbers in ``table1`` and 
   ``table2``. Hint: before the nested for loops, define ``table3`` to be a table
   having all zeros, and then overwrite the zeros one by one in the innermost loop.
        
   ~~~~
   table1 = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12]]
   
   table2 = [[10, 20, 30, 40],
             [50, 60, 70, 80],
             [90, 100, 110, 120]]
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           target = [ [11, 22, 33, 44],
                     [55, 66, 77, 88],
              [99, 110, 121, 132] ]
    for i in range(len(target)):
        for j in range(len(target[i])):
            self.assertEqual(table3[i][j], target[i][j])
   myTests().main()
.. actex:: hollins_table_intro_4_ac
   :author: Stephen Wassell
   :difficulty: 1.0
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.975
   :total_students_attempting: 80
   :num_students_correct: 80.0
   :mean_clicks_to_correct: 1.0375

   
   It's a good idea not to hardcode the number of rows and columns.
   Don't forget the table is a list of lists, so the number of rows is the
   length of the outer list, and the number of columns is the length of any
   one of the inner lists (so we might as well use the first one).
   Also, this time we use the accumulator pattern to sum up all of the
   numbers in the table.
   Check out the new code and run it.
        
   ~~~~
   table = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]
   
   total = 0
   for row in range(len(table)):
       for col in range(len(table[0])):
           total += table[row][col]
   
   print(total)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):  
           self.assertEqual(int(self.getOutput()), 78)
   myTests().main()
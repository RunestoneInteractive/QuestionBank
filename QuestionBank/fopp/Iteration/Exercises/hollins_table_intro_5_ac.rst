.. actex:: hollins_table_intro_5_ac
   :author: Stephen Wassell
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.975308642
   :total_students_attempting: 81
   :num_students_correct: 81.0
   :mean_clicks_to_correct: 1.0617283951

   
   Next let's mutate the table! We'll simply add 10 to each number
   in the table and then print the table (just using the list of lists format)
   to see the result.
   Check out the new code and run it.
        
   ~~~~
   table = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]
   
   for row in range(len(table)):
       for col in range(len(table[0])):
           table[row][col] += 10
   
   print(table)
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           target = [ [11, 12, 13, 14],
                     [15, 16, 17, 18],
              [19, 20, 21, 22] ]
    for i in range(len(target)):
        for j in range(len(target[i])):
            self.assertEqual(table[i][j], target[i][j])
   myTests().main()
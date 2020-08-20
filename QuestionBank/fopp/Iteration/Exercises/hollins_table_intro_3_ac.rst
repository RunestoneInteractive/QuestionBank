.. actex:: hollins_table_intro_3_ac
   :author: Stephen Wassell
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 82
   :num_students_correct: 82.0
   :mean_clicks_to_correct: 1.0

   
   While ``i`` and ``j`` are standard iterator variables in this situation,
   ``row`` and ``col`` might be more descriptive. Also we can print the
   values of the table in a more readable format by using the named
   parameter  ``end`` of the ``print()`` function to change what is printed
   at the end of the line, which by default is the newline character ``\n``,
   to simply a space.  We then need a print statement within only the
   outer for loop in order to get each row to be on a new line.
   Check out the new code and run it.
        
   ~~~~
   table = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]
   
   for row in range(3):
       for col in range(4):
           print(table[row][col], end=" ")
       print()
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):  
           self.assertTrue(True)
   myTests().main()
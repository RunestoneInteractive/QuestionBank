.. actex:: rab_hw_ex_01_ch_13
   :author: Richard Bernatz
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Dictionaries
   :subchapter: Exercises
   :topics: Dictionaries/Exercises
   :from_source: F
   :nocodelens: 
   :pct_on_first: 0.1111111111
   :total_students_attempting: 36
   :num_students_correct: 28.0
   :mean_clicks_to_correct: 26.9642857143

   Write a function called ```sparse_fill(d, r, c)``` that fills a sparse matrix, of size ```r``` rows by ```c``` columns, using the dictionary d for the non-zero terms. The keys in ```d``` are tuples ```(row_number, column_number)``` that specify the row and column numbers for the non-zero entry given by their corresponding values. All other entries in the matrix are zeros. The function constructs and returns the matrix. The function also returns an error code having one of four values: 0 = no errors, 1 = row range error, 2 = column range error, and 3 = column and range error. These two items are returned as a tuple, the matrix as the first item and the error code as the second item.
   
   
   ~~~~
   def sparse_fill(d, r, c):
       # your code here
       
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           d = {(0, 1): 3, (2, 2): -2}
           (m, ec) = sparse_fill(d, 3, 3)
           (mt, ect) = ([[0, 3, 0], [0, 0, 0], [0, 0, -2]], 0)
           self.assertEqual((m, ec), (mt, ect), "Tested {(0, 1): 3, (2,2): -2}, 3, 3")
           d = {(0, 1): 3, (2, 2): -2}
           (m, ec) = sparse_fill(d, 2, 3)
           (mt, ect) = ([[0, 3, 0], [0, 0, 0]], 1)
           self.assertEqual((m, ec), (mt, ect), "Tested {(0, 1): 3, (2,2): -2}, 2, 3")
           (m, ec) = sparse_fill(d, 3, 2)
           (mt, ect) = ([[0, 3], [0, 0], [0, 0]], 2)
           self.assertEqual((m, ec), (mt, ect), "Tested {(0, 1): 3, (2,2): -2}, 3, 2")
           d = {(0, 1): 3, (2, 2): -2}
           (m, ec) = sparse_fill(d, 2, 2)
           (mt, ect) = ([[0, 3], [0, 0]], 3)
           self.assertEqual((m, ec), (mt, ect), "Tested {(0, 1): 3, (2,2): -2}, 2, 2")
         
   myTests().main()
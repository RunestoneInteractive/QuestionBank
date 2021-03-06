.. actex:: rab_hw_ex_01_ch_10
   :author: Richard Bernatz
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Lists
   :subchapter: Exercises
   :topics: Lists/Exercises
   :from_source: F
   :nocodelens: 
   :pct_on_first: 0.1067961165
   :total_students_attempting: 103
   :num_students_correct: 90.0
   :mean_clicks_to_correct: 18.3555555556

   Write a function called ``find_max_index`` that takes a list of floating point numbers and determines the index, or indicies, of the maximum value in the list. Write just the function, and have it return an integer list of a single index, or a list of indices in the event the maximum occurs more than once in the input list. The return list must be ordered least to greatest.
   
   
   ~~~~
   def find_max_index(l_in):
       # your code here
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           l_in = [3.1, 4.7, 10.1, 0.5, 9.9, 6.3, 7.7, 2.1]
           l_out = find_max_index(l_in)
           self.assertTrue(l_out == [2], "Tested [3.1, 4.7, 10.1, 0.5, 9.9, 6.3, 7.7, 2.1] ")
           l_in = [12.1, 4.7, 10.1, 0.5, 9.9, 12.1, 7.7, 2.1]
           l_out = find_max_index(l_in)
           self.assertTrue(l_out == [0, 5], "Tested  [12.1, 4.7, 10.1, 0.5, 9.9, 12.1, 7.7, 2.1]")
           l_in = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]
           l_out = find_max_index(l_in)
           self.assertTrue(l_out == [0, 1, 2, 3, 4, 5, 6, 7], "Tested  [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]" )           
   
   myTests().main()
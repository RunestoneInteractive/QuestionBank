.. actex:: CS152_list_odd_times
    :author: John Cigas
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Lists
    :subchapter: Exercises
    :topics: Lists/Exercises
    :from_source: F
    :practice: T
    :autograde: unittest
    :nocodelens: 
    :pct_on_first: 0.3870967742
    :total_students_attempting: 31
    :num_students_correct: 26.0
    :mean_clicks_to_correct: 5.6538461538

    Write a fruitful function called ``list_odd_times_n(aList,n)`` that takes a list of numbers as an argument
    and a multiplier, and returns a list with only the odd numbers multiplied by n. Use a for loop and the accumulator pattern.
    ~~~~
    
    def list_odd_times_n(aList, n):
        # your code here
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
         def testOne(self):
    
             l1 = [2,3, 4, 5]
             self.assertEqual(list_odd_times_n(l1,7),[21, 35],str(l1)+', 7')
             l2 = [9]
             self.assertEqual(list_odd_times_n(l2,5),[45],str(l2)+', 5')
             l3 = [2, 4]
             self.assertEqual(list_odd_times_n(l3,21),[],str(l3)+', 3')
             self.assertEqual(list_odd_times_n(l1,2),[6,10],str(l1)+', 2')
             # Should check for contains empty list [] symbol
    
    
    myTests().main()
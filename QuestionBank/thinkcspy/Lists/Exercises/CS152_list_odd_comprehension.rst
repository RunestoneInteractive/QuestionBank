.. actex:: CS152_list_odd_comprehension
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
    :pct_on_first: 0.2857142857
    :total_students_attempting: 7
    :num_students_correct: 7.0
    :mean_clicks_to_correct: 2.8571428571

    Write a fruitful function called ``list_odd(aList)`` that takes a list of numbers as an argument
    and returns a list with only the odd numbers. Use a one line list comprehension.
    ~~~~
    
    def list_odd(aList):
        # your code here
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
         def testOne(self):
    
             l1 = [2,3, 4, 5]
             self.assertEqual(list_odd(l1),[3, 5],str(l1))
             l2 = [9]
             self.assertEqual(list_odd(l2),[9],str(l2))
             l3 = [2, 4]
             self.assertEqual(list_odd(l3),[],str(l3))
             # Should check for comprehension = how????
    
    
    myTests().main()
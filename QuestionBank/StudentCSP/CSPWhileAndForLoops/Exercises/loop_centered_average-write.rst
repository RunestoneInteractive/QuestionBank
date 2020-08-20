.. activecode:: loop_centered_average-write
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPWhileAndForLoops
   :subchapter: Exercises
   :topics: CSPWhileAndForLoops/Exercises
   :from_source: F
   :autograde: unittest
   :nocodelens: 
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 2.0

   Finish writing a function that will calculate and return a "centered average".  
   Calculate the total of the items in the list, the lowest value, and the 
   highest value.  
   Set the revised total to the total minus the lowest and highest values.  
   Set the number of items in the 
   revised total to the number of items in the list minus two.  
   Return the revised total divided by the number of items in the revised total.
   For example, get_centered_avg([1, 2, 3, 4, 100]) returns 3.  
   ~~~~
   def get_centered_avg(nums):
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertEqual(get_centered_avg([1, 2, 3, 4, 100]), 3, "get_centered_avg([1, 2, 3, 4, 100])")
           self.assertEqual(get_centered_avg([1, 1, 5, 5, 10, 8, 7]), 5.2, "get_centered_avg([1, 1, 5, 5, 10, 8, 7]),")
           self.assertEqual(get_centered_avg([-10, -4, -2, -4, -2, 0]), -3, "get_centered_avg([-10, -4, -2, -4, -2, 0])")
           self.assertEqual(get_centered_avg([1, 1, 100]), 1, "get_centered_avg([1, 1, 100])")
           self.assertEqual(get_centered_avg([7, 7, 7]), 7, "get_centered_avg([7,7,7])")
           self.assertEqual(get_centered_avg([7, 7, 7, 7]), 7, "get_centered_avg([7,7,7,7])")
           self.assertEqual(get_centered_avg([8, 1, 7]), 7, "get_centered_avg([8,1,7])")
          
          
   myTests().main()
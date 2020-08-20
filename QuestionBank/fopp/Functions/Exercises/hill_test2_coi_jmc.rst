.. activecode:: hill_test2_coi_jmc
   :author: Jonny Comes
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.5
   :total_students_attempting: 2
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   
   Write a function ``square_list`` which takes in a list of numbers, and returns a list of the squares of those numbers.  Example: ``square_list([1,5,3])`` should return ``[1,25,9]``.
   ~~~~
   ====
   
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       
   
        def testOne(self):
            self.assertIsNot(square_list([]),None,"Use the return statement.")
            self.assertEqual(square_list([1,5,3]),[1,25,9],"Checking the list [1, 5, 3]")
            self.assertEqual(square_list([8]),[64],"Checking the list [8]")
            self.assertEqual(square_list([-2, -1, 0, 1, 2]),[4, 1, 0, 1, 4],"Checking a list with negatives")
   myTests().main()
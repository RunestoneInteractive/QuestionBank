.. activecode:: hill_test2
   :author: Scott Hill
   :difficulty: 1.1587800477
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.2564102564
   :total_students_attempting: 39
   :num_students_correct: 23.0
   :mean_clicks_to_correct: 3.6956521739

   
   Define a function ``square_list(list)`` which takes in a list of numbers, and returns a list of the squares of those numbers.  Example: ``square_list([1,5,3])`` should return ``[1,25,9]``.
   ~~~~
   ====
   
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       
   
        def testOne(self):
            self.assertIsNot(square_list([1,5,3]),None,"Use the return statement.")
            self.assertEqual(square_list([1,5,3]),[1,25,9],"")
            self.assertEqual(square_list([8]),[64],"")
   
   
   myTests().main()
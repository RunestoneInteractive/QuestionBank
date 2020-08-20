.. activecode:: hill2019-function
   :author: Scott Hill
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: TestCases
   :subchapter: Exercises
   :topics: TestCases/Exercises
   :from_source: F
   :autograde: unittest
   :nocodelens: 
   :language: python
   :nopair: 
   :pct_on_first: 0.5555555556
   :total_students_attempting: 9
   :num_students_correct: 9.0
   :mean_clicks_to_correct: 6.0

   Write a function called ``formula`` which takes two values, ``x`` and ``y``, and returns x²+y if y is positive. If y is not positive, your function should return zero.
   ~~~~
   
   ====
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
        def testOne(self):
            self.assertEqual("def" in self.getEditorText(), True,"Make sure a function is defined.")
            self.assertEqual(formula(3,3),12,"")
            self.assertEqual(formula(-2,1),5,"")
            self.assertEqual(formula(3,-3),0,"What did I say to do if y is negative?")
        
   
   myTests().main()
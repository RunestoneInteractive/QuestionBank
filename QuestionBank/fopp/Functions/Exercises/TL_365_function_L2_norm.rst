.. actex:: TL_365_function_L2_norm
   :author: Tyler Luchko
   :difficulty: 1.1489881093
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.0882352941
   :total_students_attempting: 34
   :num_students_correct: 17.0
   :mean_clicks_to_correct: 3.5294117647

        
   Write a function called ``l2_norm`` that takes a vector (``list``)
   of any length as input and returns the :math:`L^{2}\text{-norm}`
   without modifying the input. Use your function to compute and print
   out the :math:`L^{2}\text{-norm}` of the vectors defined below.
   
   Hint: use your solution from a previous exercise to get started.
   ~~~~
   vec_1 = [3,0,-4]
   vec_2 = [17.4, 32.3, -3.14, 79, -55]
   vec_3 = [-39.33, 81.27, -80.88, 85.08, -35.9, 86.42, 49.23, -31.41, 47.38, -80.54]
   
   ====
   from unittest.gui import TestCaseGui
   import re
   import math
   class myTests(TestCaseGui):
       def testOne(self):
    output = self.getOutput().split('\n')
   
    
           norm = lambda vec: math.sqrt(sum([v**2 for v in vec]))
    for vec, line in zip([vec_1, vec_2, vec_3], output):
        self.assertAlmostEqual(l2_norm(vec), norm(vec), 7, 'Checking l2_norm({})'.format(vec))
        self.assertAlmostEqual(float(line), norm(vec), 7, 'Checking output for '+str(vec))
        
   myTests().main()
.. actex:: TL_365_function_midpoint
   :author: Tyler Luchko
   :difficulty: 1.520303436
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.1388888889
   :total_students_attempting: 36
   :num_students_correct: 24.0
   :mean_clicks_to_correct: 9.8333333333

   Write a function to compute the value of a mathematical function midway between two points.  E.g., for 
   
   .. math::
      
      f(x) = (x-1)^2
      
   and point :math:`a=1` and :math:`b=3`, the result is
   
   .. math::
      
      f\left(\frac{a+b}{2}\right) = 1
      
   Your function should be called ``midpoint`` and take a function and two floats as input parameters.
   
   ~~~~
   ====
   from unittest.gui import TestCaseGui
   import math
   class myTests(TestCaseGui):
       def testOne(self):
      _midpoint = lambda func, a, b: func((a+b)/2)
   
      self.assertAlmostEqual(midpoint(lambda x: x**2, 1, 2), _midpoint(lambda x: x**2, 1, 2), 7, 'Checking answer for x**2, x1=1, x2=2')
      self.assertAlmostEqual(midpoint(math.exp, -1, 2), _midpoint(math.exp, -1, 2), 7, 'Checking answer for exp(x), x1=-1, x2=2')
      self.assertAlmostEqual(midpoint(math.sin, -1, -2), _midpoint(math.sin, -1, -2), 7, 'Checking answer for sin(x), x1=-1, x2=-2')
   myTests().main()
.. actex:: TL_365_function_high_low
   :author: Tyler Luchko
   :difficulty: 1.1055332441
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.3333333333
   :total_students_attempting: 36
   :num_students_correct: 24.0
   :mean_clicks_to_correct: 2.7916666667

   Write a function called ``order`` to compute the value of a mathematical function at
   two points, ``low`` and ``high``.  If :math:`f(\mathtt{low}) <
   f(\mathtt{high})`, then return the tuple ``(low, high)``. If
   :math:`f(\mathtt{low}) > f(\mathtt{high})`, then swap ``low`` and
   ``high`` and return the tuple ``(low, high)``.
   
   E.g., for the math function
   
   .. math::
      
      f(x) = -2x+3
   
   .. code:: python
      
      def line(x):
          return -2*x+3
      
   the function could be called as
   
   .. code:: Python
   
      order(line, 1, 10)
   
   and would return ``(10, 1)``. If it was instead called as
      
   .. code:: Python
   
      order(line, 10, 1)
      
   it would also return ``(10, 1)`` as :math:`f(10)< f(1)`.
   ~~~~
   ====
   from unittest.gui import TestCaseGui
   import math
   class myTests(TestCaseGui):
       def testOne(self):
      def _order(func, low, high):
          if func(low) < func(high):
                     return low, high
   return high, low
   
      self.assertEqual(order(lambda x: -2*x+3, 1, 10), _order(lambda x: -2*x+3, 1, 10), 
          'Checking answer for -2*x+3, low=1, high=10')
      self.assertEqual(order(lambda x: -2*x+3, 10, 1), _order(lambda x: -2*x+3, 10, 1), 
          'Checking answer for -2*x+3, low=10, high=1')
      self.assertEqual(order(lambda x: x**2-5, -6, -5), _order(lambda x: x**2-1, -6, -5), 
          'Checking answer for x**2-5, low=-6, high=-5')
   myTests().main()
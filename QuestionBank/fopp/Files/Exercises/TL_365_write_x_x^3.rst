.. actex:: TL_365_write_x_x^3
   :author: Tyler Luchko
   :difficulty: 1.2300870147
   :basecourse: fopp
   :chapter: Files
   :subchapter: Exercises
   :topics: Files/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.0930232558
   :total_students_attempting: 129
   :num_students_correct: 64.0
   :mean_clicks_to_correct: 4.90625

   Generate 101 evenly spaced values between -5 and 5 and compute
   :math:`x^3` of each of these values. Write the result to a file
   called ``pow3.csv`` with one value of :math:`x` and :math:`x^3` per
   line, separated by a comma. Your first two lines should look like
   
   .. code::
      
      -5.,-125.
      -4.9,-117.649
   
   ~~~~
   def linspace(a, b, N):
       dx = (b-a)/(N-1)
       return [a + i*dx for i in range(N)]
   
   def pow3(x):
       return x**3
   
   ====
   from unittest.gui import TestCaseGui
   import re
   import math
   class myTests(TestCaseGui):
       def testOne(self):
           def _linspace(a, b, N):
        dx = (b-a)/(N-1)
        return [a + i*dx for i in range(N)]
    _x = _linspace(-5, 5, 101)
    _y = [val**3 for val in _x]
           _read_x = []
           _read_y = []
           with open('pow3.csv', 'r') as fh:
        for line in fh:
            x, y = line.split(',')
            _read_x.append(float(x))
            _read_y.append(float(y))
    
           self.assertEqual(len(_read_x), len(_x), 'Checking x values')
           self.assertEqual(len(_read_y), len(_y), 'Checking y values')
    for i in range(len(_x)):
        self.assertAlmostEqual(_read_x[i], _x[i], 7, 'Checking x['+str(i)+']')
        self.assertAlmostEqual(_read_y[i], _y[i], 7, 'Checking y['+str(i)+']')
   myTests().main()
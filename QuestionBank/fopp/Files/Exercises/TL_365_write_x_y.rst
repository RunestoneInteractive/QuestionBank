.. actex:: TL_365_write_x_y
   :author: Tyler Luchko
   :difficulty: 1.1965101786
   :basecourse: fopp
   :chapter: Files
   :subchapter: Exercises
   :topics: Files/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.1614583333
   :total_students_attempting: 192
   :num_students_correct: 116.0
   :mean_clicks_to_correct: 4.3362068966

   Write the contents of the ``x`` and ``y`` lists to a file called
   ``xy2.dat`` with one value from ``x`` and ``y`` on each line, separated by a comma.
   
   ~~~~
   
   x = [-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4,
        -0.30000000000000004, -0.19999999999999996, -0.09999999999999998,
        0.0, 0.10000000000000009, 0.19999999999999996, 0.30000000000000004,
        0.3999999999999999, 0.5, 0.6000000000000001, 0.7, 0.8,
        0.8999999999999999, 1.0]
   
   y = [1.0, 0.78, 0.67, 0.51, 0.27, 0.0, 0.14, 0.19, -0.14, 0.03,
        0.03, -0.09, -0.03, -0.12, 0.14, 0.36, 0.57, 0.63, 0.61, 0.59, 1.01]
   
   ====
   from unittest.gui import TestCaseGui
   import re
   import math
   class myTests(TestCaseGui):
       def testOne(self):
   
           _x = [-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4,
    	         -0.30000000000000004, -0.19999999999999996, -0.09999999999999998,
          0.0, 0.10000000000000009, 0.19999999999999996, 0.30000000000000004,
          0.3999999999999999, 0.5, 0.6000000000000001, 0.7, 0.8,
          0.8999999999999999, 1.0]
   
           _y = [1.0, 0.78, 0.67, 0.51, 0.27, 0.0, 0.14, 0.19, -0.14, 0.03,
          0.03, -0.09, -0.03, -0.12, 0.14, 0.36, 0.57, 0.63, 0.61, 0.59, 1.01]
   
           _read_x = []
           _read_y = []
           with open('xy2.dat', 'r') as fh:
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
.. actex:: TL_365_read_x_y
   :author: Tyler Luchko
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Files
   :subchapter: Exercises
   :topics: Files/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :available_files: xy.dat
   :pct_on_first: 0.1072961373
   :total_students_attempting: 233
   :num_students_correct: 139.0
   :mean_clicks_to_correct: 7.2661870504

   ``xy.dat`` contains two floating point numbers per line, separated
   by a comma.  Read the contents of ``xy.dat`` and store the first
   number of each line in a list called ``x`` and the second in a list
   called ``y``.  Values should be stored as floats.
   
   
   .. raw:: html
   
      <pre id="xy.dat">
      -2.0,3.97
      -1.75,2.94
      -1.5,2.25
      -1.25,1.59
      -1.0,0.97
      -0.75,0.43
      -0.5,0.38
      -0.25,-0.13
      0.0,0.01
      0.25,0.17
      0.5,0.13
      0.75,0.57
      1.0,1.03
      1.25,1.51
      1.5,2.28
      1.75,3.14
      2.0,3.97
      2.25,5.1
      2.5,6.07
      2.75,7.56
      3.0,8.94
      </pre>
   ~~~~
   ====
   from unittest.gui import TestCaseGui
   import re
   import math
   class myTests(TestCaseGui):
       def testOne(self):
   
           _read_x = []
           _read_y = []
           with open('xy.dat', 'r') as fh:
        for line in fh:
            _x, _y = line.split(',')
            _read_x.append(float(_x))
            _read_y.append(float(_y))
    
           self.assertEqual(len(x), len(_read_x), 'Checking x values')
           self.assertEqual(len(y), len(_read_y), 'Checking y values')
    for i in range(len(_read_x)):
        self.assertAlmostEqual(x[i], _read_x[i], 7, 'Checking x['+str(i)+']')
        self.assertAlmostEqual(y[i], _read_y[i], 7, 'Checking y['+str(i)+']')
    if re.search(r'[^#]+= *open', self.getEditorText(), re.M):
       
        self.assertTrue(re.search(r'[^#]+\.close\(', self.getEditorText(), re.M), 'Checking for matching open and close statements')
    else:
        self.assertTrue(re.search(r'with[ (] *open', self.getEditorText(), re.M), 'Checking open statement')
   myTests().main()
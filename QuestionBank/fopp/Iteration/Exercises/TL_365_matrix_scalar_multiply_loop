.. actex:: TL_365_matrix_scalar_multiply_loop
   :author: Tyler Luchko
   :difficulty: 1.0
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.17
   :total_students_attempting: 100
   :num_students_correct: 36.0
   :mean_clicks_to_correct: 5.4722222222

   
   In the code below, a :math:`3\times3` matrix has been define for
   you. Using loops, update this matrix by scalar multiplying by 5.7.
   
   Hint: you will need two nested loops.
        
   ~~~~
   a = [ [-6  ,   5 ,   3.9],
         [10.1,  -7 ,  -3.6],
   2.1 , -2.1,   5  ] ]
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):  
           ref_a = [ [-6  ,   5 ,   3.9],
                     [10.1,  -7 ,  -3.6],
              [2.1 , -2.1,   5  ] ]
   
    for i in range(len(ref_a)):
        for j in range(len(ref_a[i])):
            ref_a[i][j] = 5.7*ref_a[i][j]
    for i in range(len(ref_a)):
        for j in range(len(ref_a[i])):
            self.assertAlmostEqual(a[i][j], ref_a[i][j], 
         7, 
         'Checking element {:d} {:d}'.format(i, j))
            self.assertFalse(re.search(str(ref_a[i][j]), self.getEditorText()),
         'Checking for hardcoding {:d} {:d}'.format(i, j))
    outer_loops = re.findall(r'^(for .* in.*: *)$', self.getEditorText(), re.M)
    inner_loops = re.findall(r'^( +for .* in.*: *)$', self.getEditorText(), re.M)
    self.assertTrue(len(outer_loops)==1 and len(inner_loops)==1, 'Checking for-statements')
   myTests().main()
.. actex:: TL_365_matrix_scalar_multiply
   :author: Tyler Luchko
   :difficulty: 1.2102002782
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: Exercises
   :topics: Sequences/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.1272727273
   :total_students_attempting: 110
   :num_students_correct: 51.0
   :mean_clicks_to_correct: 4.568627451

   
   In the code below, a :math:`3\times3` matrix has been define for
   you. Update this matrix by scalar multiplying by 5.7.
   
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
   myTests().main()
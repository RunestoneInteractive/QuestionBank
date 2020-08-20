.. actex:: TL_365_matrix_multiply_loop
   :author: Tyler Luchko
   :difficulty: 1.4712182062
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.0675675676
   :total_students_attempting: 74
   :num_students_correct: 16.0
   :mean_clicks_to_correct: 9.0

   
   In the code below, two :math:`3\times3` matrices, ``mat1`` and
   ``mat2``, have been defined for you. Using a loops, `multiply
   <https://en.wikipedia.org/wiki/Matrix_multiplication>`_ these together without
   changing either one and assign the result to a variable called
   ``mat3``.
   
   Hint: you will need three nested loops.
   
   Hint: it is easier if you create ``mat3`` first as a :math:`3\times3` of all zeros.
   
   
   ~~~~
   mat1 = [[94.95, -26.31, -37.12], 
           [-22.37, 27.1, 27.84], 
    [31.12, -21.23, 44.08]]
     
   mat2 = [[-33.66, 68.17, -21.86], 
           [34.1, 90.36, -5.14], 
    [-89.83, 20.29, -43.35]]
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):  
           ref_mat1 = [[94.95, -26.31, -37.12], 
                       [-22.37, 27.1, 27.84], 
                [31.12, -21.23, 44.08]]
     
           ref_mat2 = [[-33.66, 68.17, -21.86], 
                       [34.1, 90.36, -5.14], 
                [-89.83, 20.29, -43.35]]
   
    ref_mat3 = [[0]*3, [0]*3, [0]*3]
    for i in range(len(ref_mat1)):
        for j in range(len(ref_mat1[i])):
            for k in range(len(ref_mat2)):
         ref_mat3[i][j] += ref_mat1[i][k]*ref_mat2[k][j]
    for i in range(len(ref_mat3)):
        for j in range(len(ref_mat3[i])):
            self.assertAlmostEqual(mat3[i][j], ref_mat3[i][j], 
         7, 
         'Checking element {:d} {:d}'.format(i, j))
            self.assertFalse(re.search(str(ref_mat3[i][j]), self.getEditorText()),
         'Checking for hardcoding {:d} {:d}'.format(i, j))
    outer_loops = re.findall(r'^(for .* in.*: *)$', self.getEditorText(), re.M)
    inner_loops = re.findall(r'^( +for .* in.*: *)$', self.getEditorText(), re.M)
    self.assertTrue(len(outer_loops)==1 and len(inner_loops)==2, 'Checking for-statements')
   myTests().main()
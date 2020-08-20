.. actex:: TL_365_matrix_transpose
   :author: Tyler Luchko
   :difficulty: 1.5222668452
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: Exercises
   :topics: TransformingSequences/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.008
   :total_students_attempting: 125
   :num_students_correct: 30.0
   :mean_clicks_to_correct: 9.8666666667

   The transpose of a matrix is flipped along its diagonal.  E.g.,
   an input matrix that looks like
   
   .. math::
      \left[\begin{array}{ccc}
      0 & 1 & 2\\
      3 & 4 & 5
      \end{array}\right]
      
   and will have a ``list`` representation of
   
   .. code:: python
      
      [[0, 1, 2], [3, 4, 5]]
   
   Its transpose will be
   
   .. math::
      \left[\begin{array}{ccc}
      0 & 3\\
      1 & 4\\
      2 & 5
      \end{array}\right]
      
   and will have a ``list`` representation of
   
   .. code:: python
      
      [[0, 3], [1, 4], [2, 5]]	       
     
   Compute the transpose of ``mat_a`` and ``mat_b`` below and store
   them in ``mat_at`` and ``mat_bt`` respectively.
   
   ~~~~
   mat_a = [[15, 1, 56], 
            [98, 86, 10]]
   mat_b = [[66, 53, 77, 65],
      [79, 63, 85, 41], 
     [36, 88, 28, 22],
     [6, 65, 20, 89]]
     
   # create the transposed matrix with all zeros
   mat_at = []
   for j in range(len(mat_a[0])):
       mat_at.append([0]*len(mat_a))
   
   ====
   from unittest.gui import TestCaseGui
   import re
   import math
   class myTests(TestCaseGui):
       def testOne(self):
    output = self.getOutput().split('\n')
    editor = self.getEditorText().split('\n')
    float_re = r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?'
     
    _mat_a = [[15, 1, 56], 
             [98, 86, 10]]
    _mat_b = [[66, 53, 77, 65], 
             [79, 63, 85, 41], 
      [36, 88, 28, 22],
             [6, 65, 20, 89]]
    _mat_at = []
    for j in range(len(_mat_a[0])):
        _mat_at.append([0]*len(_mat_a))
    for i in range(len(_mat_a)):
        for j in range(len(_mat_a[i])):
            _mat_at[j][i] = _mat_a[i][j]
    _mat_bt = []
    for j in range(len(_mat_b[0])):
        _mat_bt.append([0]*len(_mat_b))
    for i in range(len(_mat_b)):
        for j in range(len(_mat_b[i])):
            _mat_bt[j][i] = _mat_b[i][j]
   
    self.assertEqual(mat_at, _mat_at, 'Checking mat_at')
    self.assertEqual(mat_bt, _mat_bt, 'Checking mat_bt')
     
    # hardcode check
    float_re = r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?'
    print_float_re = r'print\( *'+float_re+' *\)'
    self.assertFalse(re.search(print_float_re, self.getEditorText()), 'Checking for hardcoding')
    outer_loops = re.findall(r'^(for .* in.*: *)$', self.getEditorText(), re.M)
    inner_loops = re.findall(r'^( +for .* in.*: *)$', self.getEditorText(), re.M)
    self.assertTrue(len(outer_loops)>=2 and len(inner_loops)==2, 'Checking for-statements')
   myTests().main()
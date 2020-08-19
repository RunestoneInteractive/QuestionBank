.. actex:: TL_365_function_matrix_multiply
   :author: Tyler Luchko
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.0740740741
   :total_students_attempting: 27
   :num_students_correct: 11.0
   :mean_clicks_to_correct: 6.9090909091

   Write a function called ``matmul`` that takes any two matrices and
   returns their `matrix multiplication
   <https://en.wikipedia.org/wiki/Matrix_multiplication>`_ without
   changing either one.
   
   To test your code, use the two :math:`3\times3` matrices, ``mat1``
   and ``mat2``, defined for you. If your code is correct, your
   function should return
   
   .. code:: python
      
      [[0.86814005, 0.88635532],
       [0.6728074 , 1.0937629 ]]
   
   Hint: use your solution from a previous exercise to get started.
   
   ~~~~
   mat1 = [[0.63529553, 0.0765046 , 0.67898779],
    [0.78390698, 0.70503575, 0.04992866]]
   mat2 = [[0.54642394, 0.64040164],
    [0.29474943, 0.79565233],
    [0.73410697, 0.61656478]]
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):  
           _mat1 = [ [-6  ,   5 ],
                 [10.1,  -7 ] ]
     
           _mat2 = [ [1e-2, 1e-3],
                        [1e2 , 1e3 ] ]
   
    def _matmul(mat_a, mat_b):
        mat_c = [[0]*len(mat_b[0]) for row in mat_a]
        for i in range(len(mat_c)):
            for j in range(len(mat_c[i])):
                for k in range(len(mat_b)):
             mat_c[i][j] += mat_a[i][k]*mat_b[k][j]
               return mat_c
        
    mat = matmul(_mat1, _mat2)
    _mat = _matmul(_mat1, _mat2)
    for i in range(len(_mat)):
        for j in range(len(_mat[i])):
            self.assertAlmostEqual(mat[i][j], _mat[i][j], 
         7, 
         'Checking element {:d} {:d}'.format(i, j))
           _mat1 = [[0.63529553, 0.0765046 , 0.67898779],
            [0.78390698, 0.70503575, 0.04992866]]
           _mat2 = [[0.54642394, 0.64040164],
            [0.29474943, 0.79565233],
            [0.73410697, 0.61656478]]
           mat = matmul(_mat1, _mat2)
    _mat = _matmul(_mat1, _mat2)
    for i in range(len(_mat)):
        for j in range(len(_mat[i])):
            self.assertAlmostEqual(mat[i][j], _mat[i][j], 
         7, 
         'Checking element {:d} {:d}'.format(i, j))
   
   
   myTests().main()
.. actex:: TL_365_matrix_define_append
   :author: Tyler Luchko
   :difficulty: 1.0867352193
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: Exercises
   :topics: Sequences/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.1136363636
   :total_students_attempting: 132
   :num_students_correct: 91.0
   :mean_clicks_to_correct: 2.4725274725

   Another way to create a matrix is by combining several already
   define lists using the ``append()`` function.  For example, the matrix 
   
   .. math::
      \mathbf{A}=\left[\begin{matrix}1 & 2 & 3\\
        4 & 5 & 6\\
        7 & 8 & 9
      \end{matrix}\right]
      
   can be created from predefined rows as 
   
   .. code:: python
      
      a = []
      row1 = [1, 2, 3]
      row2 = [4, 5, 6]
      row3 = [7, 8, 9]
   
      a.append(row1)
      a.append(row2)
      a.append(row3)
      
   In the code below, define the matrix 
   
   .. math::
      \mathbf{A}=\left[\begin{matrix}17 & 18 & 19 & 20\\
      7 & 8 & 9 & 10\\
      1.7\times10^{-5} & 3.1 & 4 & 2\\
      -7 & -8 & -9 & -7
      \end{matrix}\right]
     
   from the rows are already defined for you and assign it to a variable called ``mat``.
   
   ~~~~
   a = [7, 8, 9, 10]
   b = [17, 18, 19, 20]
   c = [-7, -8, -9, -7]
   d = [1.7e-5, 3.1, 4, 2]
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):  
           ref_mat = [ [17, 18, 19, 20],
                     [7, 8, 9, 10],
       [1.7e-5, 3.1, 4, 2],
                     [-7, -8, -9, -7] ]
    for i in range(len(ref_mat)):
        for j in range(len(ref_mat[i])):
            self.assertAlmostEqual(mat[i][j], ref_mat[i][j], 
         7, 
         'Checking element {:d} {:d}'.format(i, j))
   myTests().main()
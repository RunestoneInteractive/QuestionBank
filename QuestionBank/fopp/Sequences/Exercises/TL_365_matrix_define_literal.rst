.. actex:: TL_365_matrix_define_literal
   :author: Tyler Luchko
   :difficulty: 1.0
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: Exercises
   :topics: Sequences/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.446969697
   :total_students_attempting: 132
   :num_students_correct: 86.0
   :mean_clicks_to_correct: 1.4069767442

   We can represent a matrix in Python as a ``list`` of ``list`` s.
   We do this by creating a ``list`` in which each element is another
   ``list`` that contains row values. For example, the matrix
   
   .. math::
      \mathbf{A}=\left[\begin{matrix}1 & 2 & 3\\
        4 & 5 & 6\\
        7 & 8 & 9
      \end{matrix}\right]
      
   can be represented in Python as
   
   .. code:: python
      
      a = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
   
   Because Python will automatically continue lines with an ones
   parenthesis or bracket, we can also write it as
      
   .. code:: python
      
      a = [ [1, 2, 3], 
            [4, 5, 6], 
     [7, 8, 9] ]
   
   We can then access element in row and column format.  For example,
   
   .. code:: python
      
      print(a[1][2])
      
   writes out::
   
     6
     
   We can change values using the same approach. For example,
   
   .. code:: python
      
      a[1][2] = 15
      print(a)
      
   writes out::
     
     [[1, 2, 3], [4, 5, 15], [7, 8, 9]]
   
   In the code below, define the matrix 
   
   .. math::
      \mathbf{A}=\left[\begin{matrix}17 & 18 & 19 & 20\\
      7 & 8 & 9 & 10\\
      1.7\times10^{-5} & 3.1 & 4 & 2\\
      -7 & -8 & -9 & -7
      \end{matrix}\right]
     
   and assign it to a variable called ``mat``.
   ~~~~
     
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
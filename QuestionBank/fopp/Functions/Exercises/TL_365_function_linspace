.. actex:: TL_365_function_linspace
   :author: Tyler Luchko
   :difficulty: 1.0
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.0714285714
   :total_students_attempting: 42
   :num_students_correct: 23.0
   :mean_clicks_to_correct: 22.0869565217

   Write a function call ``linspace`` that returns :math:`N` evenly
   spaced values between two points :math:`a` and :math:`b` inclusive.
   Your function should take parameters ``a``, ``b``, and ``N`` and
   return a list of length ``N``.
   
   Using your function, print out the sequence
   
   .. code:: python
      
      [-5. , -4.5, -4. , -3.5, -3. , -2.5, -2. , -1.5, -1. , -0.5,  0. ,
        0.5,  1. ,  1.5,  2. ,  2.5,  3. ,  3.5,  4. ,  4.5,  5. ]
        
   ~~~~
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           def _linspace(a, b, N):
        dx = (b-a)/(N-1)
        return [a + i*dx for i in range(N)]
   
           As = [0, -11.2, 15.1]
           Bs = [10, 3.2, 1]
           Ns = [11, 73, 13]
           for a, b, N in zip(As, Bs, Ns):
               result = linspace(a, b, N)
               _result = _linspace(a, b, N)
               for i in range(len(_result)):
                   self.assertAlmostEqual(result[i], _result[i], 7,
                       "Checking linspace() value {} for a={}, b={}, and N={}".format(i, a, b, N))
   
   myTests().main()
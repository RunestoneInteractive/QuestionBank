.. actex:: TL_365_function_plus_minus_delta
   :author: Tyler Luchko
   :difficulty: 1.2141900937
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.44
   :total_students_attempting: 25
   :num_students_correct: 22.0
   :mean_clicks_to_correct: 4.6363636364

   Functions are also objects.  This means that we can pass function
   object as a parameter to another function. For example, we will
   create a function that applies another function to each element of
   a list. This function looks like:
   
   .. code:: python
      
      def apply_to_each(func, lst_in):
          lst_out = []
          for elem in lst_in:
       lst_out.append(func(elem))
   return lst_out
   
   We can then specify a list and a function to apply to it:
   
   .. code:: python
      
      nums = [1, 2, 3]
      
      def square(x):
          return x**2
   
   Finally, we can apply ``square`` to each element of ``nums``.
   
   .. code:: python
      
      print( apply_to_each(square, nums) )
      
   Notice that there are no arguments or parentheses for ``square``;
   we are pass it as an object.  The output is then
   
   .. code:: python
      
      [1, 4, 9]
   
   Create a function call ``eval_delta`` that returns the values from
   a function evaluated at ``x - dx``, ``x``, ``x+dx``.  It should
   take the function name, ``x``, and ``dx`` as parameters and return
   a tuple of the three values.  The function definition is provided for you.
      
   Use this to evaluate ``square`` at 0.5, 1, 1.5 and print out the
   results.
   
   ~~~~
   def square(x):
       return x**2
       
   def eval_delta( func, x, dx):
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):
           def square(x):
               return x**2
           def mystery(x):
               return x**2/(1+x)
   
           def _eval_delta(func, x, dx):
        return func(x-dx), func(x), func(x+dx)
    xs = [-1.5, 1, 4.73]
    dxs = [.1, 0.5, 3.14159]
           for x, dx in zip(xs, dxs):
               result = eval_delta(square, x, dx)
               _result = _eval_delta(square, x, dx)
               for i in range(len(_result)):
                   self.assertAlmostEqual(result[i], _result[i], 7,
                       'Evaluating square() at {}'.format(x-dx+i*dx))
               result = eval_delta(mystery, x, dx)
               _result = _eval_delta(mystery, x, dx)
               for i in range(len(_result)):
                   self.assertAlmostEqual(result[i], _result[i], 7,
                       'Evaluating a mystery function at {}'.format(x-dx+i*dx))
   myTests().main()
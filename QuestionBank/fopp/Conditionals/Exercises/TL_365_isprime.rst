.. actex:: TL_365_isprime
   :author: Tyler Luchko
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: Exercises
   :topics: Conditionals/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.0126582278
   :total_students_attempting: 79
   :num_students_correct: 29.0
   :mean_clicks_to_correct: 16.2068965517

   A very simple way to tell if a number, :math:`N`, is prime is to try dividing :math:`N` by all integers between 2 and :math:`N/2`. I.e.
   
   1. Set ``isprime=True``.
   
   #. Start with a test factor of 2.
   
   #. Check if the number is divisible by the test factor.
   
   #. If it is divisible, set ``isprime=False``.
   
   #. For each odd number from 3 to :math:`N/2`, if :math:`N` is
      divisible by the number, then set ``isprime=False``
   
   Using this algorithm, determine whether or not 524287 is prime.  Then 
   
   1. print ``True`` if it is prime and ``False`` if it is not, and
      
   2. print the number of iterations through the for-loop you used to get the answer on a second line.
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   import re
   import math
   class myTests(TestCaseGui):
       def testOne(self):
    output = self.getOutput().split('\n')
    editor = self.getEditorText().split('\n')
    float_re = r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?'
    
           N = 524287
           isprime = not N%2==0
    count=0
           for i in range(3,N//2,2):
               isprime = not N%i==0
        count+=1
           self.assertEqual(output[0], str(isprime), 'Checking answer')
           self.assertEqual(output[1], str(count), 'Checking the number of iterations')
            
    # hardcode check
    float_re = r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?'
    print_float_re = r'print\( *'+float_re+' *\)'
    self.assertFalse(re.search(print_float_re, self.getEditorText()), 'Checking for hardcoding')
    outer_loops = re.findall(r'^(for .* in.*: *)$', self.getEditorText(), re.M)
    inner_loops = re.findall(r'^( +for .* in.*: *)$', self.getEditorText(), re.M)
    self.assertTrue(len(outer_loops)==1 or len(inner_loops)==1, 'Checking for-statements')
   myTests().main()
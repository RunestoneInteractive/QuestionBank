.. actex:: ex_6_10_PT
   :author: pranoj thapa
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Selection
   :subchapter: Exercises
   :topics: Selection/Exercises
   :from_source: F
   :practice: T
   :autograde: unittest
   :nocodelens: 
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   Write a function ``is_rightangled`` which, given the length of three sides of a triangle,
   will determine whether the triangle is right-angled.  Assume that the third argument to the
   function is always the longest side.  It will return ``True`` if the triangle
   is right-angled, or ``False`` otherwise.
   
   Hint: floating point arithmetic is not always exactly accurate,
   so it is not safe to test floating point numbers for equality.
   If a good programmer wants to know whether
   ``x`` is equal or close enough to ``y``, they would probably code it up as
   
   .. sourcecode:: python
   
      if  abs(x - y) < 0.001:      # if x is approximately equal to y
          ...
   ~~~~
   def is_rightangled(a, b, c):
       # your code here
   
   ====
   import re
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           editText = self.getEditorText()
           self.assertEqual(2, len(re.findall("\s*return", editText)), "Need two return statements")
           self.assertEqual(is_rightangled(1.5,2.0,2.5),True,"Tested is_rightangled on inputs of 1.5, 2.0 and 2.5")
           self.assertEqual(is_rightangled(4.0,8.0,16.0),False,"Tested is_rightangled on inputs of 4.0, 8.0 and 16.0")
           self.assertEqual(is_rightangled(4.1,8.2,9.1678787077),True,"Tested is_rightangled on inputs of 4.1, 8.2 and 9.1678787077")
           self.assertEqual(is_rightangled(4.1,8.2,9.16787),True,"Tested is_rightangled on inputs of 4.1, 8.2, and 9.16787")
           self.assertEqual(is_rightangled(4.1,8.2,9.168),False,"Tested is_rightangled on inputs of 4.1, 8.2 and 9.168")
           self.assertEqual(is_rightangled(0.5,0.4,0.64031),True,"Tested is_rightangled on inputs of 0.5, 0.4 and 0.64031")
           self.assertEqual(is_rightangled(3,4,5),True,"Tested is_rightangled on inputs of 3, 4 and 5")
           self.assertEqual(is_rightangled(3.5,4.5,5),False,"Tested is_rightangled on inputs of 3.5, 4.5 and 5")
           self.assertEqual(is_rightangled(-6,8,10),True,"Tested is_rightangled on inputs of -6, 8 and 10")
   
   
   
   myTests().main()
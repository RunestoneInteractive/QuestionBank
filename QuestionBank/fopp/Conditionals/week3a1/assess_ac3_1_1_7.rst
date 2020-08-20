.. activecode:: assess_ac3_1_1_7
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: week3a1
   :topics: Conditionals/week3a1
   :from_source: T
   :language: python
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.7798561151
   :total_students_attempting: 695
   :num_students_correct: 682.0
   :mean_clicks_to_correct: 1.3152492669

   We have written conditionals for you to use. Create the variable x and assign it some integer so that at the end of the code, ``output`` will be assigned the string ``"Consistently working"``.
   ~~~~
   if x >= 10:
       output = "working"
   else:
       output = "Still working"
   if x > 12:
       output = "Always working"
   elif x < 7:
       output = "Forever working"
   else:
       output = "Consistently working"
   
   =====
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
      def testOne(self):
         self.assertEqual(output, "Consistently working", "Testing the value of output")
      def testTwo(self):
         self.assertIn(x, [7,8,9,10,11,12], "Testing that x was assigned a correct number" )
   
   myTests().main()
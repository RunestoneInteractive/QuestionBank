.. actex:: actex16_4_2
   :author: bmiller
   :difficulty: 1.0858290304
   :basecourse: fopp
   :chapter: AdvancedFunctions
   :subchapter: Exercises
   :topics: AdvancedFunctions/Exercises
   :from_source: T
   :pct_on_first: 0.5
   :total_students_attempting: 170
   :num_students_correct: 140.0
   :mean_clicks_to_correct: 2.4571428571

   2. Define a function called ``nums`` that has three parameters. The first parameter, an integer, should be required. A second parameter named ``mult_int`` should be optional with a default value of 5. The final parameter, ``switch``, should also be optional with a default value of False. The function should multiply the two integers together, and if switch is True, should change the sign of the product before returning it.
   ~~~~
   
   def nums():
       pass #remove this once you start writing the function
   
   =====
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertEqual(nums(5), 25, "Testing the function nums on input 5.")
           self.assertEqual(nums(2, mult_int = 4), 8, "Testing the function nums on inputs 2, mult_int = 4.")
           self.assertEqual(nums(3, switch = True), -15, "Testing the function nums on inputs 3, switch = True.")
           self.assertEqual(nums(4, mult_int = 3, switch = True), -12, "Testing the function nums on inputs 4, mult_int = 3, switch = True.")
           self.assertEqual(nums(0, switch = True), 0, "Testing the function nums on inputs 0, switch = True.")
   
   myTests().main()
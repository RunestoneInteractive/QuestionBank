.. activecode:: KDL_ch2_2
   :author: Kaelyn Leake
   :difficulty: 1.3081042117
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.0714285714
   :total_students_attempting: 14
   :num_students_correct: 13.0
   :mean_clicks_to_correct: 6.2307692308

   Write a program that will ask the user to enter the ``purchase_amount``. The program should then compute the ``state_sales_tax`` and ``county_sales_tax``. Assume the state sales tax is 5 percent and the county sales tax is 2.5 percent. The program should display the amount of the purchase, the state sales tax, the county sales tax, the ``total_sales_tax``, and the total of the sale (which is the sum of the amount of ``purchase_plus_tax``).
   
   Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to represent 5 percent.
   ~~~~
    
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           ans_t1=0.05*purchase_amount
           ans_t2=0.025*purchase_amount
           ans_t=ans_t1+ans_t2
           ans_ta=purchase_amount+ans_t
           self.assertEqual(ans_t1,state_sales_tax,feedback="correct state sales tax")
           self.assertEqual(ans_t2,county_sales_tax,feedback="correct county sales tax")
           self.assertEqual(ans_t,total_sales_tax,feedback="Correct total sales tax")
           self.assertEqual(ans_ta,purchase_plus_tax,feedback="Correct purchase plus tax")
           self.assertTrue(re.search(str(purchase_amount)[:2], self.getOutput()), 'print purchase.')
           self.assertTrue(re.search(str(state_sales_tax)[:2], self.getOutput()), 'print state sales')
           self.assertTrue(re.search(str(county_sales_tax)[:2], self.getOutput()), 'print county tax.')
           self.assertTrue(re.search(str(total_sales_tax)[:2], self.getOutput()), 'print total tax.')
           self.assertTrue(re.search(str(purchase_plus_tax)[:2], self.getOutput()), 'print purchase plus tax.')
   myTests().main()
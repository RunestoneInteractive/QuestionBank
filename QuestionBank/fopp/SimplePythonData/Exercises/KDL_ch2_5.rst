.. activecode:: KDL_ch2_5
   :author: Kaelyn Leake
   :difficulty: 1.2061579652
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 4.5

   Write a program to make change for an ``amount_of_money`` from 0 through 99 cents input by the user. The output of the program should show the number of coins from each denomination used to make the change.
   The program should return the number of ``quarters``, ``dimes``, ``nickles``, and ``pennies``.
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertEqual(quarters,int(amount_of_money)//25,feedback="The quarters are correct!")
           self.assertEqual(dimes,int(amount_of_money)%25//10,feedback="The dimes are correct!")
           self.assertEqual(nickles,int(amount_of_money)%25%10//5,feedback="The nickles are correct!")
           self.assertEqual(pennies,int(amount_of_money)%25%10%5,feedback="The pennies are correct!")
           self.assertIn('input(', self.getEditorText(), 'Contains user input')
           self.assertIn('print(', self.getEditorText(), 'Contains print')
   myTests().main()
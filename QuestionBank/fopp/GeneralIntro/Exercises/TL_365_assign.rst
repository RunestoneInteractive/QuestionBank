.. actex:: TL_365_assign
   :author: Tyler Luchko
   :difficulty: 1.0033658443
   :basecourse: fopp
   :chapter: GeneralIntro
   :subchapter: Exercises
   :topics: GeneralIntro/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.8878923767
   :total_students_attempting: 223
   :num_students_correct: 210.0
   :mean_clicks_to_correct: 1.0571428571

   Assign the value ``5`` to a variable called ``a``. 
   ~~~~
   ====
   
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(a, 5, 'Checking answer.')
   myTests().main()
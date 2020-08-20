.. actex:: TL_365_assign_1
   :author: Tyler Luchko
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: GeneralIntro
   :subchapter: Exercises
   :topics: GeneralIntro/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.9166666667
   :total_students_attempting: 48
   :num_students_correct: 47.0
   :mean_clicks_to_correct: 1.4893617021

   Assign the value ``5`` to a variable called ``a``. 
   ~~~~
   ====
   
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(a, 5, 'Checking answer.')
   myTests().main()
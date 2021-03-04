.. actex:: TL_365_assign_1
   :author: Tyler Luchko
   :difficulty: 1.0282240071
   :basecourse: fopp
   :chapter: GeneralIntro
   :subchapter: Exercises
   :topics: GeneralIntro/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.9183673469
   :total_students_attempting: 49
   :num_students_correct: 48.0
   :mean_clicks_to_correct: 1.4791666667

   Assign the value ``5`` to a variable called ``a``. 
   ~~~~
   ====
   
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(a, 5, 'Checking answer.')
   myTests().main()
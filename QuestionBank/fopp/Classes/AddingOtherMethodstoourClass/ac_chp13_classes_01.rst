.. activecode:: ac_chp13_classes_01
   :author: bmiller
   :difficulty: 1.0990430859
   :basecourse: fopp
   :chapter: Classes
   :subchapter: AddingOtherMethodstoourClass
   :topics: Classes/AddingOtherMethodstoourClass
   :from_source: T
   :tags: Classes/ImprovingourConstructor.rst, Classes/AddingOtherMethodstoourClass.rs
   :pct_on_first: 0.3545454545
   :total_students_attempting: 550
   :num_students_correct: 405.0
   :mean_clicks_to_correct: 2.6814814815

   
   =====
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
      def testOne(self):
         self.assertEqual(spider.arms, 4, "Testing that spider was assigned the correct number of arms.")
         self.assertEqual(spider.legs, 4, "Testing that spider was assigned the correct number of legs.")
         self.assertEqual(spidlimbs, 8, "Testing that spidlimbs was assigned correctly.")
   
   myTests().main()
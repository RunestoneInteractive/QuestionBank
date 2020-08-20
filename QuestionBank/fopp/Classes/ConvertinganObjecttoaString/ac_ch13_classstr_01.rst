.. activecode:: ac_ch13_classstr_01
   :author: bmiller
   :difficulty: 1.1335118251
   :basecourse: fopp
   :chapter: Classes
   :subchapter: ConvertinganObjecttoaString
   :topics: Classes/ConvertinganObjecttoaString
   :from_source: T
   :tags: Classes/ImprovingourConstructor.rst, Classes/AddingOtherMethodstoourClass.rst, Classes/ConvertinganObjecttoaString.rst
   :pct_on_first: 0.218487395
   :total_students_attempting: 476
   :num_students_correct: 315.0
   :mean_clicks_to_correct: 3.2666666667

   
   =====
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
      def testOne(self):
         self.assertEqual(c1.__str__(), "Corn Flakes cereal is produced by Kellogg's and has 2 grams of fiber in every serving!", "Testing that c1 prints correctly.")
      def testTwo(self):
         self.assertEqual(c2.__str__(), "Honey Nut Cheerios cereal is produced by General Mills and has 3 grams of fiber in every serving!", "Testing that c2 prints correctly.")
   
   myTests().main()
.. actex:: LHSChapterNineQuestionOne
   :author: Wesley Thang
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Strings
   :subchapter: Exercises
   :topics: Strings/Exercises
   :from_source: F

   Write a function that reverses its string argument.
   ~~~~
   def reverse(astring):
       # your code here

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

     def testOne(self):
         self.assertEqual(reverse("happy"),"yppah","Tested reverse on input of 'happy'")
         self.assertEqual(reverse("Python"),"nohtyP","Tested reverse on input of 'Python'")
         self.assertEqual(reverse(""),"","Tested reverse on input of ''")




   myTests().main()
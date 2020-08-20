.. activecode:: retention_14_F16_q21
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPIntroDecisions
   :subchapter: Exercises
   :topics: CSPIntroDecisions/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :chatcodes:
   :practice: T
   :topics: Final_Exam_F16/q_21

   Define a function called **shortest_string** that takes a list of strings as input and returns
   the string with the fewest characters in it. (You can assume that one string in any input list will
   be shorter than the rest.) 

   ~~~~

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

     def testOne(self):
         L = ["ABCDE", "ABC", "ABCDEFGH"]
         self.assertEqual(shortest_string(L), "ABC", "Testing whether ``shortest_string(L)`` returns the right value.")

   myTests().main()
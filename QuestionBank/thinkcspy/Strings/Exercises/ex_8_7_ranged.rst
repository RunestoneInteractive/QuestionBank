.. actex:: ex_8_7_ranged
   :author: Karl Sickendick
   :difficulty: 2.0
   :basecourse: thinkcspy
   :chapter: Strings
   :subchapter: Exercises
   :topics: Strings/Exercises
   :from_source: F
   :practice: T
   :autograde: unittest
   :pct_on_first: 0.25
   :total_students_attempting: 16
   :num_students_correct: 11.0
   :mean_clicks_to_correct: 2.9090909091

   Write a function that removes all occurrences of specific letters from a string.  The letters to remove are all of them that are between the two input letters, inclusive.
   
   As an example, remove_letters("a", "d", "Dog, Bog, Sog, Abcdefg") should return "og, og, Sog, efg".
   ~~~~
   def remove_letters(first_letter, last_letter, theString):
       # your code here
   
   ====
   
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
     def testOne(self):
         self.assertEqual(remove_letters("a", "m","apple"),"pp","Tested remove_letters on inputs of 'a', 'm', and 'apple'")
         self.assertEqual(remove_letters("a", "f", "banana"),"nn","Tested remove_letters on inputs of 'a', 'f', and 'banana'")
         self.assertEqual(remove_letters("z", "z","banana"),"banana","Tested remove_letters on inputs of 'z', 'z', and 'banana'")
   
   
   
   myTests().main()
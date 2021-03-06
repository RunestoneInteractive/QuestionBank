.. actex:: rab_hw_ex_01_ch_09
   :author: Richard Bernatz
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Strings
   :subchapter: Exercises
   :topics: Strings/Exercises
   :from_source: F
   :nocodelens: 
   :pct_on_first: 0.0594059406
   :total_students_attempting: 101
   :num_students_correct: 84.0
   :mean_clicks_to_correct: 30.3333333333

   Write a function called ```is_valid_isbn(astring)``` that takes the string entitled "astring" and returns the Boolean result of checking if astring is a valid ISBN (International Standard Book Number) number. The parameter "astring" has two common formats. One is "a-bcde-fghi-j," and the other is "abcdefghij." The first digit "a" denotes the country where the book is published or the language of the book. The digits "bcde" identify the publisher, the digits "fghi" the book, and the digit "j" represents the "check digit." It value is such that 
   
   (10*a + 9*b + 8*c + 7*d + 6*e + 5*f + 4*g + 3*h + 2*i + j) mod 11 = 0  
   
   The character "X" is used for the digit j if j must be 10.
   
   
   ~~~~
   def is_valid_isbn(astring):
       # your code here
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(is_valid_isbn("0-9654-8534-X") , True, "Tested 0-9654-8534-X ")
           self.assertEqual(is_valid_isbn("1-2345-6789-0"), False, "Tested 1-2345-6789-0" )
           self.assertEqual(is_valid_isbn("1234567890"), False, "Tested 1234567890")
           self.assertEqual(is_valid_isbn("0-7167-4992-0"), True, "Tested  0-7167-4992-0")
           self.assertEqual(is_valid_isbn("0716749920"), True,  "Tested  0716749920")
   
   
   myTests().main()
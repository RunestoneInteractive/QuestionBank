.. actex:: ex_8_8_PT
   :author: pranoj thapa
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Strings
   :subchapter: Exercises
   :topics: Strings/Exercises
   :from_source: F
   :practice: T
   :autograde: unittest
   :nocodelens: 
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 2.0

   Write a function that recognizes palindromes. (Hint: use your ``reverse`` function to make this easy!).
   ~~~~
   def is_palindrome(myStr):
       # your code here
   
   ====
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(is_palindrome("abba"),True,"Tested is_palindrome on input of 'abba'")
           self.assertEqual(is_palindrome("abab"),False,"Tested is_palindrome on input of 'abab'")
           self.assertEqual(is_palindrome("kayak"),True,"Tested is_palindrome on input of 'kayak'")
           self.assertEqual(is_palindrome("Kayak"),False,"Tested is_palindrome on input of 'Kayak'")
           self.assertEqual(is_palindrome("straw warts"),True,"Tested is_palindrome on input of 'straw warts'")
           self.assertEqual(is_palindrome("a"),True,"Tested is_palindrome on input of 'a'")
           self.assertEqual(is_palindrome(""),True,"Tested is_palindrome on input of ''")
   
   
   
   
   myTests().main()
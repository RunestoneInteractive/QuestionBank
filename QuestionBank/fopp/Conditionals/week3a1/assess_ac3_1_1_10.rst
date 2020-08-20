.. activecode:: assess_ac3_1_1_10
   :author: bmiller
   :difficulty: 1.0476301705
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: week3a1
   :topics: Conditionals/week3a1
   :from_source: T
   :language: python
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.5610795455
   :total_students_attempting: 704
   :num_students_correct: 533.0
   :mean_clicks_to_correct: 1.808630394

   For each string in ``wrd_lst``, find the number of characters in the string. If the number of characters is less than 6, add 1 to ``accum`` so that in the end, ``accum`` will contain an integer representing the total number of words in the list that have fewer than 6 characters.
   ~~~~
   wrd_lst = ["Hello", "activecode", "Java", "C#", "Python", "HTML and CSS", "Javascript", "Swift", "php"]
   
   =====
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
      def testOne(self):
         self.assertEqual(accum, 5, "Testing the value of accum")
         self.assertIn('for ', self.getEditorText(), "Testing that your code has a for loop")
   
   myTests().main()
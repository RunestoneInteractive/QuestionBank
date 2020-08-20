.. actex:: CS152_upper_last_word
    :author: John Cigas
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
    :total_students_attempting: 20
    :num_students_correct: 13.0
    :mean_clicks_to_correct: 9.7692307692

    Write a fruitful function called ``upper_last_word(aString)`` that takes a string as an argument
    and returns that same string with the last word in upper case.
    ~~~~
    
    def upper_last_word(aString):
        # your code here
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
         def testOne(self):
    
             self.assertEqual(upper_last_word("yes or no"),"yes or NO","yes or no")
             self.assertEqual(upper_last_word("i am a student"),"i am a STUDENT","i am a student")
             self.assertEqual(upper_last_word("Good Job"),"Good JOB","Good Job")
             self.assertEqual(upper_last_word("yes"),"YES","yes")
             self.assertEqual(upper_last_word("NO"),"NO","NO")
    
    myTests().main()
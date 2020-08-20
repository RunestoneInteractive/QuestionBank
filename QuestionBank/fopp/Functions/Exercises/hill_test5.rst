.. activecode:: hill_test5
    :author: Scott Hill
    :difficulty: 1.3935742972
    :basecourse: fopp
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: F
    :language:python: 
    :autograde: unittest
    :pct_on_first: 0.1111111111
    :total_students_attempting: 36
    :num_students_correct: 22.0
    :mean_clicks_to_correct: 7.6818181818

    Define a function ``first_letters(sentence)`` which takes in a string, and counts the number of words that begin with each letter of the alphabet. The function should return a dictionary.  Example: ``first_letters(“She sold six buns today”)`` should return ``{‘s’: 3, ‘b’: 1, ‘t’: 1}``. 
    ~~~~
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            self.assertEqual(first_letters("she sold six buns today"),{'s':3,'b':1,'t':1},"she sold six buns today")
            self.assertEqual(first_letters("She sold six buns today"),{'s':3,'b':1,'t':1},"Lower-case and capital letters should be added together.")
            self.assertEqual(first_letters("rubber baby buggy bumpers"),{'r':1,'b':3},"Another sentence")
        
    
    myTests().main()
.. activecode:: asu_cs_recusion_q1
    :author: Erdogan Dogdu
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: IntroRecursion
    :subchapter: Exercises
    :topics: IntroRecursion/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0
    :total_students_attempting: 11
    :num_students_correct: 5.0
    :mean_clicks_to_correct: 10.8

    Write the function ``palindrome(s)`` which takes a string ``s`` and check if it is
    palindrome. Returns True if palindrome, False otherwise.
    
    Write the function described recursively. You should have not for or while loops
    in your code.
    
    ~~~~
    
    def palindrome(s)
        0 # write your code here
    
    # Make your own test cases here
    
    ====
    import sys
    import re
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
    
            # hide print()
            fname = "test.out"
            sys.stdout = open(fname, "w")
    
            editText = self.getEditorText()
            numForWhile = len(re.findall("\s*while[( ]", editText)) + len(re.findall("\s*for ", editText))
            if numForWhile > 0:
                self.assertEqual(numForWhile, 0, "Used a for or while in code")
                return
    
            # Make an object
            self.assertEqual(palindrome("kayak"), True, "Testing 'kayak'")
            self.assertEqual(palindrome("hurrah"), False, "Testing 'hurrah'")
            self.assertEqual(palindrome("abccba"), True, "Testing 'abccba'")
            self.assertEqual(palindrome("a"), True, "Testing 'a'")
            self.assertEqual(palindrome("Was it a car or a cat I saw"), True, "Testing 'Was it a car or a cat I saw'.\nNeed to ignore spaces and not case sensitive!")
    
    myTests().main()
.. activecode:: asu_cs_rec_q3
    :author: Erdogan Dogdu
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: IntroRecursion
    :subchapter: Exercises
    :topics: IntroRecursion/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.4615384615
    :total_students_attempting: 13
    :num_students_correct: 12.0
    :mean_clicks_to_correct: 2.1666666667

    Write a **recursive** boolean function ``palindrome(lst)`` that
    ``lst`` is a list and the function returns
    True if the first half of elements are a reflection of the second half of the elements.
    For example, ``palindrome(['a','b','c','b','a'])`` should return True.
    
    Hint: Check the first and the last element, and if the middle is a palindrome.
    
    ~~~~
    def palindrome(lst):
        # Your code here
    
    # Your test code here, next example returns True.
    print(palindrome([1,2,3,3,2,1]))
    
    ====
    import re
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            SelfTest = False
            if (SelfTest):
                self.assertEqual(0,1,"Auto-testing if OFF - you must check the program yourself for now")
                return
    
            print('Auto-testing...')
    
            self.assertGreaterEqual(self.getEditorText().count('palindrome('), 3, 'Make sure you have recursive calls')
            if self.getEditorText().count('palindrome(') < 3:
                return
    
            tests = [
                 ([1,3,5,3,1],True,'palindrome({})->{}'),
                 ([1,1],True,'palindrome({})->{}'),
                 ([0],True,'palindrome({})->{}')
            ]
    
            for t in tests:
                self.assertEqual(palindrome(t[0]), t[1], t[2].format(t[0],t[1]) )
    
    myTests().main()
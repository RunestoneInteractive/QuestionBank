.. activecode:: assess_ps3_1_1_5
    :author: bmiller
    :difficulty: 1.1346732784
    :basecourse: fopp
    :chapter: Conditionals
    :subchapter: week3a1
    :topics: Conditionals/week3a1
    :from_source: T
    :language: python
    :autograde: unittest
    :practice: T
    :pct_on_first: 0.4363636364
    :total_students_attempting: 825
    :num_students_correct: 639.0
    :mean_clicks_to_correct: 3.2863849765

    Write code that will count the number of vowels in the sentence ``s`` and assign the result to the variable ``num_vowels``. For this problem, vowels are only a, e, i, o, and u. Hint: use the ``in`` operator with ``vowels``.
    ~~~~
    s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
    vowels = ['a','e','i','o','u']
    
    # Write your code here.
    
    
    =====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
           self.assertEqual(num_vowels, 32, "testing whether num_vowels is set correctly")
    
        def testOneA(self):
           self.assertIn('for', self.getEditorText(), "Testing that you are using a for loop.")
    
    myTests().main()
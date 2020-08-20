.. activecode:: assess_ps3_1_1_3
    :author: bmiller
    :difficulty: 1.1013807053
    :basecourse: fopp
    :chapter: Conditionals
    :subchapter: week3a1
    :topics: Conditionals/week3a1
    :from_source: T
    :language: python
    :autograde: unittest
    :practice: T
    :pct_on_first: 0.5286549708
    :total_students_attempting: 855
    :num_students_correct: 685.0
    :mean_clicks_to_correct: 2.7211678832

    Write code to count the number of strings in list ``items`` that have the character ``w`` in it. Assign that number to the variable ``acc_num``.
    
    HINT 1: Use the accumulation pattern!
    
    HINT 2: the ``in`` operator checks whether a substring is present in a string.
    
    
    Hard-coded answers will receive no credit.
    ~~~~
    items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
    
    
    =====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            self.assertIn(' in ', self.getEditorText(), "Testing that you are using the in operator.")
            self.assertEqual(acc_num, 4, "Testing that acc_num has been set to the number of strings that have 'w' in them.")
    
    myTests().main()
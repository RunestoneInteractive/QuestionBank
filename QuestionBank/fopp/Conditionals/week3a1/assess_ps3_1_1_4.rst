.. activecode:: assess_ps3_1_1_4
    :author: bmiller
    :difficulty: 1.1647135889
    :basecourse: fopp
    :chapter: Conditionals
    :subchapter: week3a1
    :topics: Conditionals/week3a1
    :from_source: T
    :language: python
    :autograde: unittest
    :practice: T
    :pct_on_first: 0.3493234932
    :total_students_attempting: 813
    :num_students_correct: 609.0
    :mean_clicks_to_correct: 3.7963875205

    Write code that counts the number of words in ``sentence`` that contain *either* an "a" or an "e". Store the result in the variable ``num_a_or_e``.
    
    Note 1: be sure to not double-count words that contain both an a and an e.
    
    HINT 1: Use the ``in`` operator.
    
    HINT 2: You can either use ``or`` or ``elif``.
    
    
    Hard-coded answers will receive no credit.
    ~~~~
    sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
    
    
    =====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            self.assertIn(' in ', self.getEditorText(), "Testing that you are using the in operator.")
            self.assertEqual(num_a_or_e, 14, "Testing that num_a_or_e has been set to the correct number.")
    
    myTests().main()
.. activecode:: mihaela_hw1_p1
    :author: Mihaela Sabin
    :difficulty: 1.1598776057
    :basecourse: fopp
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :practice: T
    :pct_on_first: 0.0909090909
    :total_students_attempting: 33
    :num_students_correct: 21.0
    :mean_clicks_to_correct: 3.7142857143

    Implement a function called pow_answer that has 2 parameters, base and exponent.
    The function computes the value of the base to the power of the exponent.
    It then returns a friendly answer
    For example, calling pow_answer(2, 3) returns:
    Value of 2 to the power of 3 is 8
    ~~~~
    def pow_answer(base, exponent):
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def test_2_3(self):
            self.assertEqual(pow_answer(2, 3), None, "Value of 2 to the power of 3 is 8")
        def test_1_10(self):
            self.assertEqual(pow_answer(1, 10), None, "Value of 1 to the power of 10 is 1")
    
    
    myTests().main()
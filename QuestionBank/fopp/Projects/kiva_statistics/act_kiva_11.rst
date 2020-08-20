.. activecode:: act_kiva_11
    :author: bmiller
    :difficulty: 1.2975554241
    :basecourse: fopp
    :chapter: Projects
    :subchapter: kiva_statistics
    :topics: Projects/kiva_statistics
    :from_source: T
    :include: act_kiva_1
    :pct_on_first: 0.1988071571
    :total_students_attempting: 503
    :num_students_correct: 387.0
    :mean_clicks_to_correct: 6.0516795866

    Calculate the standard deviation of the loan_amount variable and store the variance in loan_var and the standard deviation in ``loan_stdev``.
    ~~~~
    # Your code here
    ====
    from unittest.gui import TestCaseGui
    
    class MyTests(TestCaseGui):
    
        def testOne(self):
            self.assertTrue('loan_stdev' in self.getEditorText(), "you need a loan_stdev variable")
            self.assertAlmostEqual(loan_var, 250456.0, 1, "")
            self.assertAlmostEqual(loan_stdev, 500.456, 3,  "Hint: x ** 0.5  is the same as the square root")
    
    
    MyTests().main()
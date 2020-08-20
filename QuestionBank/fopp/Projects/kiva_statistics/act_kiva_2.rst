.. activecode:: act_kiva_2
    :author: bmiller
    :difficulty: 1.1117551286
    :basecourse: fopp
    :chapter: Projects
    :subchapter: kiva_statistics
    :topics: Projects/kiva_statistics
    :from_source: T
    :include: act_kiva_1
    :pct_on_first: 0.4009852217
    :total_students_attempting: 1015
    :num_students_correct: 925.0
    :mean_clicks_to_correct: 2.8972972973

    Compute the total amount of money loaned and store it in the variable ``loan_total``
    ~~~~
    # Your code here
    ====
    from unittest.gui import TestCaseGui
    
    class MyTests(TestCaseGui):
    
        def testOne(self):
            self.assertTrue('loan_total' in self.getEditorText(), "you need a loan_total variable")
            self.assertEqual(loan_total, sum(loan_amount), "Use the accumulator pattern to add up all the loans")
            self.assertFalse('sum(' in self.getEditorText(), "you may not use sum")
    
    MyTests().main()
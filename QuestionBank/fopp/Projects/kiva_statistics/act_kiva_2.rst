.. activecode:: act_kiva_2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Projects
    :subchapter: kiva_statistics
    :topics: Projects/kiva_statistics
    :from_source: T
    :include: act_kiva_1
    :pct_on_first: 0.4003944773
    :total_students_attempting: 1014
    :num_students_correct: 924.0
    :mean_clicks_to_correct: 2.8993506494

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
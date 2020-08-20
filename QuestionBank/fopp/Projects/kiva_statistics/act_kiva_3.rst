.. activecode:: act_kiva_3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Projects
    :subchapter: kiva_statistics
    :topics: Projects/kiva_statistics
    :from_source: T
    :include: act_kiva_1
    :pct_on_first: 0.5283613445
    :total_students_attempting: 952
    :num_students_correct: 877.0
    :mean_clicks_to_correct: 2.4549600912

    Compute the average amount of money loaned and store it in the variable ``loan_average``
    ~~~~
    # Your code here
    ====
    from unittest.gui import TestCaseGui
    
    class MyTests(TestCaseGui):
    
        def testOne(self):
            self.assertTrue('loan_average' in self.getEditorText(), "you need a loan_total variable")
            self.assertEqual(loan_average, sum(loan_amount)/len(loan_amount), "Use the accumulator pattern to add up all the loans")
            self.assertFalse('sum(' in self.getEditorText(), "you may not use sum")
    
    MyTests().main()
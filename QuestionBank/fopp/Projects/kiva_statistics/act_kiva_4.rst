.. activecode:: act_kiva_4
    :author: bmiller
    :difficulty: 1.2848806418
    :basecourse: fopp
    :chapter: Projects
    :subchapter: kiva_statistics
    :topics: Projects/kiva_statistics
    :from_source: T
    :include: act_kiva_1
    :pct_on_first: 0.1123227917
    :total_students_attempting: 917
    :num_students_correct: 685.0
    :mean_clicks_to_correct: 5.8364963504

    Store the amount of the minimum loan in  ``min_loan`` and the amount of the maximum loan in ``max_loan`` Then, store the name of the country that received the largest loan in ``max_country`` and the smallest loan in ``min_country``  Hint: ``max`` and ``min`` are built in Python functions that you can use to find the minimum value or maximum value in any sequence.
    ~~~~
    # Your code here
    ====
    from unittest.gui import TestCaseGui
    
    class MyTests(TestCaseGui):
    
        def testOne(self):
            self.assertEqual(min_loan, min(loan_amount), "dont be afraid to use the hint")
            self.assertEqual(max_loan, max(loan_amount), "dont be afraid to use the hint")
            self.assertEqual(min_country, country_name[loan_amount.index(min(loan_amount))], "dont be afraid to use the hint")
            self.assertEqual(max_country, country_name[loan_amount.index(max(loan_amount))], "dont be afraid to use the hint")
            self.assertTrue("index" in self.getEditorText())
            self.assertTrue("min(" in self.getEditorText(), "use the min function")
            self.assertTrue("max(" in self.getEditorText(), "use the max function")
    
    
    
    MyTests().main()
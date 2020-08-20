.. activecode:: act_kiva_8
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Projects
    :subchapter: kiva_statistics
    :topics: Projects/kiva_statistics
    :from_source: T
    :include: act_kiva_1
    :pct_on_first: 0.3865905849
    :total_students_attempting: 701
    :num_students_correct: 608.0
    :mean_clicks_to_correct: 3.3338815789

    The index positions for the Phillipines are  ``[5, 6, 9, 11, 13, 14, 22]`` Use that information to compute the average loan amount for the Phillipines.  Store your result in the variable ``p_average``
    ~~~~
    # Your code here
    ====
    from unittest.gui import TestCaseGui
    
    class MyTests(TestCaseGui):
    
        def testOne(self):
            self.assertTrue('p_average' in self.getEditorText(), "you need a p_average variable")
            tot = 0
            for i in [5, 6, 9, 11, 13, 14, 22]:
                tot += loan_amount[i]
            res = tot / 7
            self.assertEqual(p_average, res, "Use the accumulator pattern to add up the loans just for the Philippines")
    
    
    MyTests().main()
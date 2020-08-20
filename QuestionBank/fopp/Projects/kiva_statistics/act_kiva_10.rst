.. activecode:: act_kiva_10
    :author: bmiller
    :difficulty: 1.2435688701
    :basecourse: fopp
    :chapter: Projects
    :subchapter: kiva_statistics
    :topics: Projects/kiva_statistics
    :from_source: T
    :include: act_kiva_1
    :pct_on_first: 0.2942238267
    :total_students_attempting: 554
    :num_students_correct: 407.0
    :mean_clicks_to_correct: 5.1351351351

    What is the arithmetic mean of the time / dollar it takes to fund a loan?  The arithmetic mean is the average of the individual time/dollar calculations, not the average of the sum of time divided by the sum of dollar amounts. Store your result in the variable ``a_mean``
    ~~~~
    # Your code here
    ====
    from unittest.gui import TestCaseGui
    
    class MyTests(TestCaseGui):
    
        def testOne(self):
            self.assertTrue('a_mean' in self.getEditorText(), "you need a a_mean variable")
            self.assertAlmostEqual(a_mean, 1974.424, places=3, feedback="Use the accumulator pattern to add up all the loans")
            self.assertFalse('sum(' in self.getEditorText(), "you should not use sum")
    
    
    MyTests().main()
.. activecode:: act_kiva_6
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Projects
    :subchapter: kiva_statistics
    :topics: Projects/kiva_statistics
    :from_source: T
    :include: act_kiva_1
    :pct_on_first: 0.2366127024
    :total_students_attempting: 803
    :num_students_correct: 647.0
    :mean_clicks_to_correct: 4.3786707883

    Compute the total number of loans made to the Philippines and store it in a variable ``philippines_count``
    ~~~~
    # Your code here
    ====
    from unittest.gui import TestCaseGui
    
    class MyTests(TestCaseGui):
    
        def testOne(self):
            self.assertTrue('philippines_count' in self.getEditorText(), "you need a philippines_count variable")
            self.assertEqual(philippines_count, country_name.count('Philippines'), "")
            self.assertTrue('country_name.count' in self.getEditorText(), "you should use a list method to count")
    
    
    MyTests().main()
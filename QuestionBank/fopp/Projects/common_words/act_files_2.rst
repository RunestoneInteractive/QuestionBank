.. activecode:: act_files_2
    :author: bmiller
    :difficulty: 1.5118562104
    :basecourse: fopp
    :chapter: Projects
    :subchapter: common_words
    :topics: Projects/common_words
    :from_source: T
    :nocodelens: 
    :pct_on_first: 0.1133144476
    :total_students_attempting: 353
    :num_students_correct: 258.0
    :mean_clicks_to_correct: 9.6899224806

    Calculate the total usage percentage for the top 10 words in the list.  Store this result in a variable called ``top_10``  At the same time calculate the percentage for teh bottom 10 words in the list and store that result in ``bottom_10``
    
    ~~~~
    
    ====
    from unittest.gui import TestCaseGui
    
    class MyTests(TestCaseGui):
    
        def testOne(self):
            self.assertAlmostEqual(top_10, 0.276, 3)
            self.assertAlmostEqual(bottom_10, 0.00015, 5)
    MyTests().main()
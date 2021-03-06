.. activecode:: wvu_finalexam_printdict
    :author: Brian Powell
    :difficulty: 1.1178045515
    :basecourse: fopp
    :chapter: Dictionaries
    :subchapter: Exercises
    :topics: Dictionaries/Exercises
    :from_source: F
    :autograde: unittest
    :pct_on_first: 0.1147540984
    :total_students_attempting: 61
    :num_students_correct: 19.0
    :mean_clicks_to_correct: 3.0

    Using the data from the **elections** dictionary, print the year of each presidential election and its winner, one election to a line like:
    
    ``1968: Richard Nixon``
    
    ``1972: Richard Nixon``
    
    ...
    ~~~~
    elections = {1968: 'Richard Nixon', 1972: 'Richard Nixon', 1976: 'Jimmy Carter', 1980: 'Ronald Reagan', 1984: 'Ronald Reagan', 1988: 'George H.W. Bush', 1992: 'Bill Clinton', 1996: 'Bill Clinton', 2000: 'George W. Bush', 2004: 'George W. Bush', 2008: 'Barack Obama', 2012: 'Barack Obama', 2016: 'Donald Trump'}
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            test_one = "print(" in self.getEditorText()
            self.assertEqual(test_one, True, "Displaying output.")
    
            self.assertIn('1972: Richard Nixon\n', self.getOutput(), '1972 displayed')
            self.assertIn('2008: Barack Obama\n', self.getOutput(), '2008 displayed')
    
    myTests().main()
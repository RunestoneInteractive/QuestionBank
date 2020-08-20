.. activecode:: wvu_finalexam_uniquedict
    :author: Brian Powell
    :difficulty: 1.1639019848
    :basecourse: fopp
    :chapter: Dictionaries
    :subchapter: Exercises
    :topics: Dictionaries/Exercises
    :from_source: F
    :autograde: unittest
    :pct_on_first: 0.1896551724
    :total_students_attempting: 58
    :num_students_correct: 23.0
    :mean_clicks_to_correct: 3.7826086957

    Create a list named **presidents** that contains the unique names of the presidents from **elections**. Each president should only appear once in the list.
    ~~~~
    elections = {1968: 'Richard Nixon', 1972: 'Richard Nixon', 1976: 'Jimmy Carter', 1980: 'Ronald Reagan', 1984: 'Ronald Reagan', 1988: 'George H.W. Bush', 1992: 'Bill Clinton', 1996: 'Bill Clinton', 2000: 'George W. Bush', 2004: 'George W. Bush', 2008: 'Barack Obama', 2012: 'Barack Obama', 2016: 'Donald Trump'}
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            self.assertEqual(presidents, list(set(elections.values())), 'Correct list generated.')
    
    myTests().main()
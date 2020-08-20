.. activecode:: wvu_finalexam_sort
    :author: Brian Powell
    :difficulty: 0.0
    :basecourse: fopp
    :chapter: Dictionaries
    :subchapter: Exercises
    :topics: Dictionaries/Exercises
    :from_source: F
    :autograde: unittest
    :pct_on_first: 0.0980392157
    :total_students_attempting: 51
    :num_students_correct: 16.0
    :mean_clicks_to_correct: 4.625

    Create a list named **sorted_presidents** that contains the contents of the **presidents** list, sorted by the presidents' last names.
    ~~~~
    presidents = ['Richard Nixon', 'Jimmy Carter', 'Ronald Reagan', 'George H.W. Bush', 'Bill Clinton', 'George W. Bush', 'Barack Obama', 'Donald Trump']
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            self.assertEqual(sorted_presidents, sorted(presidents, key=lambda x: x.split()[-1]), 'Sorted in correct order.')
    
    myTests().main()
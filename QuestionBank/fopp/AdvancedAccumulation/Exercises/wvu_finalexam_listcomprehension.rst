.. activecode:: wvu_finalexam_listcomprehension
    :author: Brian Powell
    :difficulty: 1.1083801874
    :basecourse: fopp
    :chapter: AdvancedAccumulation
    :subchapter: Exercises
    :topics: AdvancedAccumulation/Exercises
    :from_source: F
    :autograde: unittest
    :pct_on_first: 0.34375
    :total_students_attempting: 32
    :num_students_correct: 25.0
    :mean_clicks_to_correct: 2.84

    Write a list comprehension to filter the values from the **values** list so it includes values that are at least 0 but not more than 100. Place the results in a new list named **filtered_values**.
    ~~~~
    values = [5, 25, -7, 67, 99, 100, 124, 55]
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            self.assertEqual([value for value in values if value >= 0 and value <= 100], filtered_values, "Correct results produced.")
    
            test_two = 'in values if' in self.getEditorText()
            self.assertEqual(test_two, True, 'List comprehension used.')
    
    myTests().main()
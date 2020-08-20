.. activecode:: mihaela_hp1_1
    :author: Mihaela Sabin
    :difficulty: 1.1325301205
    :basecourse: fopp
    :chapter: Sequences
    :subchapter: Exercises
    :topics: Sequences/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :practice: T
    :pct_on_first: 0.2878787879
    :total_students_attempting: 132
    :num_students_correct: 80.0
    :mean_clicks_to_correct: 3.25

    Create a copy of the temps list such that it has all the temperature values in temps,
    but reduced by 10. The copy is called lower_temps and starts as an empty list. 
    Use a for loop to iterate through the temps list and keep building lower_temps list.
    ~~~~
    temps = [95, 87, 100, 84, 78]
    lower_temps = []
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def test1(self):
            result = [85, 77, 90, 74, 68]
            self.assertEqual(lower_temps, result, "All temp values are reduced by 10")
    
    myTests().main()
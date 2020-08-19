.. activecode:: egt_example_Type_activecode_08_unittest_with_gui_nocodelens
    :author: Eric Taucher (Instructor)
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: GeneralIntro
    :subchapter: Exercises
    :topics: GeneralIntro/Exercises
    :from_source: F
    :nocodelens: 
    :pct_on_first: 0.0
    :total_students_attempting: 11
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 2.0

    Fix the following code so that it always correctly adds two numbers.
    ~~~~
    def add(a,b):
        return 4
    
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            self.assertEqual(add(2,2),4,"A feedback string when the test fails")
            self.assertAlmostEqual(add(2.0,3.0), 5.0, 5, "Try adding your parameters")
    
    myTests().main()
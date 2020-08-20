.. activecode:: sigcse_ex1
    :author: Andrew McDonald
    :difficulty: 1.2524383247
    :basecourse: fopp
    :chapter: GeneralIntro
    :subchapter: Exercises
    :topics: GeneralIntro/Exercises
    :from_source: F
    :language: python
    :pct_on_first: 0.0133333333
    :total_students_attempting: 75
    :num_students_correct: 7.0
    :mean_clicks_to_correct: 5.2857142857

    Write a Python function to sum the first N numbers starting with 0.  So if N is 4 then your function should add 0 + 1 + 2 + 3
    ~~~~
    def sum_first_n(N):
        print('your code here')
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            self.assertEqual(sum_first_n(4),6,feedback="0 + 1 + 2 + 3 == 6")
            self.assertEqual(sum_first_n(0),0,feedback="summing 0 numbers should be 0")
    
    myTests().main()
.. activecode:: lhs_7_2
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Selection
    :subchapter: Exercises
    :topics: Selection/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.5219206681
    :total_students_attempting: 479
    :num_students_correct: 476.0
    :mean_clicks_to_correct: 3.0441176471

    Now write the function ``isOdd(n)`` that returns ``True`` when ``n`` is odd and ``False`` otherwise.
    ~~~~
    
    def isOdd(n):
         # your code here
    
    # make some tests for your function
    print( isOdd( try_some_number_here ) )
    print( isOdd( try_some_number_here ) )
    print( isOdd( try_some_number_here ) )
    print( isOdd( try_some_number_here ) )
    
    
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            print("Auto-testing...")
            self.assertEqual(isOdd(10),False,"Tested isOdd on input of 10")
            self.assertEqual(isOdd(5),True,"Tested isOdd on input of 5")
            self.assertEqual(isOdd(1),True,"Tested isOdd on input of 1")
            self.assertEqual(isOdd(0),False,"Tested isOdd on input of 0")
    
    myTests().main()
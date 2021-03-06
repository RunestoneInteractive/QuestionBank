.. activecode:: lhs_test_1
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Labs
    :subchapter: Exercises
    :topics: Labs/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.4244897959
    :total_students_attempting: 245
    :num_students_correct: 172.0
    :mean_clicks_to_correct: 3.2209302326

    **(10 pts)** Write a function called ``f(x)`` that calculates and returns the output of the following function:
    
    ::
    
      f(x) = (2/7)(x-2)(x+3)(2x+1)
    
      Example: f(9) = 456.0
    
    
    ~~~~
    # Your Name:
    
    # Write your code below
    
    ====
    import sys
    from unittest.gui import TestCaseGui
        
    class myTests(TestCaseGui):
            
        def golden_fx(self, x):
            return( (2/7) * (x-2) * (x+3) * (2*x+1) )
    
        def checkf(self, x):
            self.assertEqual(f(x), self.golden_fx(x), "Testing " + str(x) )
            
        def testOne(self):
    
            # hide print()
            fname = "test.out"
            sys.stdout = open(fname, "w")
    
            self.checkf(1)
            self.checkf(0)
            self.checkf(7)
    
            self.deleteFile(fname)
    
        # just opening and closing file does not work, so need a print statement to "empty" the file
        def deleteFile(self, fname):
            # empty out the file so nothing shows
            sys.stdout = open(fname, "w")
            print()
            sys.stdout.close()
                
    myTests().main()
.. activecode:: lhs_test_4
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Labs
    :subchapter: Exercises
    :topics: Labs/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.1829268293
    :total_students_attempting: 246
    :num_students_correct: 137.0
    :mean_clicks_to_correct: 6.3065693431

    **(6 pts)** Write a function called ``middleValue(a,b,c)`` that **returns** the middle integer value (i.e. median)  of the three
    inputs ``a, b, c``. If any of the inputs are the same value, then the middle value is this number.
    
    **Example:** The middle number of 2, 4 and 4 is: 4
    
    ~~~~
    # Your Name:
    
    # Write your code below
    
    ====
    '''
    def middleValue(a, b, c):
        if ((a <= b and b <= c) or (c <= b and b <= a)):
            return(b)
        elif ((a <= c and c <= b) or (b <= c and c <= a)):
            return(c)
        else:
            return(a)
    '''
    import sys
    from unittest.gui import TestCaseGui
            
    class myTests(TestCaseGui):
    
        def golden_mid(self, a, b, c):
            if ((a <= b and b <= c) or (c <= b and b <= a)):
                return(b)
            elif ((a <= c and c <= b) or (b <= c and c <= a)):
                return(c)
            else:
                return(a)
    
        def check(self, a, b, c):
            self.assertEqual(middleValue(a, b, c), self.golden_mid(a, b, c), "Test "+str(a)+" "+str(b)+" "+str(c))
    
        def testOne(self):
    
            # hide print()
            fname = "test.out"
            sys.stdout = open(fname, "w")
    
            self.check(2,3,4)
            self.check(4,3,2)
            self.check(3,2,4)
            self.check(3,4,2)
            self.check(2,4,3)
            self.check(4,2,3)
            self.check(5,5,3)
            self.check(5,5,7)
            self.check(5,3,5)
            self.check(5,7,5)
            self.check(3,5,5)
            self.check(7,5,5)
            self.check(5,5,5)
    
            self.deleteFile(fname)
    
        # just opening and closing file does not work, so need a print statement to "empty" the file
        def deleteFile(self, fname):
            # empty out the file so nothing shows
            sys.stdout = open(fname, "w")
            print("", end="")
            sys.stdout.close()
    
    myTests().main()
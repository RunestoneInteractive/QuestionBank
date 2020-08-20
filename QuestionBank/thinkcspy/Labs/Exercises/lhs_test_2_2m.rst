.. activecode:: lhs_test_2_2m
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Labs
    :subchapter: Exercises
    :topics: Labs/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0
    :total_students_attempting: 5
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 4.0

    **(8 pts)** Create a function ``idNumber(idString)`` that returns an integer 
    of the id number in the ID string.
    
    The ID string has the format ``LHS#####...##`` where the first three characters 
    are always “LHS”. Then it is followed by a sequence of numbers of variable length.
    
    The ID ``LHS123`` has an ID number of ``123``.
    
    The ID ``LHS56789`` has an ID number of ``56789``.
    
    **HINT:** No looping is necessary.
    
    ~~~~
    # Your Name:
    
    # Write your code below
    
    ====
    from unittest.gui import TestCaseGui
        
    import sys
    class myTests(TestCaseGui):
            
        def golden_id(self, idString):
            return(int(idString[3:]))
           
        def check(self, a):
            self.assertEqual(idNumber(a), self.golden_id(a), a)
    
        def testOne(self):
    
            # hide print()
            fname = "test.out"
            sys.stdout = open(fname, "w")
    
            self.check("LHS123")
            self.check("LHS1234567")
    
            self.deleteFile(fname)
    
        # just opening and closing file does not work, so need a print statement to "empty" the file
        def deleteFile(self, fname):
            # empty out the file so nothing shows
            sys.stdout = open(fname, "w")
            print()
            sys.stdout.close()
    
    myTests().main()
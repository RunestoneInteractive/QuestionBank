.. activecode:: lhs_test_5
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Labs
    :subchapter: Exercises
    :topics: Labs/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.2943548387
    :total_students_attempting: 248
    :num_students_correct: 154.0
    :mean_clicks_to_correct: 13.7532467532

    **(6 pts)** Write a function called ``countRandomNumbers(match)`` which generates 20 random numbers
    from 1 to 10 and **returns** how many times the random number matched the input ``match``.
    
    ~~~~
    # Your Name:
    
    # Write your code below
    
    ====
    '''
    import random
    def countRandomNumbers(match):
        count = 0
        for i in range(20):
            number = random.randrange(1,11)
            if number == match:
                count += 1
        return (count)
    '''
    import sys
    from unittest.gui import TestCaseGui
            
    class myTests(TestCaseGui):
    
        def golden_count(self, match):
            count = 0
            for i in range(20):
                number = random.randrange(1,11)
                if number == match:
                    count += 1
            return (count)
    
        def check(self, match):
            random.seed(match)
            retVal = countRandomNumbers(match)
            random.seed(match)
            goldenVal = self.golden_count(match)
            self.assertEqual(retVal, goldenVal, "Test")
    
        def testOne(self):
    
            # hide print()
            fname = "test.out"
            sys.stdout = open(fname, "w")
    
            self.check(5)
            self.check(11)
            self.check(10)
            self.check(3)
    
            self.deleteFile(fname)
    
        # just opening and closing file does not work, so need a print statement to "empty" the file
        def deleteFile(self, fname):
            # empty out the file so nothing shows
            sys.stdout = open(fname, "w")
            print()
            sys.stdout.close()
    
    myTests().main()
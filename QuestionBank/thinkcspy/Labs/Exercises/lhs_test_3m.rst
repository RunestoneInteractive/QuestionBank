.. activecode:: lhs_test_3m
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Labs
    :subchapter: Exercises
    :topics: Labs/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.2
    :total_students_attempting: 10
    :num_students_correct: 3.0
    :mean_clicks_to_correct: 1.3333333333

    **(8 pts)** Write a function called ``addNumbers(start, end, divByN)`` which **returns** the sum of
    all numbers between ``start`` and ``end`` (inclusive of ``start`` and ``end``) that are
    divisible by ``divByN``. All the inputs are positive integers greater than 0.
    
    **Example:** ``addNumbers(2,12,3)`` will return the sum of 3+6+9+12
    
    **Note:** If this is too difficult, then just return the sum of all the numbers between
    ``start`` and ``end`` (inclusive of these numbers) for partial credit.
    
    ~~~~
    # Your Name:
    
    # Write your code below
    
    ====
    '''
    def addNumbers(start, end, divByN):
        sum = 0
        for i in range(start, end+1, 1):
            if (i % divByN) == 0:
                sum = sum + i
        return (sum)
    '''
    
    import sys
    from unittest.gui import TestCaseGui
            
    class myTests(TestCaseGui):
    
        def golden_addNumbers(self, start, end, divByN):
            sum = 0
            for i in range(start, end+1, 1):
                if (i % divByN) == 0:
                    sum = sum + i
            return (sum)
    
        def check(self, start, end, divByN):
            self.assertEqual(addNumbers(start,end,divByN), self.golden_addNumbers(start, end, divByN), "Test")
    
        def testOne(self):
            # hide print()
            fname = "test.out"
            sys.stdout = open(fname, "w")
    
            self.check(2,20,2)
            self.check(2,20,21)
            self.check(4,18,3)
            self.check(4,19,3)
            self.check(4,20,3)
            self.check(4,4,4)
            self.check(5,4,4)
    
            self.deleteFile(fname)
    
        def deleteFile(self, fname):
            # empty out the file so nothing shows
            sys.stdout = open(fname, "w")
            print()
            sys.stdout.close()    
    
    myTests().main()
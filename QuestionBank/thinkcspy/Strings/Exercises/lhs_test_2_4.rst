.. activecode:: lhs_test_2_4
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Strings
    :subchapter: Exercises
    :topics: Strings/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.1138211382
    :total_students_attempting: 246
    :num_students_correct: 106.0
    :mean_clicks_to_correct: 6.6132075472

    **(6 pts)** Create a function ``bunnyFarm(bunnies, rateOfGrowth, limit)`` which returns 
    the number of years it will take until there are too many bunnies in the farm.
    
    ``bunnies`` is the initial amount of bunnies.
    
    ``limit`` is the maximum number of bunnies that can comfortably live on the farm.
    
    ``rateOfGrowth`` is a number which is the rate of growth of the bunnies each year. 
    After 1 year, there are bunnies*(1+rateOfGrowth). (You can assume fractional bunnies 
    for the sake of simplicity. You don’t need to round the bunnies every year.)
    
    Example: ``bunnyFarm(100, 1, 799)``
    
    Year 0: 100 bunnies
    
    Year 1: 200 bunnies
    
    Year 2: 400 bunnies
    
    Year 3: 800 bunnies --> too many bunnies for the farm (max is 799)
    
    
    **Return** the integer 3.
    
    ~~~~
    # Your Name:
    
    # Write your code below
    
    ====
    import sys
    from unittest.gui import TestCaseGui
        
    class myTests(TestCaseGui):
            
        def golden_bunnies(self, bunnies, rateOfGrowth, limit):
            year = 0
            #print("Year {}: {} bunnies".format(year, bunnies))
    
            while bunnies <= limit:
                year += 1
                bunnies = bunnies*(1+rateOfGrowth)
                #print("Year {}: {} bunnies".format(year, bunnies))
        
            return(year)
    
           
        def check(self, a, b, c):
            self.assertEqual(bunnyFarm(a, b, c), self.golden_bunnies(a, b, c), "{} {} {}".format(a, b, c))
    
        def testOne(self):
            # hide print()
            fname = "test.out"
            sys.stdout = open(fname, "w")
    
            self.check(100, 1, 800)
            self.check(100, 1, 799)
            self.check(100, 0.1, 740)
            self.check(120, 0.15, 1122)
    
            self.deleteFile(fname)
    
        def deleteFile(self, fname):
            # empty out the file so nothing shows
            sys.stdout = open(fname, "w")
            print("", end="")
            sys.stdout.close()
    
    myTests().main()
.. activecode:: lhs_5_6
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: PythonModules
    :subchapter: Exercises
    :topics: PythonModules/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.2127659574
    :total_students_attempting: 141
    :num_students_correct: 99.0
    :mean_clicks_to_correct: 10.4242424242

    Write a function ``howManyLessThan(max, num, limit)`` that generates a random number
    from 0 to ``max`` (including the max) repeatedly ``num`` times. The function returns the count of
    how many numbers are less than the ``limit``.
    
    If ``howManyLessThan(12, 10, 4)`` generated the 10 random numbers:
    
    ::
    
      4
      5
      12
      1
      0
      11
      2
      8
      9
      10
    
    Then the function would return 3 since 1, 0 and 2 in the list above are below the limit of 4.
    
    You may assume that ``max`` is a number greater than 1, that ``num`` is a number greater than
    1 and that ``limit`` is any integer.
    
    ~~~~
    # Your Name:
    
    def howManyLessThan ...
        # write you code here
            
    ====
    import sys
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def _golden(self, max, num, limit):
            count = 0
            for _ in range(num):
                rand = random.randrange(max+1)
                if rand < limit:
                    count += 1
            return count
        
        def check(self, max, num, limit):
            random.seed(max)
            count = howManyLessThan(max, num, limit)
    
            random.seed(max)
            golden_count = self._golden(max, num, limit)
    
            self.assertEqual(count, golden_count, "Testing for ({},{}, {})".format(max, num, limit))
            
        def testOne(self):
    
            # disable print()
            fname = "test.out"
            sys.stdout = open(fname, "w")
    
            tests = [ (6, 20, 5), \
                      (10, 100, 8), \
                      (100, 100, 25)
                      ]
    
            for t in tests:
                self.check(t[0], t[1], t[2])
    
            sys.stdout.close()
            self.deleteFile("test.out")
    
        def deleteFile(self, fname):
            # empty out the file so nothing shows
            sys.stdout = open(fname, "w")
            print("", end="")
            sys.stdout.close()
    
    myTests().main()
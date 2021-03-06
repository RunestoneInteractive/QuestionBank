.. activecode:: lhs_test_2_1m
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
    :total_students_attempting: 5
    :num_students_correct: 2.0
    :mean_clicks_to_correct: 3.5

    **(10 pts)** Create a function ``hello(first, last, flavor)`` that **returns** a single string as follows:
    
    ``hello('Steph', 'Curry', 'strawberry')`` returns the string:
    
    ``Hello, my name is Steph Curry. I like strawberry ice cream.`` 
    
    **NOTE:** There is a single space between each word.
    
    ~~~~
    # Your Name:
    
    # Write your code below
    
    ====
    import sys
    from unittest.gui import TestCaseGui
        
    class myTests(TestCaseGui):
            
        def golden_hello(self, first, last, flavor):
            return("Hello, my name is {} {}. I like {} ice cream.".format(first, last, flavor))
    
        def check(self, a, b, c):
            self.assertEqual(hello(a, b, c), self.golden_hello(a, b, c), "Test")
    
        def testOne(self):
    
            # hide print()
            fname = "test.out"
            sys.stdout = open(fname, "w")
    
            self.check("Mark", "Kwong", "vanilla")
            self.check("Steph", "Curry", "rocky road")
                
            self.deleteFile(fname)
    
        # just opening and closing file does not work, so need a print statement to "empty" the file
        def deleteFile(self, fname):
            # empty out the file so nothing shows
            sys.stdout = open(fname, "w")
            print()
            sys.stdout.close()
    
    myTests().main()
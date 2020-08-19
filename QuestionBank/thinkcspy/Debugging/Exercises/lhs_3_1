.. activecode:: lhs_3_1
    :author: LHS CS Team
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: Debugging
    :subchapter: Exercises
    :topics: Debugging/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :nocodelens: 
    :pct_on_first: 0.8240740741
    :total_students_attempting: 648
    :num_students_correct: 624.0
    :mean_clicks_to_correct: 1.8189102564

    Find and fix the error(s) in the following program:
    
    ~~~~
    a = input('wpisz godzine')
    x = input('wpisz liczbe godzin')
    int(x)
    int(a)
    h = x // 24
    s = x % 24
    print (h, s)
    a = a + s
    print ('godzina teraz', a)
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            result = a - s + (x % 24)
            self.assertIn('godzina teraz ' + str(result), self.getOutput(), "Testing output. (Don't worry about Actual and Expected Values.)")
    
    myTests().main()
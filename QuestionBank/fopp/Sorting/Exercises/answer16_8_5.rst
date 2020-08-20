.. actex:: answer16_8_5
    :author: bmiller
    :difficulty: 1.0
    :basecourse: fopp
    :chapter: Sorting
    :subchapter: Exercises
    :topics: Sorting/Exercises
    :from_source: T
    :pct_on_first: 1.0
    :total_students_attempting: 16
    :num_students_correct: 16.0
    :mean_clicks_to_correct: 1.0

    def five_most_frequent(s):
        d = {}
        for x in s:
            if x in d:
                d[x] = d[x] + 1
            else:
                d[x] = 1
    
        s = sorted(d, key=lambda x: d[x], reverse=True)
    
        return s[:5]
    
    =====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
       def testOne(self):
          self.assertEqual(five_most_frequent("aaaaaabbbbbccccdefggghijkk"), ['a', 'b', 'c', 'g', 'k'], "Checking the value returned from using five_most_frequent.")
    
    myTests().main()
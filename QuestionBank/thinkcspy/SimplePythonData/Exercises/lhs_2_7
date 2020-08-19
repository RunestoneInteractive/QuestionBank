.. activecode:: lhs_2_7
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: SimplePythonData
    :subchapter: Exercises
    :topics: SimplePythonData/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.112244898
    :total_students_attempting: 294
    :num_students_correct: 249.0
    :mean_clicks_to_correct: 7.3493975904

    AVERAGE 1
    
    Compute the average of the 3 values ``score1``, ``score2``, ``score3``. They may be different data types, so consider how to deal with that in the average calculation. Print out the average. Then round the average down to the nearest integer and print this value out.  The output should be as below:
    
    ::
    
      The average score is: 5.693
      The rounded down average is: 5
    
    ~~~~
    # Average computation
    
    score1 = 92
    score2 = "93.7"
    score3 = 82.6
    
    # compute and print the average of the three scores
    # put your code here
    
    # round the average score **down** and find the "floor" of this average score - i.e. floor(3.94) = 3
    # print this value out
    # put your code here
    
    =====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testMany(self):
            edText = self.getEditorText()
            outText = self.getOutput()
            outText = " ".join(outText.split())
            self.assertIn("+", edText, "Testing for add operation")
            self.assertIn("/", edText, "Testing for divide operation")
            self.assertIn("float(", edText, "Testing for float conversion")
            self.assertIn("The average score is:", outText, "Testing printout")
            self.assertIn("89.4333333333", outText, "Testing average calculation")
            self.assertIn("The rounded down average is: 89", outText, "Testing rounded down calc printout")
    
    myTests().main()
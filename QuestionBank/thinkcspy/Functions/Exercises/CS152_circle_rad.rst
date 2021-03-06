.. actex:: CS152_circle_rad
    :author: John Cigas
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.1739130435
    :total_students_attempting: 23
    :num_students_correct: 22.0
    :mean_clicks_to_correct: 7.1363636364

    Write a fruitful function ``circle_rad(len, wid)`` that returns the radius of a circle with area len * wid. The formula is to take the square root of len*wid/Pi
    
    
    ~~~~
    
    def circle_rad(len, wid):
        """ Returns the radius of a circle with an area of len * wid """
        # Put your code here
    
    ====
    import re
    import math
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            editText = self.getEditorText()
            self.assertEqual(1, len(re.findall("\s*return ", editText)), "Need exactly one return statement")
            self.assertAlmostEqual(circle_rad(1,1),math.sqrt(1/math.pi),0,"Tested circle_rad(1,1)")
            self.assertAlmostEqual(circle_rad(1,4),math.sqrt(4/math.pi),0,"Tested circle_rad(1,4)")
            self.assertAlmostEqual(circle_rad(5,4), math.sqrt(20/math.pi),0,"Tested circle_rad(5,4)")
    
    
    myTests().main()
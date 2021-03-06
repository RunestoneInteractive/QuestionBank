.. actex:: CS152_perimeter
    :author: John Cigas
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.4
    :total_students_attempting: 25
    :num_students_correct: 23.0
    :mean_clicks_to_correct: 5.6086956522

    Write a fruitful function ``perimeter(len, wid)`` that returns the perimeter of a rectangle with dimensions len and wid
    
    ~~~~
    
    def perimeter(len, wid):
        """ Returns the perimeter of rectangle with dimensions len and wid. """
        # Put your code here
    
    ====
    import re
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            editText = self.getEditorText()
            self.assertEqual(1, len(re.findall("\s*return", editText)), "Need exactly one return statement")
            self.assertAlmostEqual(perimeter(5,6),22,0,"Tested perimeter(5,6)")
            self.assertAlmostEqual(perimeter(6,5),22,0,"Tested perimeter(6,5)")
            self.assertAlmostEqual(perimeter(1,309),620,0,"Tested perimeter(1,309)")
            self.assertAlmostEqual(perimeter(2.5,3.5),12.0,0,"Tested perimeter(2.5,3.5)")
    
    
    
    myTests().main()
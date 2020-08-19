.. activecode:: lhs_2_8
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: SimplePythonData
    :subchapter: Exercises
    :topics: SimplePythonData/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :nocodelens: 
    :pct_on_first: 0.2976190476
    :total_students_attempting: 420
    :num_students_correct: 407.0
    :mean_clicks_to_correct: 3.6142506143

    Write a program that will compute the area of a circle. Prompt the user to enter the radius and print a nice message back to the user with the answer. (change the ``area`` assignment in ``area_of_circle``).
    
    **Note**: There is only a single line that you need to modify below
    ~~~~
    import math
    
    def area_of_circle (r):
        # formula for area of a circle is: (math.pi) times (r squared) 
        area = 0 # ---fix this line only---
        return area
    
    radius = int(input("What is the radius of the circle? "))
    
    print("Area of a circle with radius ", radius,  " is", area_of_circle (radius))
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            self.assertAlmostEqual (  area_of_circle (10), 314.159, 3,"Testing that area_of_circle (10) = 314.159") 
    
    myTests().main()
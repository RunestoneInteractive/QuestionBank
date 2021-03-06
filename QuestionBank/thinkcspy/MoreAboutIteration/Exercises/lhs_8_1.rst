.. activecode:: lhs_8_1
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: MoreAboutIteration
    :subchapter: Exercises
    :topics: MoreAboutIteration/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0873015873
    :total_students_attempting: 504
    :num_students_correct: 469.0
    :mean_clicks_to_correct: 11.7249466951

    Write a function ``print_triangular_numbers(n)`` that prints out the first
    n triangular numbers. A call to ``print_triangular_numbers(5)`` would
    produce the following output::
    
        1       1
        2       3
        3       6
        4       10
        5       15
    
    (*hint: use a web search to find out what a triangular number is.*)
    ~~~~
    def print_triangular_numbers(n):
        # your code here
    
    
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            print("\nAuto-testing...")
    
            oLen = len(self.getOutput())
            print_triangular_numbers(6)
            oLenTest = len(self.getOutput())
            outText = self.getOutput()[oLen:oLenTest]  #extract new output   
            lExpected = [['1', '1'], ['2', '3'], ['3', '6'], ['4', '10'], ['5', '15'], ['6', '21']]
            lActual = []
            lines = outText.splitlines()
            for tnums in lines:
                tnums = tnums.split()
                self.assertEqual(2, len(tnums), "checking only 2 values on each line")
                lActual.append(tnums)
    
            self.assertTrue(lExpected == lActual, "checking expected output for print_triangular_numbers(6)")
    
    myTests().main()
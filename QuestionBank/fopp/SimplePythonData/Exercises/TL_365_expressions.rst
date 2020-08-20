.. activecode:: TL_365_expressions
    :author: Tyler Luchko
    :difficulty: 1.1491502071
    :basecourse: fopp
    :chapter: SimplePythonData
    :subchapter: Exercises
    :topics: SimplePythonData/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.2561983471
    :total_students_attempting: 242
    :num_students_correct: 171.0
    :mean_clicks_to_correct: 3.5321637427

    Write Python expressions and print the result for the following mathematical expressions.  The first one is done for you.  
    
    Do not evaluate the expressions by hand.
    
    .. math::
       &3+6\\
       &-0.35 / 4\\
       &5 / 6\\
       &123456789 / 13\text{ (integer division)}\\
       &2^3 \\       
       &\text{remainder of }123456789 / 13 \\       
       &(116 -3.2)/(2\times7.75)\\       
       &(978 + -3\times-4)^{0.5}\\
    
    ~~~~
    print(3+6)
    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):
        def testOne(self):
            self.assertIn('9\n', self.getOutput(), 'Checking expression 1')
            self.assertIn('-0.0875\n', self.getOutput(), 'Checking expression 2')
            self.assertIn('0.833333333333\n', self.getOutput(), 'Checking expression 3')
            self.assertIn('9496676\n', self.getOutput(), 'Checking expression 4')
            self.assertIn('8\n', self.getOutput(), 'Checking expression 5')
            self.assertIn('7.27741935484\n', self.getOutput(), 'Checking expression 6')
            self.assertIn('1.4642654451\n', self.getOutput(), 'Checking expression 7')
    myTests().main()
.. activecode:: ab_1
    :author: Shishir Shah
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: PythonTurtle
    :subchapter: Exercises
    :topics: PythonTurtle/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :nocodelens: 
    :pct_on_first: 0.0666666667
    :total_students_attempting: 30
    :num_students_correct: 23.0
    :mean_clicks_to_correct: 5.1304347826

    Write a program that uses a ``for`` loop to print out each element and its ``type`` from the following list: ``["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]``.
    
    ~~~~
    # Your code here
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            self.assertIn('for', self.getEditorText(), "Testing your code. (Don't worry about Actual and Expected Values.)")
            self.assertIn("hello " + chr(60) + "class 'str'>", self.getOutput(), "Testing output. (Don't worry about Actual and Expected Values.)")
            self.assertIn("2 " + chr(60) + "class 'int'>", self.getOutput(), "Testing output. (Don't worry about Actual and Expected Values.)")
            self.assertIn("6.0 " + chr(60) + "class 'float'>", self.getOutput(), "Testing output. (Don't worry about Actual and Expected Values.)")
            self.assertIn("7.5 " + chr(60) + "class 'float'>", self.getOutput(), "Testing output. (Don't worry about Actual and Expected Values.)")
            self.assertIn("234352354 " + chr(60) + "class 'int'>", self.getOutput(), "Testing output. (Don't worry about Actual and Expected Values.)")
            self.assertIn("the end " + chr(60) + "class 'str'>", self.getOutput(), "Testing output. (Don't worry about Actual and Expected Values.)")
            self.assertIn(" " + chr(60) + "class 'str'>", self.getOutput(), "Testing output. (Don't worry about Actual and Expected Values.)")
            self.assertIn("99 " + chr(60) + "class 'int'>", self.getOutput(), "Testing output. (Don't worry about Actual and Expected Values.)")
    
    myTests().main()
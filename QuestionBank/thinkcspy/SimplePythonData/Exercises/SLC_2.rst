.. activecode:: SLC_2
    :author: Derek Green
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: SimplePythonData
    :subchapter: Exercises
    :topics: SimplePythonData/Exercises
    :from_source: F
    :language: python
    :autograde: unittest

    Write code to print out the type of the variable ``greeting``, the type of the variable ``wage``, and the type of the variable ``stuff``. (Use the print command!)
    ~~~~
    apples_and_oranges = "Hello there. How are you?"

    wage = 6.75483

    stuff = 824

    ====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):
        def testOne(self):
            self.assertIn('print', self.getEditorText(), "Testing that 'print' is in the code. (Don't worry about Actual and Expected Values.)")
            self.assertIn('type', self.getOutput(), "Testing output. (Don't worry about Actual and Expected Values.)")           

    myTests().main()
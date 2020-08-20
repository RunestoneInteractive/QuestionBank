.. activecode:: wvu_finalexam_stringrep
    :author: Brian Powell
    :difficulty: 0.0
    :basecourse: fopp
    :chapter: Classes
    :subchapter: Exercises
    :topics: Classes/Exercises
    :from_source: F
    :autograde: unittest
    :pct_on_first: 0.1724137931
    :total_students_attempting: 29
    :num_students_correct: 16.0
    :mean_clicks_to_correct: 3.4375

    Add a method to the **Pet** class that generates a string representation that resembles ``Archie: 0.5 years old`` when an instance of the class is printed.
    
    Print the string representation of the **archie** object.
    ~~~~
    class Pet:
        name = None
        age = 0
    
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
        def dog_info(self):
            return "The pet {} is {} years old.".format(self.name, self.age)
    
    archie = Pet("Archie", 0.5)
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            test_one = "print(archie)" in self.getEditorText()
            self.assertEqual(test_one, True, "Call to print output")
    
            test_two = "def __str__(self):" in self.getEditorText() or "def __repr__(self):" in self.getEditorText()
            self.assertEqual(test_two, True, "Method defined.")
    
            self.assertIn('Archie: 0.5 years old', self.getOutput(), 'Correct output displayed.')
    
    myTests().main()
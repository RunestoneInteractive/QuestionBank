.. activecode:: wvu_finalexam_callclass
    :author: Brian Powell
    :difficulty: 1.1054040724
    :basecourse: fopp
    :chapter: Classes
    :subchapter: Exercises
    :topics: Classes/Exercises
    :from_source: F
    :autograde: unittest
    :pct_on_first: 0.1515151515
    :total_students_attempting: 33
    :num_students_correct: 19.0
    :mean_clicks_to_correct: 2.7894736842

    
    Write code using the **archie** object that prints the text `The pet Archie is 0.5 years old.` Make use of the existing **dog_info()** method in your code. Do not modify the existing **dog_info()** method.
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
            self.assertIn('archie.dog_info', self.getEditorText(), 'Existing method is being called.')
            self.assertIn('The pet Archie is 0.5 years old.', self.getOutput(), 'Correct output displayed.')
    
    myTests().main()
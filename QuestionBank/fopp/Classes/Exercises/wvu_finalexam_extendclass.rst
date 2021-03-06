.. activecode:: wvu_finalexam_extendclass
    :author: Brian Powell
    :difficulty: 1.1767068273
    :basecourse: fopp
    :chapter: Classes
    :subchapter: Exercises
    :topics: Classes/Exercises
    :from_source: F
    :autograde: unittest
    :pct_on_first: 0.18
    :total_students_attempting: 50
    :num_students_correct: 34.0
    :mean_clicks_to_correct: 4.0

    
    Write a new class named **Dog** to inherit from the **Pet** class. The new class should have a class variable named **breed** with a default value of ``Unknown``. **Dog**'s constructor must allow users to specify the dog's name, age, and breed.
    
    ~~~~
    class Pet:
        name = None
        age = 0
    
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
        def dog_info(self):
            return "The pet {} is {} years old.".format(self.name, self.age)
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            self.assertEqual('Test Breed', Dog(name='Test Dog', age=5, breed='Test Breed').breed, 'Constructor for class works.')
            self.assertIsInstance(Dog(name='Test Dog', age=5, breed='Test Breed'), Pet, 'Breed inherits properly.')
    
    myTests().main()
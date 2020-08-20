.. activecode:: msmu_class_3
    :author: Irma Ravkic
    :difficulty: 1.2356091031
    :basecourse: fopp
    :chapter: Inheritance
    :subchapter: Exercises
    :topics: Inheritance/Exercises
    :from_source: F
    :autograde: unittest
    :pct_on_first: 0.2
    :total_students_attempting: 15
    :num_students_correct: 10.0
    :mean_clicks_to_correct: 5.0

    
    Write a new class named **Dog** to inherit from the **Pet** class. The new class should have a class variable named **breed** with a default value of ``Unknown``. **Dog**'s constructor must allow users to specify the dog's name, age, and breed.
    To remind yourselves how a class inherits from a super class and how it invokes its constructors please 
    see Section 22.4. To make this work you need to add at most 4-5 lines.
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
.. activecode:: ClassTestTwo
    :author: Wesley Thang
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: ClassesBasics
    :subchapter: Exercises
    :topics: ClassesBasics/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 1.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 1.0

    Create a class called Sports that contains 2 instance variables, ``name`` and
    ``number_of_players``. Add the instance method, ``__str__``, that allows you to
    customize the message returned when you print the instance so that it says
    "The name of the sport is [name goes here] and [number_of_players goes here] people create one team!"
    Create two instances of the class, one assigned to the variable ``football_info`` and
    one called ``quidditch_info``. The first uses ``football`` as the name and has 11 players,
    the second uses ``quidditch`` as the name and has 7 players.
    
    
    ~~~~
    #Define the class here
    
    #Your test code here
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            SelfTest = False
            if (SelfTest):
                self.assertEqual(0,1,"Auto-testing if OFF - you must check the program yourself for now")
                return
    
        def testOne(self):
            self.assertEqual(football_info.__str__(), "The name of the sport is football and 11 people create one team!", "Testing that football_info has the correct value assigned.")
        def testTwo(self):   
            self.assertEqual(quidditch_info.__str__(), 'The name of the sport is quidditch and 7 people create one team!', "Testing that quidditch_info has the correct value assigned.")
         
    myTests().main()
.. activecode:: Hill_examS19_4
   :author: Scott Hill
   :difficulty: 1.2987186843
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.0357142857
   :total_students_attempting: 28
   :num_students_correct: 14.0
   :mean_clicks_to_correct: 6.0714285714

   Write a function ``speak(animal,number)`` which takes in the name of an animal (either ``cow``, ``dog``, or ``pig``) and a number between 1 and 5, and prints their signature utterance (``moo``, ``woof``, or ``oink``) as many times as ``number`` says.  It should print an error message if you choose another animal, or if the number is outside the range above.
   ~~~~
    
   ====
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
        def testOne(self):
            self.assertEqual(speak("cow",3).strip(),"moo moo moo","speak('cow',3)")
            self.assertEqual(speak("pig",2).strip(),"oink oink","spean('pig',2)")
            self.assertEqual(speak("dog",5).strip(),"woof woof woof woof woof","speak('dog',5)")
            self.assertEqual(None,speak("elephant",1),"Your function should return None if a different animal is given.")
            self.assertEqual(None,speak("dog",6),"Your function should return None if the number is not between 1 and 5.")
   
   
   myTests().main()
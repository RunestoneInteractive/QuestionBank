.. activecode:: hill2019-dictionary
   :author: Scott Hill
   :difficulty: 1.4417670683
   :basecourse: fopp
   :chapter: TestCases
   :subchapter: Exercises
   :topics: TestCases/Exercises
   :from_source: F
   :autograde: unittest
   :nocodelens: 
   :language: python
   :nopair: 
   :pct_on_first: 0.0
   :total_students_attempting: 9
   :num_students_correct: 6.0
   :mean_clicks_to_correct: 8.5

   Write a function called ``wordfreq`` which takes in a sentence (as a string without punctuation) and returns a dictionary whose keys are lower-case words and whose values are the number of times that word appears.
   
   For example, ``wordfreq("Her can of fish can feed her")`` should return ``{"her":2,"can":2,"of":1,"fish":1,"feed":1}``
   (The order might vary.)
   ~~~~
   #Enter code here
   
   print(wordfreq("Her can of fish can feed her"))
   ====
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):           
   
        def testOne(self):
            self.assertIsNotNone(wordfreq("hello there"),"Your function needs a return statement.")
            self.assertEqual(wordfreq("her can of fish can feed her"),{"her":2,"can":2,"of":1,"fish":1,"feed":1},"Testing without capitals.")
            self.assertEqual(wordfreq("Her can of fish can feed her"),{"her":2,"can":2,"of":1,"fish":1,"feed":1},"Capitalized words should be made lower-case.")
            self.assertTrue(wordfreq("bob happy happy bob may bob")=={"bob":3,"happy":2,"may":1},"Another sample sentence")
        
   
   myTests().main()
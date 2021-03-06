.. activecode:: hill2019-file
   :author: Scott Hill
   :difficulty: 1.6184738956
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
   :total_students_attempting: 7
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 11.5

   Write a function called ``namecount`` that takes in a list of names and a capital letter, and returns the number of students whose *last* names begin with that letter. An example is given, which should return the number 3.
   
   You may assume that the names are all in the same format as shown below, with one capitalized first name, a space, and then a capitalized last name.
   ~~~~
   def namecount(names,letter):
       #enter code here   
   
   print(namecount([
              'Ron Buskirk', 'Ernie Castlebaum', 'Ivan Drogo', 'Hannah Kane', 
              'Grover Reidemeister', 'Nate Robinson', 'Daniel Rubio', 'James Watson'],"R"))
   
   ====
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):           
        def testOne(self):
            self.assertIsNotNone(namecount(['Scott Hill'],"H"),"Your function needs a return statement.")
            self.assertEqual(namecount(['Ryan Boyd', 'Enrique Castillo', 'Idris Daranijoh', 'Hope Kapelanski', 'Griffin Reynard', 'Nick Rizzo', 'Dayton Rush', 'Jacob Witt'],"R"),3,"The given example")
            self.assertTrue(namecount(['Ryan Boyd', 'Enrique Castillo', 'Idris Daranijoh', 'Hope Kapelanski', 'Griffin Reynard', 'Nick Rizzo', 'Dayton Rush', 'Jacob Witt'],"W")==1,"Another example")
            self.assertTrue(namecount(['Scott Hill','Bob Bob'],"W")==0,"Another example")
   
   
        
   
   myTests().main()
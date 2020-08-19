.. activecode:: caught-speeding
       :author: Barbara  Ericson
       :difficulty: 1.0
       :basecourse: StudentCSP
       :chapter: CSPNameNames
       :subchapter: Exercises
       :topics: CSPNameNames/Exercises
       :from_source: F
       :nocodelens:
       :autograde: unittest

       You are driving a little too fast, and a police officer stops you. Write code to
       compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 
       2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 
       and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless 
       it is your birthday -- on that day, your speed can be 5 higher in all cases.
       For example, if it is your birthday and your speed is 65 you won't get a ticket, 
       but if it isn't your birthday you will get a small ticket (the function will return 1). 
       ~~~~
       def caught_speeding(speed, is_birthday):

       ====
       from unittest.gui import TestCaseGui

       class myTests(TestCaseGui):

           def testOne(self):
               self.assertEqual(caught_speeding(60, False), 0)
               self.assertEqual(caught_speeding(61, False), 1)
               self.assertEqual(caught_speeding(65, False), 1)
               self.assertEqual(caught_speeding(65, True), 0)
               self.assertEqual(caught_speeding(80, False), 1)
               self.assertEqual(caught_speeding(85, False), 2)
               self.assertEqual(caught_speeding(85, True), 1)
               self.assertEqual(caught_speeding(70, False), 1)
               self.assertEqual(caught_speeding(75, True), 1)
               self.assertEqual(caught_speeding(40, False), 0)
               self.assertEqual(caught_speeding(40, True), 0)
               self.assertEqual(caught_speeding(90, False), 2)


       myTests().main()
.. activecode:: personClass-Write
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPNameNames
   :subchapter: Exercises
   :topics: CSPNameNames/Exercises
   :from_source: F
   :autograde: unittest
   :nocodelens: 
   :pct_on_first: 0.4166666667
   :total_students_attempting: 132
   :num_students_correct: 128.0
   :mean_clicks_to_correct: 2.9296875

   Write code to define a Person class.  Each person object has a first and
   last name.  Write a constructor (__init__) which sets the object's 
   first and last names.  Write a 
   method (__str__) to print the object's first name followed by a space 
   and then the last name.  Also write a
   method, initials, which returns the first letter of the first name appended
   with the first letter of the last name.  For example, 
   Person("Barbara", "Ericson") returns "Barbara Ericson" from __str__ and
   "BE" from initials().
   ~~~~
   class Person:
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
       def testOne(self):
           p = Person("Barbara", "Ericson")
           self.assertEqual(p.__str__(), "Barbara Ericson", 'Person("Barbara", "Ericson")')
           self.assertEqual(p.initials(), "BE", 'p.initials()')
           p = Person("Leila", "Jones")
           self.assertEqual(p.__str__(), "Leila Jones", 'Person("Leila", "Jones")')
           self.assertEqual(p.initials(), "LJ", 'p.initials()')
              
   myTests().main()
.. activecode:: ee_exceptions_012
   :author: bmiller
   :difficulty: 1.0644460194
   :basecourse: fopp
   :chapter: Exceptions
   :subchapter: intro-exceptions
   :topics: Exceptions/intro-exceptions
   :from_source: T
   :tags: Exceptions/intro-exceptions.rst
   :practice: T
   :pct_on_first: 0.5573770492
   :total_students_attempting: 183
   :num_students_correct: 170.0
   :mean_clicks_to_correct: 2.0941176471

   5. Below, we have provided a list of tuples that consist of student names, final exam scores, and whether or not they will pass the class. For some students, the tuple does not have a third element because it is unknown whether or not they will pass. Currently, the for loop does not work. Add a try/except clause so the code runs without an error - if there is no third element in the tuple, no changes should be made to the dictionary.
   ~~~~
   
   students = [('Timmy', 95, 'Will pass'), ('Martha', 70), ('Betty', 82, 'Will pass'), ('Stewart', 50, 'Will not pass'), ('Ashley', 68), ('Natalie', 99, 'Will pass'), ('Archie', 71), ('Carl', 45, 'Will not pass')]
   
   passing = {'Will pass': 0, 'Will not pass': 0}
   for tup in students:
       if tup[2] == 'Will pass':
           passing['Will pass'] += 1
       elif tup[2] == 'Will not pass':
           passing['Will not pass'] += 1
   
   =====
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
      def testOne(self):
         self.assertEqual(passing, {'Will pass': 3, 'Will not pass': 2}, "Testing that passing is created correctly.")
   
   myTests().main()
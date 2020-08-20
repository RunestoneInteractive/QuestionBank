.. activecode:: ac_exceptions_011
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Exceptions
   :subchapter: ChapterAssessment
   :topics: Exceptions/ChapterAssessment
   :from_source: T
   :tags: Exceptions/intro-exceptions.rst
   :pct_on_first: 0.9202898551
   :total_students_attempting: 138
   :num_students_correct: 137.0
   :mean_clicks_to_correct: 1.3795620438

   Provided is a buggy for loop that tries to accumulate some values out of some dictionaries. Insert a try/except so that the code passes.
   ~~~~
   
   di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
   total = 0
   for diction in di:
       total = total + diction['Puppies']
   
   print("Total number of puppies:", total)
   
   
   =====
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
      def testOne(self):
         self.assertEqual(total, 130, "Testing that total has the correct value.")
   
   myTests().main()
.. actex:: TL_365_function_in_list
   :author: Tyler Luchko
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.2692307692
   :total_students_attempting: 26
   :num_students_correct: 24.0
   :mean_clicks_to_correct: 8.0416666667

   Write a function called ``in_list`` that reproduces the ``in``
   operator without using the ``in`` operator.  That is it takes
   a list and an object as parameters and returns ``True`` if the object is in
   the list and ``False`` otherwise.
   
   ~~~~
   
   def in_list(lst, obj):
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):
           test_list = [1,2,3,4]
    for elem in test_list+[5,6]:
               self.assertEqual(in_list(test_list, elem), elem in test_list,
            "Looking for {} in {}".format(elem, str(test_list)))
    self.assertFalse(re.search(r'obj *in *lst', self.getEditorText()), 'Checking for hardcoding')
   
   myTests().main()
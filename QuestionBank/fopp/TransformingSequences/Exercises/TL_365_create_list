.. actex:: TL_365_create_list
   :author: Tyler Luchko
   :difficulty: 1.0
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: Exercises
   :topics: TransformingSequences/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.5422535211
   :total_students_attempting: 142
   :num_students_correct: 94.0
   :mean_clicks_to_correct: 1.5106382979

   Create a new list called ``sqrts`` that contains the square root of
   each number in the list ``numbers``.  Your solution should work for
   any number of elements in the list.
   
   First, create an empty list, then add each value using ``append()``.
   
   ~~~~
   numbers = [71, 96, 88, 76, 39, 34, 17, 88, 40, 69, 51, 23, 84, 74, 14, 84, 20, 63, 37]
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   import math
   class myTests(TestCaseGui):
       def testOne(self):
    output = self.getOutput().split('\n')
    editor = self.getEditorText().split('\n')
    float_re = r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?'
    _numbers = [71, 96, 88, 76, 39, 34, 17, 88, 40, 69, 51, 23, 84, 74, 14, 84, 20, 63, 37]
    _sqrts = []
    for i in range(len(numbers)):
        _sqrts.append(numbers[i]**0.5)
   
    self.assertEqual(len(numbers), len(_numbers), 'Checking number of elements')
    for number, _number in zip(numbers, _numbers):
        self.assertEqual(number, _number, 'Checking answer')
   
    self.assertTrue(re.search(r'sqrts *\. *append *\(', self.getEditorText()), 'Checking for append')
        
    # hardcode check
    float_re = r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?'
    print_float_re = r'print\( *'+float_re+' *\)'
    self.assertFalse(re.search(print_float_re, self.getEditorText()), 'Checking for hardcoding')
    outer_loops = re.findall(r'^(for .* in .*: *)$', self.getEditorText(), re.M)
    inner_loops = re.findall(r'^( +for .* in.*: *)$', self.getEditorText(), re.M)
    self.assertTrue(len(outer_loops)>=1 and len(inner_loops)==0, 'Checking for-statements')
   myTests().main()
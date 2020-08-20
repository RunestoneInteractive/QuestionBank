.. actex:: TL_365_pig_latin
   :author: Tyler Luchko
   :difficulty: 1.817492191
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: Exercises
   :topics: TransformingSequences/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.0387596899
   :total_students_attempting: 129
   :num_students_correct: 33.0
   :mean_clicks_to_correct: 14.8787878788

   Pig latin is a `language game or argot
   <https://en.wikipedia.org/wiki/Pig_Latin>`_. The rules are
   
   1. All consonants at the start of the string are moved to the end. (Treat 'y' is a vowel here.)
   
   2. An 'a' is added to the end of the string.
   
   For example, 'string' becomes 'ingstra'.
   
   Copy the list ``english`` into a new list called ``pig_latin`` and translate each word into pig latin.
   You may use ``+`` to create new strings but do not use ``append`` or ``+`` to build the list ``pig_latin``.
        
   ~~~~
   english = ['computational', 'physics', 'is', 'awesome']
   ====
   from unittest.gui import TestCaseGui
   import re
   import math
   class myTests(TestCaseGui):
       def testOne(self):
    output = self.getOutput().split('\n')
    editor = self.getEditorText().split('\n')
    float_re = r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?'
    
    _english = ['computational', 'physics', 'is', 'awesome']
    _pig_latin = _english[:]
    for iword in range(len(_pig_latin)):
        for letter in _pig_latin[iword]:
            if letter not in 'aeiouy':
         _pig_latin[iword] = _pig_latin[iword][1:]+letter
     else:
         break
        _pig_latin[iword] = _pig_latin[iword]+'a'
        
    self.assertEqual(english, _english, 'Checking that the original list has not changed')
    self.assertEqual(pig_latin, _pig_latin, 'Checking the new list')
    
    # hardcode check
    float_re = r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?'
    print_float_re = r'print\( *'+float_re+' *\)'
    self.assertFalse(re.search(print_float_re, self.getEditorText()), 'Checking for hardcoding')
    self.assertFalse(re.search(r'append', self.getEditorText()), 'Checking for hardcoding')
    self.assertTrue(re.search(r'\[.*:.*\]', self.getEditorText()), 'Checking for hardcoding')
    outer_loops = re.findall(r'^(for .* in.*: *)$', self.getEditorText(), re.M)
    inner_loops = re.findall(r'^( +for .* in.*: *)$', self.getEditorText(), re.M)
    self.assertTrue(len(outer_loops)==1 and len(inner_loops)==1, 'Checking for-statements')
   myTests().main()
.. actex:: ex_6_8_PT
    :author: pranoj thapa
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Selection
    :subchapter: Exercises
    :topics: Selection/Exercises
    :from_source: F
    :practice: T
    :autograde: unittest
    :nocodelens: 
    :pct_on_first: 1.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 1.0

    Now write the function ``is_odd(n)`` that returns ``True`` when ``n`` is odd
    and ``False`` otherwise.
    ~~~~
    
    def is_odd(n):
        # your code here
    
    
    ====
    import re
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
         def testOne(self):
             editText = self.getEditorText()
             self.assertEqual(2, len(re.findall("\s*return", editText)), "Need two return statements")
             self.assertEqual(is_odd(10),False,"Tested is_odd on input of 10")
             self.assertEqual(is_odd(5),True,"Tested is_odd on input of 5")
             self.assertEqual(is_odd(1),True,"Tested is_odd on input of 1")
             self.assertEqual(is_odd(0),False,"Tested is_odd on input of 0")
             self.assertEqual(is_odd(-10),False,"Tested is_odd on input of -10")
             self.assertEqual(is_odd(-11),True,"Tested is_odd on input of -11")
    
    
    myTests().main()
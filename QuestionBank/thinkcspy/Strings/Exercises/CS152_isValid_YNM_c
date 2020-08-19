.. actex:: CS152_isValid_YNM_c
    :author: John Cigas
    :difficulty: 2.0
    :basecourse: thinkcspy
    :chapter: Strings
    :subchapter: Exercises
    :topics: Strings/Exercises
    :from_source: F
    :practice: T
    :autograde: unittest
    :nocodelens: 
    :pct_on_first: 0.3076923077
    :total_students_attempting: 13
    :num_students_correct: 12.0
    :mean_clicks_to_correct: 3.5833333333

    Write a function called ``is_validYNM(aString)`` that takes a string as an argument
    and returns ``True`` if the argument is one of **"yes"**, **"no"** or **"maybe"** and ``False`` if
    it is anything else. Case shouldn't matter. Extra spaces at the beginning or end shouldn't matter.
    ~~~~
    
    def is_validYNM(aString):
        # your code here
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
         def testOne(self):
             self.assertEqual(is_validYNM("yes"),True,"yes")
             self.assertEqual(is_validYNM("NO"),True,"NO")
             self.assertEqual(is_validYNM("   yes"),True,"'     yes'")
             self.assertEqual(is_validYNM("NO  "),True,"'NO  '")
             self.assertEqual(is_validYNM("Maybe"),True,"Maybe")
             self.assertEqual(is_validYNM("MaYbE"),True,"MaYbE")
             self.assertEqual(is_validYNM(" MaYbE "),True,"' MaYbE '")
             self.assertEqual(is_validYNM("say what?"),False,"say what?")
             self.assertEqual(is_validYNM(""),False,"''")
             self.assertEqual(is_validYNM("ye"),False,"ye")
             self.assertEqual(is_validYNM("may"),False,"may")
    
    myTests().main()
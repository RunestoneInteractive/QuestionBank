.. actex:: CS152_isValid_YNM_d
    :author: John Cigas
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Strings
    :subchapter: Exercises
    :topics: Strings/Exercises
    :from_source: F
    :practice: T
    :autograde: unittest
    :nocodelens: 
    :pct_on_first: 0.0
    :total_students_attempting: 15
    :num_students_correct: 6.0
    :mean_clicks_to_correct: 12.5

    Write a function called ``is_validYNM(aString)`` that takes a string as an argument
    and returns ``True`` if the argument is one of **"yes"**, **"no"** or **"maybe"** and ``False`` if
    it is anything else. Case shouldn't matter. Extra spaces at the beginning or end shouldn't matter. Allow any valid prefix of a valid word, like 'ye', 'n', or 'mayb'.
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
             #self.assertEqual(is_validYNM(""),False,"''")
             self.assertEqual(is_validYNM("ye"),True,"ye")
             self.assertEqual(is_validYNM("MaY"),True,"MaY")
             self.assertEqual(is_validYNM("N"),True,"N")
             self.assertEqual(is_validYNM("e"),False,"e")
    
    myTests().main()
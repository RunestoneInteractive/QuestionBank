.. activecode:: sks_cw2_ex4
   :author: Shishir Shah
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :autograde: unittest
   :pct_on_first: 0.0622009569
   :total_students_attempting: 209
   :num_students_correct: 149.0
   :mean_clicks_to_correct: 14.1476510067

   [30 pts] Print out the following output.
    
   You must use exactly 2 ``for`` statements, 2 ``range`` statements, and 3 ``print`` statements.
   
   ::
   
     Calculating x ** 1
     1
     3
     5
     ====
     Calculating x ** 2
     1
     9
     25
     ====
     Calculating x ** 3
     1
     27
     125
     ====
   
   ~~~~
   # Write your code here
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
       # counts how many lines have 'keyword' in word position 'where'
       def count_code(self, code, keyword, where):
           cnt = 0
           for line in code.splitlines():
               word = line.split()
               if where < len(word):
                   # parse function keyword
                   if '(' in word[where]:
                       word = word[where].split('(')
                       if word[0] == keyword:
                           cnt = cnt + 1
                   else:
                       if word[where] == keyword:
                           cnt = cnt + 1
           return(cnt)
    
       def testOne(self):
           outText = self.getOutput()
           editText = self.getEditorText()
           golden_str = ""
           for power in range(1,4):
               golden_str = golden_str + "Calculating x ** " + str(power) + "\n"
               for i in range(1,6,2):
                   golden_str = golden_str + str(i ** power) + "\n"
               golden_str = golden_str + "====\n"
                
           self.assertIn(golden_str, outText, "Comparing printed output")
           self.assertNotIn('25', editText, "Checking no hard coded outputs")
           self.assertEqual(2, self.count_code(editText, 'for', 0), "Checking 'for' usage")
           self.assertEqual(2, self.count_code(editText, 'range', 3), "Checking 'range' usage")
           self.assertEqual(3, self.count_code(editText, 'print', 0), "Checking 'print' usage")
        
   myTests().main()
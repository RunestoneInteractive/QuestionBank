.. actex:: cutr_ch08_ex03
  :author: Sandra Jackson
  :difficulty: 1.0
  :basecourse: thinkcspy
  :chapter: MoreAboutIteration
  :subchapter: Exercises
  :topics: MoreAboutIteration/Exercises
  :from_source: F
  :pct_on_first: 0.1176470588
  :total_students_attempting: 34
  :num_students_correct: 24.0
  :mean_clicks_to_correct: 11.875

  In practice, while loops and for loops are used for two very different types of iteration.  One being a definite number of iterations and the other being an uncertain number.  However, knowing how to write various loops both ways is a useful way to practice.  The function 'forLoop' operates on a list.  Read the code to find out what it does, then write a function called 'whileLoop' that does the same thing using a while loop.  The original list should not be modified.
  ~~~~
  
  def forLoop(alist):
       new_list = []
       for each in alist:
            if type(each) is type("string"):
                 new_list.append(each[:1])
       return new_list
       
  def whileLoop(alist):
       # your code here
  
  ====
  from unittest.gui import TestCaseGui
  
  class myTests(TestCaseGui):
  
      def testOne(self):
          a = [7, 6.7, 'right', 'left', 18, 'up', 4.5, 'down']
          self.assertEqual(whileLoop(a),forLoop(a),"Tested on [7, 6.7, 'right', 'left', 18, 'up', 4.5, 'down']")
          self.assertEqual(a,[7, 6.7, 'right', 'left', 18, 'up', 4.5, 'down'],"If this test fails, your function modified the original list.")
          self.assertEqual(whileLoop([]),forLoop([]), "Tested on the Empty List")
  
  myTests().main()
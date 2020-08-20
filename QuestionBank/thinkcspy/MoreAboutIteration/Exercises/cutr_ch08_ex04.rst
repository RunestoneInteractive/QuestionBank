.. actex:: cutr_ch08_ex04
  :author: Sandra Jackson
  :difficulty: 1.0
  :basecourse: thinkcspy
  :chapter: MoreAboutIteration
  :subchapter: Exercises
  :topics: MoreAboutIteration/Exercises
  :from_source: F
  :pct_on_first: 0.6060606061
  :total_students_attempting: 33
  :num_students_correct: 31.0
  :mean_clicks_to_correct: 2.064516129

  Write a function called 'getAges', that continuously prompts the user for ages of some set of individuals.  When the user wants to stop entering ages, there should be an appropriate value they can enter to stop the prompting.  The function should return a list of the entered ages.
  ~~~~
  
  def getAges():
       # your code here
  
  ====
  from unittest.gui import TestCaseGui
  
  class myTests(TestCaseGui):
  
      def testOne(self):
          self.assertEqual(type(getAges()),type([]), "If this test failed the return type of the function is not a list")
  
  myTests().main()
.. actex:: cutr_ch08_ex05
 :author: Sandra Jackson
 :difficulty: 1.0
 :basecourse: thinkcspy
 :chapter: MoreAboutIteration
 :subchapter: Exercises
 :topics: MoreAboutIteration/Exercises
 :from_source: F
 :pct_on_first: 0.2941176471
 :total_students_attempting: 34
 :num_students_correct: 27.0
 :mean_clicks_to_correct: 4.3333333333

 Write a function called 'getTrueFalseResponse', that prompts the user for a True or False answer to a question.  The user is required to enter 'T' for True and 'F' for False.  The function should take a string parameter, that represents the question being posed.  The function must ensure that the user's response matches either 'T' or 'F', if it does the function returns a boolean value matching the user's response.  If the user's response does not match the function should print some sort of useful message, telling them, what they did wrong, and continuously re-prompt for a response that matches one of the expected input possibilities. 
 
 Note that the function is not meant to check the correctness of the True-False answer.  It is just checking that the response is one of the two input possibilities.
 ~~~~
 
 def getTrueFalseResponse():
       # your code here
 
 ====
 from unittest.gui import TestCaseGui
 
 class myTests(TestCaseGui):
 
  def testOne(self):
    self.assertIn(getTrueFalseResponse("It is raining today."),[True,False], "If this test fails the function does not return a boolean True/False value. ")
 
 myTests().main()
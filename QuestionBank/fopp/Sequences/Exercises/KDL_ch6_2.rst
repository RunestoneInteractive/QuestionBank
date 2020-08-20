.. activecode:: KDL_ch6_2
   :author: Kaelyn Leake
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: Exercises
   :topics: Sequences/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.2142857143
   :total_students_attempting: 14
   :num_students_correct: 14.0
   :mean_clicks_to_correct: 9.9285714286

   
   
   A magic 8 ball has the given set of possible answers. Create a program that determines the number of possible solutions and then randomly chooses an answer.
   Print the answer!
   ~~~~
   magi8=['It is certain.','It is decidedly so.','Without a doubt.','Yes - definitely.','You may rely on it.','As I see it, yes.','Most likely.','Outlook good.','Yes','Signs point to yes.','Reply hazy, try again.','Ask again later.','Better not tell you now.','Cannot predict now.','Concentrate and ask again.',"Don't count on it.",'My reply is no.','My sources say no.','Outlook not so good.','Very doubtful.']
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           
           self.assertIn('len(magi8)', self.getEditorText(), 'determines length')
           self.assertIn('random.randrange(0,', self.getEditorText(), 'gets random')
           self.assertIn('print(', self.getEditorText(), 'prints')
   myTests().main()
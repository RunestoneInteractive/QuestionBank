.. mchoice:: ePost_5_21
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPAbilitySummary
   :subchapter: examPost
   :topics: CSPAbilitySummary/examPost
   :from_source: T
   :answer_a: It will print "Hello Fred"
   :answer_b: It will print "Good-bye Fred"
   :answer_c: It will print "Hello name"
   :answer_d: It will print hello + " " + name
   :correct: b
   :feedback_a: Even though the variable is called hello it contains "Good-bye".
   :feedback_b: Yes, this is what it will print.
   :feedback_c: It prints the value in name which has been set to "Fred".
   :feedback_d: It will print the value of hello and then a space and the value of name.

   Given the following code segment, which of the below statements is true?

   ::

      hello = "Good-bye"
      fred = "name"
      name = "Fred"
      message = hello + " " + name
      print (message)
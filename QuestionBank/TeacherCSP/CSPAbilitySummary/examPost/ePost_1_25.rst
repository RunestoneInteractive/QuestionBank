.. mchoice:: ePost_1_25
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPAbilitySummary
   :subchapter: examPost
   :topics: CSPAbilitySummary/examPost
   :from_source: T
   :answer_a: The turtle in this example draws a pentagram.
   :answer_b: This code will generate an error.
   :answer_c: The turtle draws four lines of length 5, 11, 16, and 21
   :answer_d: The turtle draws a square.
   :correct: d
   :feedback_a: This only loops 4 times, so how can it draw a pentagram?
   :feedback_b: This will not cause an error.
   :feedback_c: This would be true if it was sue.forward(sides)
   :feedback_d: This will loop 4 times and each time draw a line of length 100 so this will be a square.

   What is the output from the program below?

   ::

      from turtle import *
      space = Screen()
      sue = Turtle()
      sue.setheading(90)
      for sides in [5,11,16,21]:
          sue.forward(100)
          sue.right(90)
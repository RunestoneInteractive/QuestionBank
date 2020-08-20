.. mchoice:: pre_10
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPrinTeasers
   :subchapter: pretest
   :topics: CSPrinTeasers/pretest
   :from_source: T
   :answer_a: The turtle in this example draws a pentagram.
   :answer_b: The turtle draws four lines of length 5, 11, 16, and 21
   :answer_c: The turtle draws a square.
   :answer_d: This code will generate an error.
   :answer_e: I don’t know
   :correct: c
   :feedback_a: It loops 4 times, how can that be a pentagram?
   :feedback_b: It always moves forward by 100.
   :feedback_c: It draws a square with a side length of 100.
   :feedback_d: No error will be generated.
   :feedback_e: That is okay.  We do not expect you to know this.
   :pct_on_first: 0.2546523017
   :total_students_attempting: 3063
   :num_students_correct: 905.0
   :mean_clicks_to_correct: 1.2298342541

   Given the following code segment, which of the statements below is true?
   
   ::
   
      from turtle import *
      space = Screen()
      alisha = Turtle()
      alisha.setheading(90)
      for sides in [5,11,16,21]:
          alisha.forward(100)
          alisha.right(90)
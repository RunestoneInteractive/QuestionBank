.. mchoice:: 6_4_1_Function_Var_Q1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPNameNames
   :subchapter: namesInput
   :topics: CSPNameNames/namesInput
   :from_source: T
   :practice: T
   :answer_a: 100
   :answer_b: 50
   :answer_c: 200
   :answer_d: 90
   :correct: c
   :feedback_a: How much will it go forward?
   :feedback_b: What value is size set to?
   :feedback_c: Size is set to 200 in line 2 so this will draw a square that has a side length of 200.
   :feedback_d: It turns 90 degrees.  It doesn't go forward 90.
   :pct_on_first: 0.8304054054
   :total_students_attempting: 1480
   :num_students_correct: 1476.0
   :mean_clicks_to_correct: 1.2310298103

   What is the side length for a square drawn by the following procedure?
   
   ::
   
     def square(turtle):
         size = 200
         turtle.forward(size)
         turtle.right(90)
         turtle.forward(size)
         turtle.right(90)
         turtle.forward(size)
         turtle.right(90)
         turtle.forward(size)
         turtle.right(90)
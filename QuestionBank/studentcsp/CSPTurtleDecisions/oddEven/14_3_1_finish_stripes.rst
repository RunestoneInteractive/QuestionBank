.. mchoice:: 14_3_1_finish_stripes
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPTurtleDecisions
   :subchapter: oddEven
   :topics: CSPTurtleDecisions/oddEven
   :from_source: T
   :answer_a: 10
   :answer_b: 16
   :answer_c: 17
   :answer_d: 32
   :correct: c
   :feedback_a: This will stop before filling the top half of the space. Try it.
   :feedback_b: The turtle starts at the middle of height and draws 5 pixels below it and 5 pixels above it, so this leaves 5 pixels at the top that need to be filled.
   :feedback_c: The height of the top half is 160 and each stripe is a height of 10 so 16 nearly does it, but 17 fills the entire area.  The turtle starts in the middle of the space so the first row has 5 pixels above the middle and 5 below.
   :feedback_d: This would fill more than the top half.

   What value should you use as the parameter for the range function in line 12 to fill the top half of the drawing space with stripes?  The height of the space is 320.
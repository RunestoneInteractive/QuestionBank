.. mchoice:: assess_question2_1_1_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: week2a1
   :topics: Sequences/week2a1
   :from_source: T
   :answer_a: zpzpzpzpzp
   :answer_b: zzzzzppppp
   :answer_c: pzpzpzpzpz
   :answer_d: pppppzzzzz
   :answer_e: None of the above, an error will occur.
   :correct: c
   :feedback_a: The order of concatenation matters.
   :feedback_b: Think about the order that the program is executed in, what occurs first?
   :feedback_c: Yes, because let_two was put before let, c has "pz" and then that is repeated five times.
   :feedback_d: Think about the order that the program is executed in, what occurs first?
   :feedback_e: This is correct syntax and no errors will occur.
   :practice: T

   What will the output be for the following code?

   .. sourcecode:: python

    let = "z"
    let_two = "p"
    c = let_two + let
    m = c*5
    print(m)
.. mchoice:: assess_question5_1_1_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: week4a1
   :topics: TransformingSequences/week4a1
   :from_source: T
   :answer_a: item
   :answer_b: lst
   :answer_c: num
   :correct: a
   :feedback_a: Yes, this is the iterator variable. It changes each time but is not the whole sequence itself.
   :feedback_b: This is the sequence that we iterate over.
   :feedback_c: This is the accumulator variable. By the end of the program, it will have the total value of the integers that are in lst.
   :practice: T

   Which of these is the iterator (loop) variable?

   .. sourcecode:: python

    lst = [5, 10, 3, 8, 94, 2, 4, 9]
    num = 0
    for item in lst:
        num += item
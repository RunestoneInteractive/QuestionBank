.. mchoice:: assess_question5_1_1_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: week4a1
   :topics: TransformingSequences/week4a1
   :from_source: T
   :answer_a: cawdra
   :answer_b: elem
   :answer_c: t
   :correct: a
   :feedback_a: Yes, this is the sequence that we iterate over.
   :feedback_b: This is the iterator variable. It changes each time but is not the whole sequence itself.
   :feedback_c: This is the accumulator variable. By the end of the program, it will have a full count of how many items are in cawdra.
   :practice: T

   Which of these is the sequence?

   .. sourcecode:: python

    cawdra = ['candy', 'daisy', 'pear', 'peach', 'gem', 'crown']
    t = 0
    for elem in cawdra:
        t = t + len(elem)
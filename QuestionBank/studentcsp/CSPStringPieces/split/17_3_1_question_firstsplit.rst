.. mchoice:: 17_3_1_question_firstsplit
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPStringPieces
   :subchapter: split
   :topics: CSPStringPieces/split
   :from_source: T
   :practice: T
   :answer_a: Smith
   :answer_b: girl
   :answer_c: 65 Elm Street
   :answer_d: eat
   :answer_e: We would get an error
   :correct: c
   :feedback_a: That's pieces[1].
   :feedback_b: That's pieces[2]
   :feedback_c: The address is at position 3 in the resulting list.
   :feedback_d: That's pieces[4]
   :feedback_e: Why would this cause an error?  We can use indices to get the element at an index in a list.

   What do you think we would get if we executed ``print(pieces[3])``
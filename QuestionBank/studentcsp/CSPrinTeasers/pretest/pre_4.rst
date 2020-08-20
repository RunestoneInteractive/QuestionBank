.. mchoice:: pre_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPrinTeasers
   :subchapter: pretest
   :topics: CSPrinTeasers/pretest
   :from_source: T
   :answer_a: 10        [3, 1, -2]          -1
   :answer_b: 6          [3, 1, -2]          2
   :answer_c: 6          [3, 1, -2]         -1
   :answer_d: 6          [3, 1, -2]         -2
   :answer_e: I don’t know
   :correct: c
   :feedback_a: This would print 10 first if lists started at index 0, but they start at index 1.
   :feedback_b: Remember that lists start at index 0.
   :feedback_c: Lists start at index 0.  You can modify the value at an index.
   :feedback_d: Notice that second[2] is incremented.
   :feedback_e: That is okay.  We do not expect you to know this.

   What is the output from the program below?

   ::

      first = [10,5,10,6]
      print (first[3])
      second = [3,1,-2]
      print (second)
      second[2] = second[2] + 1
      print (second[2])
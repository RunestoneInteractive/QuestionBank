.. mchoice:: 17_6_1_Find_red
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPStringPieces
   :subchapter: createPartsOfStrings
   :topics: CSPStringPieces/createPartsOfStrings
   :from_source: T
   :practice: T
   :answer_a: 1
   :answer_b: 9
   :answer_c: 10
   :answer_d: -1
   :correct: a
   :feedback_a: The find function returns the index of the first position that contains the given string.
   :feedback_b: This would be true if it was pos = str.find(" is").
   :feedback_c: This would be true if it was pos = str.find(" is") and the first position was 1, but it is 0.
   :feedback_d: A -1 is returned if the string you are looking for isn't found.

   What will be printed when the following executes?

   ::

     str = "His shirt is red"
     pos = str.find("is")
     print(pos)